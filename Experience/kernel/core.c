/**
 * core.c — Çəkirdək (Kernel) əsas implementasiyası
 * Agent idarəetmə nüvəsi
 */

#include "core.h"

/* ─────────────────────────────────────────────────────────
 *  kernel_init  —  Çəkirdəyi başlat
 * ───────────────────────────────────────────────────────── */
int kernel_init(Kernel *k)
{
    if (!k) return RESULT_INVALID;

    memset(k, 0, sizeof(Kernel));
    k->state       = KERNEL_STATE_INIT;
    k->tick_count  = 0;
    k->agent_count = 0;
    k->uptime_ms   = 0;

    LOG_INFO("Çəkirdək başladılır  (versiya %s)", PROJECT_VERSION);
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  kernel_start  —  Çəkirdəyi işə sal
 * ───────────────────────────────────────────────────────── */
int kernel_start(Kernel *k)
{
    if (!k) return RESULT_INVALID;
    if (k->state != KERNEL_STATE_INIT && k->state != KERNEL_STATE_PAUSED)
        return RESULT_ERROR;

    k->state = KERNEL_STATE_RUNNING;
    LOG_INFO("Çəkirdək işə düşdü  (agentlər: %u)", k->agent_count);
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  kernel_stop  —  Çəkirdəyi dayandır
 * ───────────────────────────────────────────────────────── */
int kernel_stop(Kernel *k)
{
    if (!k) return RESULT_INVALID;

    k->state = KERNEL_STATE_SHUTDOWN;
    LOG_INFO("Çəkirdək dayandırıldı  (tick: %u, uptime: %llu ms)",
             k->tick_count, (unsigned long long)k->uptime_ms);
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  kernel_tick  —  Bir addım irəli
 * ───────────────────────────────────────────────────────── */
int kernel_tick(Kernel *k)
{
    if (!k || k->state != KERNEL_STATE_RUNNING)
        return RESULT_ERROR;

    k->tick_count++;
    k->uptime_ms += KERNEL_TICK_INTERVAL_MS;

    /* Hər agenti bir dəfə çağır */
    for (uint32_t i = 0; i < k->agent_count; i++) {
        if (k->agents[i].status == AGENT_STATUS_RUNNING) {
            /* Agent kontekstini icra et (genişləndirilə bilər) */
        }
    }
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  kernel_register_agent  —  Agenti qeydiyyatdan keçir
 * ───────────────────────────────────────────────────────── */
int kernel_register_agent(Kernel *k, const Agent *agent)
{
    if (!k || !agent) return RESULT_INVALID;
    if (k->agent_count >= KERNEL_MAX_AGENTS) return RESULT_NO_MEMORY;

    k->agents[k->agent_count] = *agent;
    k->agents[k->agent_count].id = k->agent_count + 1;
    k->agent_count++;

    LOG_INFO("Agent qeydiyyatdan keçdi: \"%s\"  (id=%u, növ=%s)",
             agent->name,
             k->agents[k->agent_count - 1].id,
             agent->type == AGENT_TYPE_XUSUSI ? "Xüsusi" : "Claude-Sonnet-4.6");
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  kernel_unregister_agent  —  Agenti sil
 * ───────────────────────────────────────────────────────── */
int kernel_unregister_agent(Kernel *k, uint32_t agent_id)
{
    if (!k || agent_id == 0) return RESULT_INVALID;

    for (uint32_t i = 0; i < k->agent_count; i++) {
        if (k->agents[i].id == agent_id) {
            /* Son elementi bu yerinə köçür */
            k->agents[i] = k->agents[k->agent_count - 1];
            k->agent_count--;
            LOG_INFO("Agent silindi: id=%u", agent_id);
            return RESULT_OK;
        }
    }
    return RESULT_ERROR;
}

/* ─────────────────────────────────────────────────────────
 *  kernel_get_agent  —  Agent-ə göstərici al
 * ───────────────────────────────────────────────────────── */
Agent *kernel_get_agent(Kernel *k, uint32_t agent_id)
{
    if (!k) return NULL;
    for (uint32_t i = 0; i < k->agent_count; i++) {
        if (k->agents[i].id == agent_id)
            return &k->agents[i];
    }
    return NULL;
}

/* ─────────────────────────────────────────────────────────
 *  kernel_log_status  —  Status çap et
 * ───────────────────────────────────────────────────────── */
void kernel_log_status(const Kernel *k)
{
    if (!k) return;

    const char *state_str[] = { "INIT", "RUNNING", "PAUSED", "SHUTDOWN" };

    printf("\n=== Çəkirdək Statusu ============================\n");
    printf("  Vəziyyət  : %s\n", state_str[k->state]);
    printf("  Tick       : %u\n", k->tick_count);
    printf("  Uptime     : %llu ms\n", (unsigned long long)k->uptime_ms);
    printf("  Agentlər   : %u / %d\n", k->agent_count, KERNEL_MAX_AGENTS);
    printf("=================================================\n\n");
}
