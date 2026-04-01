/**
 * claude_agent.h — Claude Sonnet 4.6 Agent modulu
 * Süni intellekt əsaslı agent — dil modeli simulyasiyası
 */

#ifndef CLAUDE_AGENT_H
#define CLAUDE_AGENT_H

#include "../../include/common.h"

/* ── Claude Agent konfiqurasiyası ─────────────────────── */
#define CLAUDE_MODEL_NAME       "Claude Sonnet 4.6"
#define CLAUDE_MAX_TOKENS       4096
#define CLAUDE_MAX_CONTEXT      8192
#define CLAUDE_MAX_TASKS        128

/* ── Tapşırıq növləri ─────────────────────────────────── */
typedef enum {
    CLAUDE_TASK_TEXT_GENERATION,     /* Mətn yaratma          */
    CLAUDE_TASK_CODE_GENERATION,     /* Kod yaratma           */
    CLAUDE_TASK_ANALYSIS,            /* Analiz                */
    CLAUDE_TASK_REASONING,           /* Mühakimə              */
    CLAUDE_TASK_TRANSLATION,         /* Tərcümə               */
    CLAUDE_TASK_SUMMARIZATION        /* Xülasə                */
} ClaudeTaskType;

/* ── Tapşırıq strukturu ──────────────────────────────── */
typedef struct {
    ClaudeTaskType  type;
    char            input[CLAUDE_MAX_TOKENS];
    char            output[CLAUDE_MAX_TOKENS];
    uint32_t        input_tokens;
    uint32_t        output_tokens;
    float           confidence;          /* 0.0 — 1.0          */
    bool            completed;
} ClaudeTask;

/* ── Model parametrləri ───────────────────────────────── */
typedef struct {
    float    temperature;       /* 0.0 — 2.0   yaradıcılıq    */
    float    top_p;             /* 0.0 — 1.0   seçim          */
    uint32_t max_tokens;        /* Cavab limiti                 */
    bool     streaming;         /* Axın rejimi                  */
} ClaudeParams;

/* ── Claude Agent konteksti ──────────────────────────── */
typedef struct {
    Agent           base;               /* əsas agent strukturu    */
    ClaudeParams    params;
    ClaudeTask      tasks[CLAUDE_MAX_TASKS];
    uint32_t        task_count;
    uint32_t        total_input_tokens;
    uint32_t        total_output_tokens;
    uint32_t        tasks_completed;
    float           avg_confidence;
    char            system_prompt[CLAUDE_MAX_CONTEXT];
} ClaudeAgent;

/* ── API ──────────────────────────────────────────────── */
int     claude_agent_init(ClaudeAgent *ca, const char *name);
int     claude_agent_configure(ClaudeAgent *ca, const ClaudeParams *params);
int     claude_agent_set_system_prompt(ClaudeAgent *ca, const char *prompt);
int     claude_agent_submit_task(ClaudeAgent *ca, ClaudeTaskType type,
                                  const char *input);
int     claude_agent_process(ClaudeAgent *ca);
int     claude_agent_get_result(const ClaudeAgent *ca, uint32_t task_id,
                                 char *output, uint32_t max_len);
void    claude_agent_status(const ClaudeAgent *ca);
void    claude_agent_reset_stats(ClaudeAgent *ca);

#endif /* CLAUDE_AGENT_H */
