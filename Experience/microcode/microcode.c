/**
 * microcode.c — Mikro kod mühərriki implementasiyası
 */

#include "microcode.h"

/* ─────────────────────────────────────────────────────────
 *  microcode_init
 * ───────────────────────────────────────────────────────── */
int microcode_init(MicrocodeProgram *prog)
{
    if (!prog) return RESULT_INVALID;

    memset(prog, 0, sizeof(MicrocodeProgram));
    prog->halted = false;

    LOG_INFO("Mikro kod mühərriki başladı");
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  microcode_load  —  Təlimatları yüklə
 * ───────────────────────────────────────────────────────── */
int microcode_load(MicrocodeProgram *prog,
                   const MicroInstruction *instr, uint32_t count)
{
    if (!prog || !instr) return RESULT_INVALID;
    if (count > MICROCODE_MAX_INSTRUCTIONS) return RESULT_NO_MEMORY;

    memcpy(prog->instructions, instr, count * sizeof(MicroInstruction));
    prog->count = count;
    prog->pc    = 0;

    LOG_INFO("Mikro proqram yükləndi  (%u təlimat)", count);
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  microcode_step  —  Bir təlimat icra et
 * ───────────────────────────────────────────────────────── */
int microcode_step(MicrocodeProgram *prog)
{
    if (!prog || prog->halted) return RESULT_ERROR;
    if (prog->pc >= prog->count) {
        prog->halted = true;
        return RESULT_OK;
    }

    MicroInstruction *mi = &prog->instructions[prog->pc];

    switch (mi->opcode) {

    case MC_NOP:
        break;

    case MC_LOAD:
        if (mi->result < 16)
            prog->registers[mi->result] = mi->operand_a;
        break;

    case MC_STORE:
        mi->result = (mi->operand_a < 16) ? prog->registers[mi->operand_a] : 0;
        break;

    case MC_ADD:
        if (mi->result < 16 && mi->operand_a < 16 && mi->operand_b < 16)
            prog->registers[mi->result] =
                prog->registers[mi->operand_a] + prog->registers[mi->operand_b];
        break;

    case MC_SUB:
        if (mi->result < 16 && mi->operand_a < 16 && mi->operand_b < 16)
            prog->registers[mi->result] =
                prog->registers[mi->operand_a] - prog->registers[mi->operand_b];
        break;

    case MC_MUL:
        if (mi->result < 16 && mi->operand_a < 16 && mi->operand_b < 16)
            prog->registers[mi->result] =
                prog->registers[mi->operand_a] * prog->registers[mi->operand_b];
        break;

    case MC_CMP:
        if (mi->operand_a < 16 && mi->operand_b < 16)
            prog->registers[0] =
                (prog->registers[mi->operand_a] == prog->registers[mi->operand_b])
                    ? 1 : 0;
        break;

    case MC_JMP:
        prog->pc = mi->operand_a;
        return RESULT_OK;   /* pc artıq dəyişdi */

    case MC_JEQ:
        if (prog->registers[0] == 1) {
            prog->pc = mi->operand_a;
            return RESULT_OK;
        }
        break;

    case MC_CALL:
        /* Sadə çağırış — geri dönüş ünvanını r15-ə yazır */
        prog->registers[15] = prog->pc + 1;
        prog->pc = mi->operand_a;
        return RESULT_OK;

    case MC_RET:
        prog->pc = prog->registers[15];
        return RESULT_OK;

    case MC_AGENT_INIT:
        LOG_INFO("MC_AGENT_INIT  (id=%u)", mi->operand_a);
        break;

    case MC_AGENT_EXEC:
        LOG_INFO("MC_AGENT_EXEC  (id=%u)", mi->operand_a);
        break;

    case MC_AGENT_HALT:
        LOG_INFO("MC_AGENT_HALT  (id=%u)", mi->operand_a);
        break;

    case MC_MSG_SEND:
        LOG_INFO("MC_MSG_SEND  (from=%u, to=%u)", mi->operand_a, mi->operand_b);
        break;

    case MC_MSG_RECV:
        LOG_INFO("MC_MSG_RECV  (agent=%u)", mi->operand_a);
        break;

    case MC_HALT:
        prog->halted = true;
        LOG_INFO("Mikro mühərrik HALT");
        return RESULT_OK;

    default:
        LOG_WARN("Bilinməyən opcode: 0x%02X", mi->opcode);
        break;
    }

    prog->pc++;
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  microcode_run  —  Bütün proqramı icra et
 * ───────────────────────────────────────────────────────── */
int microcode_run(MicrocodeProgram *prog)
{
    if (!prog) return RESULT_INVALID;

    while (!prog->halted) {
        int r = microcode_step(prog);
        if (r != RESULT_OK) return r;
    }
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  microcode_reset
 * ───────────────────────────────────────────────────────── */
void microcode_reset(MicrocodeProgram *prog)
{
    if (!prog) return;
    prog->pc = 0;
    prog->halted = false;
    memset(prog->registers, 0, sizeof(prog->registers));
    LOG_INFO("Mikro mühərrik sıfırlandı");
}

/* ─────────────────────────────────────────────────────────
 *  microcode_dump  —  Registrləri çap et
 * ───────────────────────────────────────────────────────── */
void microcode_dump(const MicrocodeProgram *prog)
{
    if (!prog) return;

    printf("\n=== Mikro Kod Dump ==============================\n");
    printf("  PC      : %u / %u\n", prog->pc, prog->count);
    printf("  Halted  : %s\n", prog->halted ? "Bəli" : "Xeyr");
    printf("  Registrlər:\n");
    for (int i = 0; i < 16; i++)
        printf("    r%-2d = 0x%08X  (%u)\n", i, prog->registers[i], prog->registers[i]);
    printf("=================================================\n\n");
}
