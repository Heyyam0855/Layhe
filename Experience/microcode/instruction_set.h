/**
 * instruction_set.h — Təlimat dəsti (Instruction Set)
 * Yüksək səviyyəli agent əmrlərini mikro koda çevirir
 */

#ifndef INSTRUCTION_SET_H
#define INSTRUCTION_SET_H

#include "microcode.h"

/* ── Yüksək səviyyəli əmrlər ─────────────────────────── */
typedef enum {
    INSTR_CREATE_AGENT,       /* Yeni agent yarat           */
    INSTR_DESTROY_AGENT,      /* Agenti məhv et             */
    INSTR_SEND_MESSAGE,       /* Mesaj göndər               */
    INSTR_PROCESS_TASK,       /* Tapşırığı icra et          */
    INSTR_SYNC_AGENTS,        /* Agentləri sinxronlaşdır    */
    INSTR_EVALUATE,           /* Nəticəni qiymətləndir      */
    INSTR_REPORT              /* Hesabat hazırla            */
} HighLevelInstruction;

/* ── Təlimat dəsti proqramı ───────────────────────────── */
typedef struct {
    HighLevelInstruction  opcode;
    uint32_t              param1;
    uint32_t              param2;
    char                  label[32];
} Instruction;

/* ── API ──────────────────────────────────────────────── */
int  instruction_compile(const Instruction *instr, uint32_t count,
                         MicrocodeProgram *out);
const char *instruction_name(HighLevelInstruction instr);

#endif /* INSTRUCTION_SET_H */
