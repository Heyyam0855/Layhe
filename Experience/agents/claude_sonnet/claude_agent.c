/**
 * claude_agent.c — Claude Sonnet 4.6 Agent implementasiyası
 * Süni intellekt əsaslı agent — dil modeli simulyasiyası
 */

#include "claude_agent.h"

/* ── Daxili yardımçı: tapşırıq adı ───────────────────── */
static const char *task_type_name(ClaudeTaskType t)
{
    switch (t) {
    case CLAUDE_TASK_TEXT_GENERATION: return "Mətn yaratma";
    case CLAUDE_TASK_CODE_GENERATION: return "Kod yaratma";
    case CLAUDE_TASK_ANALYSIS:        return "Analiz";
    case CLAUDE_TASK_REASONING:       return "Mühakimə";
    case CLAUDE_TASK_TRANSLATION:     return "Tərcümə";
    case CLAUDE_TASK_SUMMARIZATION:   return "Xülasə";
    default:                          return "Naməlum";
    }
}

/* ─────────────────────────────────────────────────────────
 *  claude_agent_init  —  Claude agentini başlat
 * ───────────────────────────────────────────────────────── */
int claude_agent_init(ClaudeAgent *ca, const char *name)
{
    if (!ca || !name) return RESULT_INVALID;

    memset(ca, 0, sizeof(ClaudeAgent));
    strncpy(ca->base.name, name, sizeof(ca->base.name) - 1);
    ca->base.type   = AGENT_TYPE_CLAUDE_SONNET;
    ca->base.status = AGENT_STATUS_IDLE;
    ca->base.priority = 10;      /* Yüksək prioritet */
    ca->base.context  = ca;

    /* Default parametrlər */
    ca->params.temperature = 0.7f;
    ca->params.top_p       = 0.9f;
    ca->params.max_tokens  = CLAUDE_MAX_TOKENS;
    ca->params.streaming   = false;

    ca->task_count          = 0;
    ca->total_input_tokens  = 0;
    ca->total_output_tokens = 0;
    ca->tasks_completed     = 0;
    ca->avg_confidence      = 0.0f;

    strncpy(ca->system_prompt,
            "Sən Claude Sonnet 4.6 süni intellekt agentisən. "
            "Dəqiq, faydalı və təhlükəsiz cavablar ver.",
            sizeof(ca->system_prompt) - 1);

    LOG_INFO("[Claude 4.6] \"%s\" yaradıldı  (model: %s)",
             name, CLAUDE_MODEL_NAME);
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  claude_agent_configure  —  Parametrləri tənzimlə
 * ───────────────────────────────────────────────────────── */
int claude_agent_configure(ClaudeAgent *ca, const ClaudeParams *params)
{
    if (!ca || !params) return RESULT_INVALID;

    ca->params = *params;
    LOG_INFO("[Claude 4.6] Parametrlər yeniləndi  "
             "(temp=%.2f, top_p=%.2f, max_tokens=%u)",
             params->temperature, params->top_p, params->max_tokens);
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  claude_agent_set_system_prompt
 * ───────────────────────────────────────────────────────── */
int claude_agent_set_system_prompt(ClaudeAgent *ca, const char *prompt)
{
    if (!ca || !prompt) return RESULT_INVALID;

    strncpy(ca->system_prompt, prompt, sizeof(ca->system_prompt) - 1);
    ca->system_prompt[sizeof(ca->system_prompt) - 1] = '\0';

    LOG_INFO("[Claude 4.6] Sistem promptu yeniləndi");
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  claude_agent_submit_task  —  Tapşırıq göndər
 * ───────────────────────────────────────────────────────── */
int claude_agent_submit_task(ClaudeAgent *ca, ClaudeTaskType type,
                              const char *input)
{
    if (!ca || !input) return RESULT_INVALID;
    if (ca->task_count >= CLAUDE_MAX_TASKS) return RESULT_NO_MEMORY;

    ClaudeTask *t = &ca->tasks[ca->task_count];
    memset(t, 0, sizeof(ClaudeTask));
    t->type = type;
    strncpy(t->input, input, CLAUDE_MAX_TOKENS - 1);
    t->input_tokens = (uint32_t)strlen(input);  /* sadələşdirilmiş token hesabı */
    t->completed    = false;
    t->confidence   = 0.0f;

    ca->task_count++;

    LOG_INFO("[Claude 4.6] Tapşırıq əlavə edildi: %s  (id=%u, tokens=%u)",
             task_type_name(type), ca->task_count - 1, t->input_tokens);
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  claude_agent_process  —  Bütün tapşırıqları icra et
 * ───────────────────────────────────────────────────────── */
int claude_agent_process(ClaudeAgent *ca)
{
    if (!ca) return RESULT_INVALID;

    ca->base.status = AGENT_STATUS_RUNNING;
    LOG_INFO("[Claude 4.6] \"%s\" emal başladı  (%u tapşırıq)",
             ca->base.name, ca->task_count);

    for (uint32_t i = 0; i < ca->task_count; i++) {
        ClaudeTask *t = &ca->tasks[i];
        if (t->completed) continue;

        /* ── Simulyasiya: tapşırıq növünə görə cavab yarat ── */
        switch (t->type) {
        case CLAUDE_TASK_TEXT_GENERATION:
            snprintf(t->output, CLAUDE_MAX_TOKENS,
                     "[Claude Sonnet 4.6 Cavab] Mətn yaradıldı: "
                     "girişə əsasən %u simvol emal edildi.", t->input_tokens);
            t->confidence = 0.92f;
            break;

        case CLAUDE_TASK_CODE_GENERATION:
            snprintf(t->output, CLAUDE_MAX_TOKENS,
                     "/* Claude Sonnet 4.6 tərəfindən yaradılmış kod */\n"
                     "#include <stdio.h>\n"
                     "int main(void) {\n"
                     "    printf(\"Salam Dünya!\\n\");\n"
                     "    return 0;\n"
                     "}\n");
            t->confidence = 0.95f;
            break;

        case CLAUDE_TASK_ANALYSIS:
            snprintf(t->output, CLAUDE_MAX_TOKENS,
                     "[Analiz Nəticəsi] %u token analiz edildi. "
                     "Əsas mövzu müəyyən edildi.", t->input_tokens);
            t->confidence = 0.88f;
            break;

        case CLAUDE_TASK_REASONING:
            snprintf(t->output, CLAUDE_MAX_TOKENS,
                     "[Mühakimə] Addım-addım mühakimə aparıldı. "
                     "Nəticə: giriş məlumatları ardıcıl və məntiqlidir.");
            t->confidence = 0.90f;
            break;

        case CLAUDE_TASK_TRANSLATION:
            snprintf(t->output, CLAUDE_MAX_TOKENS,
                     "[Tərcümə] Mətni tərcümə edildi  (%u simvol).",
                     t->input_tokens);
            t->confidence = 0.93f;
            break;

        case CLAUDE_TASK_SUMMARIZATION:
            snprintf(t->output, CLAUDE_MAX_TOKENS,
                     "[Xülasə] %u simvolluq mətn xülasə edildi. "
                     "Əsas fikirlər çıxarıldı.", t->input_tokens);
            t->confidence = 0.91f;
            break;
        }

        t->output_tokens = (uint32_t)strlen(t->output);
        t->completed     = true;

        ca->total_input_tokens  += t->input_tokens;
        ca->total_output_tokens += t->output_tokens;
        ca->tasks_completed++;

        /* Orta inam yenilə */
        ca->avg_confidence =
            (ca->avg_confidence * (ca->tasks_completed - 1) + t->confidence)
            / ca->tasks_completed;

        LOG_INFO("[Claude 4.6] Tapşırıq tamamlandı: id=%u, "
                 "out_tokens=%u, inam=%.2f",
                 i, t->output_tokens, t->confidence);
    }

    ca->base.status = AGENT_STATUS_COMPLETED;
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  claude_agent_get_result  —  Tapşırıq nəticəsini al
 * ───────────────────────────────────────────────────────── */
int claude_agent_get_result(const ClaudeAgent *ca, uint32_t task_id,
                             char *output, uint32_t max_len)
{
    if (!ca || !output || task_id >= ca->task_count)
        return RESULT_INVALID;

    const ClaudeTask *t = &ca->tasks[task_id];
    if (!t->completed) return RESULT_ERROR;

    strncpy(output, t->output, max_len - 1);
    output[max_len - 1] = '\0';
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  claude_agent_status  —  Status çap et
 * ───────────────────────────────────────────────────────── */
void claude_agent_status(const ClaudeAgent *ca)
{
    if (!ca) return;

    const char *status_str[] = {
        "IDLE", "RUNNING", "WAITING", "COMPLETED", "ERROR"
    };

    printf("\n=== Claude Sonnet 4.6 Agent: \"%s\" ===============\n",
           ca->base.name);
    printf("  Model           : %s\n", CLAUDE_MODEL_NAME);
    printf("  Status          : %s\n", status_str[ca->base.status]);
    printf("  Prioritet       : %u\n", ca->base.priority);
    printf("  Temperature     : %.2f\n", ca->params.temperature);
    printf("  Top_p           : %.2f\n", ca->params.top_p);
    printf("  Max tokens      : %u\n", ca->params.max_tokens);
    printf("  Tapşırıqlar     : %u (%u tamamlanmış)\n",
           ca->task_count, ca->tasks_completed);
    printf("  Giriş tokenləri : %u\n", ca->total_input_tokens);
    printf("  Çıxış tokenləri : %u\n", ca->total_output_tokens);
    printf("  Orta inam       : %.2f\n", ca->avg_confidence);
    printf("=================================================\n\n");
}

/* ─────────────────────────────────────────────────────────
 *  claude_agent_reset_stats  —  Statistikanı sıfırla
 * ───────────────────────────────────────────────────────── */
void claude_agent_reset_stats(ClaudeAgent *ca)
{
    if (!ca) return;
    ca->task_count          = 0;
    ca->total_input_tokens  = 0;
    ca->total_output_tokens = 0;
    ca->tasks_completed     = 0;
    ca->avg_confidence      = 0.0f;
    LOG_INFO("[Claude 4.6] Statistika sıfırlandı");
}
