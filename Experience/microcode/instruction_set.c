/**
 * instruction_set.c — Yüksək səviyyəli təlimat → mikro kod kompilyatoru
 */

#include "instruction_set.h"

/* Təlimat adı cədvəli */
static const char *instr_names[] = {
    "CREATE_AGENT",
    "DESTROY_AGENT",
    "SEND_MESSAGE",
    "PROCESS_TASK",
    "SYNC_AGENTS",
    "EVALUATE",
    "REPORT"
};

const char *instruction_name(HighLevelInstruction instr)
{
    if (instr <= INSTR_REPORT) return instr_names[instr];
    return "UNKNOWN";
}

/* ─────────────────────────────────────────────────────────
 *  instruction_compile  —  Yüksək səviyyə → mikro kod
 *
 *  Hər yüksək səviyyəli təlimat bir neçə mikro təlimata
 *  açılır (genişləndirilə bilən sadə kompilyator).
 * ───────────────────────────────────────────────────────── */
int instruction_compile(const Instruction *instr, uint32_t count,
                        MicrocodeProgram *out)
{
    if (!instr || !out) return RESULT_INVALID;

    microcode_init(out);

    uint32_t mc_idx = 0;

    for (uint32_t i = 0; i < count && mc_idx < MICROCODE_MAX_INSTRUCTIONS - 2; i++) {

        LOG_INFO("Kompilyasiya: %s  (p1=%u, p2=%u)",
                 instruction_name(instr[i].opcode),
                 instr[i].param1, instr[i].param2);

        switch (instr[i].opcode) {

        case INSTR_CREATE_AGENT:
            out->instructions[mc_idx++] = (MicroInstruction){
                MC_AGENT_INIT, instr[i].param1, 0, 0 };
            out->instructions[mc_idx++] = (MicroInstruction){
                MC_LOAD, instr[i].param1, 0, 1 };
            break;

        case INSTR_DESTROY_AGENT:
            out->instructions[mc_idx++] = (MicroInstruction){
                MC_AGENT_HALT, instr[i].param1, 0, 0 };
            break;

        case INSTR_SEND_MESSAGE:
            out->instructions[mc_idx++] = (MicroInstruction){
                MC_MSG_SEND, instr[i].param1, instr[i].param2, 0 };
            break;

        case INSTR_PROCESS_TASK:
            out->instructions[mc_idx++] = (MicroInstruction){
                MC_AGENT_EXEC, instr[i].param1, 0, 0 };
            break;

        case INSTR_SYNC_AGENTS:
            out->instructions[mc_idx++] = (MicroInstruction){
                MC_NOP, 0, 0, 0 };     /* placeholder sync */
            break;

        case INSTR_EVALUATE:
            out->instructions[mc_idx++] = (MicroInstruction){
                MC_CMP, instr[i].param1, instr[i].param2, 0 };
            break;

        case INSTR_REPORT:
            out->instructions[mc_idx++] = (MicroInstruction){
                MC_STORE, instr[i].param1, 0, 0 };
            break;
        }
    }

    /* Proqramı HALT ilə bitir */
    out->instructions[mc_idx++] = (MicroInstruction){ MC_HALT, 0, 0, 0 };
    out->count = mc_idx;

    LOG_INFO("Kompilyasiya tamamlandı: %u yüksək → %u mikro təlimat",
             count, mc_idx);
    return RESULT_OK;
}
