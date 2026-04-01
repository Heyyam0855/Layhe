/**
 * xususi_agent.c — Xüsusi Agent implementasiyası
 * Qaydalar əsasında qərar qəbul edən xüsusi agent
 */

#include "xususi_agent.h"

/* ─────────────────────────────────────────────────────────
 *  xususi_agent_init  —  Xüsusi agenti başlat
 * ───────────────────────────────────────────────────────── */
int xususi_agent_init(XususiAgent *xa, const char *name)
{
    if (!xa || !name) return RESULT_INVALID;

    memset(xa, 0, sizeof(XususiAgent));
    strncpy(xa->base.name, name, sizeof(xa->base.name) - 1);
    xa->base.type   = AGENT_TYPE_XUSUSI;
    xa->base.status = AGENT_STATUS_IDLE;
    xa->base.priority = 5;
    xa->base.context  = xa;

    xa->rule_count        = 0;
    xa->actions_executed  = 0;
    xa->knowledge_level   = 0;
    xa->experience_points = 0;

    LOG_INFO("[Xüsusi Agent] \"%s\" yaradıldı", name);
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  xususi_agent_add_rule  —  Yeni qayda əlavə et
 * ───────────────────────────────────────────────────────── */
int xususi_agent_add_rule(XususiAgent *xa, const XususiRule *rule)
{
    if (!xa || !rule) return RESULT_INVALID;
    if (xa->rule_count >= XUSUSI_MAX_RULES) return RESULT_NO_MEMORY;

    xa->rules[xa->rule_count] = *rule;
    xa->rules[xa->rule_count].enabled = true;
    xa->rule_count++;

    LOG_INFO("[Xüsusi Agent] Qayda əlavə edildi: \"%s\"  (növ=%d)",
             rule->description, rule->type);
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  xususi_agent_evaluate  —  Girişi qiymətləndir
 * ───────────────────────────────────────────────────────── */
int xususi_agent_evaluate(XususiAgent *xa, uint32_t input)
{
    if (!xa) return RESULT_INVALID;

    int matched = 0;

    for (uint32_t i = 0; i < xa->rule_count; i++) {
        XususiRule *r = &xa->rules[i];
        if (!r->enabled) continue;

        bool fire = false;
        switch (r->type) {
        case RULE_IF_EQUAL:    fire = (input == r->condition_value); break;
        case RULE_IF_GREATER:  fire = (input >  r->condition_value); break;
        case RULE_IF_LESS:     fire = (input <  r->condition_value); break;
        case RULE_IF_CONTAINS: fire = ((input & r->condition_value) != 0); break;
        case RULE_ALWAYS:      fire = true; break;
        }

        if (fire) {
            LOG_INFO("[Xüsusi Agent] Qayda tetiklendi: \"%s\"  (action=%u)",
                     r->description, r->action_id);
            matched++;
        }
    }

    return matched;
}

/* ─────────────────────────────────────────────────────────
 *  xususi_agent_execute  —  Agenti icra et
 * ───────────────────────────────────────────────────────── */
int xususi_agent_execute(XususiAgent *xa)
{
    if (!xa) return RESULT_INVALID;

    xa->base.status = AGENT_STATUS_RUNNING;
    xa->actions_executed++;

    LOG_INFO("[Xüsusi Agent] \"%s\" icra olunur  (dəfə: %u)",
             xa->base.name, xa->actions_executed);

    /* Hər icrada bəzi təcrübə xalları qazanır */
    xususi_agent_learn(xa, 10);

    xa->base.status = AGENT_STATUS_COMPLETED;
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  xususi_agent_learn  —  Təcrübə qazan
 * ───────────────────────────────────────────────────────── */
int xususi_agent_learn(XususiAgent *xa, uint32_t xp)
{
    if (!xa) return RESULT_INVALID;

    xa->experience_points += xp;

    /* Hər 100 XP-də bilik səviyyəsi artır */
    uint32_t new_level = xa->experience_points / 100;
    if (new_level > 100) new_level = 100;

    if (new_level > xa->knowledge_level) {
        xa->knowledge_level = new_level;
        LOG_INFO("[Xüsusi Agent] \"%s\" bilik səviyyəsi artdı: %u",
                 xa->base.name, new_level);
    }

    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  xususi_agent_status  —  Status çap et
 * ───────────────────────────────────────────────────────── */
void xususi_agent_status(const XususiAgent *xa)
{
    if (!xa) return;

    const char *status_str[] = {
        "IDLE", "RUNNING", "WAITING", "COMPLETED", "ERROR"
    };

    printf("\n=== Xüsusi Agent: \"%s\" ==========================\n",
           xa->base.name);
    printf("  ID              : %u\n", xa->base.id);
    printf("  Növ             : Xüsusi\n");
    printf("  Status          : %s\n", status_str[xa->base.status]);
    printf("  Prioritet       : %u\n", xa->base.priority);
    printf("  Qaydalar        : %u\n", xa->rule_count);
    printf("  İcra sayı       : %u\n", xa->actions_executed);
    printf("  Bilik səviyyəsi : %u / 100\n", xa->knowledge_level);
    printf("  Təcrübə xalları : %u\n", xa->experience_points);
    printf("=================================================\n\n");
}
