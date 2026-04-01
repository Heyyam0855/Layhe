/**
 * scheduler.c — Agent planlaşdırıcı implementasiyası
 */

#include "scheduler.h"

/* ─────────────────────────────────────────────────────────
 *  scheduler_init
 * ───────────────────────────────────────────────────────── */
int scheduler_init(Scheduler *s, SchedulerPolicy policy)
{
    if (!s) return RESULT_INVALID;

    s->policy        = policy;
    s->current_index = 0;
    s->quantum_ms    = 100;   /* default: 100 ms */

    LOG_INFO("Planlaşdırıcı başladı  (siyasət: %d)", policy);
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  scheduler_next  —  Növbəti icra olunacaq agenti seç
 * ───────────────────────────────────────────────────────── */
Agent *scheduler_next(Scheduler *s, Kernel *k)
{
    if (!s || !k || k->agent_count == 0)
        return NULL;

    switch (s->policy) {

    case SCHED_ROUND_ROBIN: {
        uint32_t start = s->current_index;
        do {
            Agent *a = &k->agents[s->current_index];
            s->current_index = (s->current_index + 1) % k->agent_count;
            if (a->status == AGENT_STATUS_RUNNING ||
                a->status == AGENT_STATUS_IDLE)
                return a;
        } while (s->current_index != start);
        return NULL;
    }

    case SCHED_PRIORITY: {
        Agent *best = NULL;
        for (uint32_t i = 0; i < k->agent_count; i++) {
            Agent *a = &k->agents[i];
            if ((a->status == AGENT_STATUS_RUNNING ||
                 a->status == AGENT_STATUS_IDLE) &&
                (!best || a->priority > best->priority))
                best = a;
        }
        return best;
    }

    case SCHED_FIFO:
        for (uint32_t i = 0; i < k->agent_count; i++) {
            if (k->agents[i].status == AGENT_STATUS_RUNNING ||
                k->agents[i].status == AGENT_STATUS_IDLE)
                return &k->agents[i];
        }
        return NULL;

    default:
        return NULL;
    }
}

/* ─────────────────────────────────────────────────────────
 *  scheduler_set_policy
 * ───────────────────────────────────────────────────────── */
int scheduler_set_policy(Scheduler *s, SchedulerPolicy policy)
{
    if (!s) return RESULT_INVALID;
    s->policy = policy;
    s->current_index = 0;
    LOG_INFO("Planlaşdırma siyasəti dəyişdi: %d", policy);
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  scheduler_reset
 * ───────────────────────────────────────────────────────── */
void scheduler_reset(Scheduler *s)
{
    if (s) s->current_index = 0;
}
