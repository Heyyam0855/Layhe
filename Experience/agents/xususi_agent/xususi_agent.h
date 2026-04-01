/**
 * xususi_agent.h — Xüsusi Agent modulu
 * Fərdiləşdirilmiş davranış və qaydalar əsasında işləyən agent
 */

#ifndef XUSUSI_AGENT_H
#define XUSUSI_AGENT_H

#include "../../include/common.h"

/* ── Xüsusi Agent konfiqurasiyası ─────────────────────── */
#define XUSUSI_MAX_RULES    32
#define XUSUSI_MAX_ACTIONS  64

/* ── Qayda növləri ────────────────────────────────────── */
typedef enum {
    RULE_IF_EQUAL,
    RULE_IF_GREATER,
    RULE_IF_LESS,
    RULE_IF_CONTAINS,
    RULE_ALWAYS
} RuleType;

/* ── Qayda strukturu ─────────────────────────────────── */
typedef struct {
    RuleType   type;
    uint32_t   condition_value;
    uint32_t   action_id;
    char       description[64];
    bool       enabled;
} XususiRule;

/* ── Xüsusi Agent konteksti ──────────────────────────── */
typedef struct {
    Agent           base;               /* əsas agent strukturu    */
    XususiRule      rules[XUSUSI_MAX_RULES];
    uint32_t        rule_count;
    uint32_t        actions_executed;
    uint32_t        knowledge_level;    /* bilik səviyyəsi 0-100  */
    uint32_t        experience_points;  /* təcrübə xalları        */
} XususiAgent;

/* ── API ──────────────────────────────────────────────── */
int     xususi_agent_init(XususiAgent *xa, const char *name);
int     xususi_agent_add_rule(XususiAgent *xa, const XususiRule *rule);
int     xususi_agent_evaluate(XususiAgent *xa, uint32_t input);
int     xususi_agent_execute(XususiAgent *xa);
int     xususi_agent_learn(XususiAgent *xa, uint32_t xp);
void    xususi_agent_status(const XususiAgent *xa);

#endif /* XUSUSI_AGENT_H */
