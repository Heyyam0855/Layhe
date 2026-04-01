/**
 * scheduler.h — Agent planlaşdırıcı (Scheduler)
 * Agentlərin icra sırasını idarə edir
 */

#ifndef KERNEL_SCHEDULER_H
#define KERNEL_SCHEDULER_H

#include "core.h"

/* ── Planlaşdırma alqoritmləri ────────────────────────── */
typedef enum {
    SCHED_ROUND_ROBIN,
    SCHED_PRIORITY,
    SCHED_FIFO
} SchedulerPolicy;

/* ── Planlaşdırıcı strukturu ─────────────────────────── */
typedef struct {
    SchedulerPolicy  policy;
    uint32_t         current_index;
    uint32_t         quantum_ms;
} Scheduler;

/* ── API ──────────────────────────────────────────────── */
int     scheduler_init(Scheduler *s, SchedulerPolicy policy);
Agent  *scheduler_next(Scheduler *s, Kernel *k);
int     scheduler_set_policy(Scheduler *s, SchedulerPolicy policy);
void    scheduler_reset(Scheduler *s);

#endif /* KERNEL_SCHEDULER_H */
