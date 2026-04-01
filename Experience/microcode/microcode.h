/**
 * microcode.h — Mikro kod mühərriki
 * Agent əməliyyatlarını mikro təlimatlara çevirir
 */

#ifndef MICROCODE_H
#define MICROCODE_H

#include "../include/common.h"

/* ── Mikro əməliyyat kodları (opcode) ─────────────────── */
typedef enum {
    MC_NOP          = 0x00,   /* Heç nə etmə                  */
    MC_LOAD         = 0x01,   /* Registrə yüklə               */
    MC_STORE        = 0x02,   /* Yaddaşa yaz                   */
    MC_ADD          = 0x03,   /* Toplama                       */
    MC_SUB          = 0x04,   /* Çıxma                         */
    MC_MUL          = 0x05,   /* Vurma                         */
    MC_CMP          = 0x06,   /* Müqayisə                      */
    MC_JMP          = 0x07,   /* Şərtsiz keçid                 */
    MC_JEQ          = 0x08,   /* Bərabərdirsə keçid            */
    MC_CALL         = 0x09,   /* Funksiya çağır                */
    MC_RET          = 0x0A,   /* Geri qayıt                    */
    MC_AGENT_INIT   = 0x10,   /* Agent başlat                  */
    MC_AGENT_EXEC   = 0x11,   /* Agent icra et                 */
    MC_AGENT_HALT   = 0x12,   /* Agent dayandır                */
    MC_MSG_SEND     = 0x20,   /* Mesaj göndər                  */
    MC_MSG_RECV     = 0x21,   /* Mesaj al                      */
    MC_HALT         = 0xFF    /* Sistemi dayandır              */
} MicroOpcode;

/* ── Mikro təlimat ────────────────────────────────────── */
typedef struct {
    MicroOpcode opcode;
    uint32_t    operand_a;
    uint32_t    operand_b;
    uint32_t    result;
} MicroInstruction;

/* ── Mikro kod proqramı ───────────────────────────────── */
#define MICROCODE_MAX_INSTRUCTIONS 512

typedef struct {
    MicroInstruction instructions[MICROCODE_MAX_INSTRUCTIONS];
    uint32_t         count;
    uint32_t         pc;         /* program counter */
    uint32_t         registers[16];
    bool             halted;
} MicrocodeProgram;

/* ── API ──────────────────────────────────────────────── */
int     microcode_init(MicrocodeProgram *prog);
int     microcode_load(MicrocodeProgram *prog,
                       const MicroInstruction *instr, uint32_t count);
int     microcode_step(MicrocodeProgram *prog);
int     microcode_run(MicrocodeProgram *prog);
void    microcode_reset(MicrocodeProgram *prog);
void    microcode_dump(const MicrocodeProgram *prog);

#endif /* MICROCODE_H */
