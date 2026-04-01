/**
 * core.h — Çəkirdək (Kernel) əsas başlıq faylı
 * Agent idarəetmə sistemi üçün nüvə tərifləri
 */

#ifndef KERNEL_CORE_H
#define KERNEL_CORE_H

#include "../include/common.h"

/* ── Çəkirdək konfiqurasiyası ─────────────────────────── */
#define KERNEL_MAX_AGENTS       64
#define KERNEL_TICK_INTERVAL_MS 10
#define KERNEL_STACK_SIZE       4096

/* ── Çəkirdək statusu ────────────────────────────────── */
typedef enum {
    KERNEL_STATE_INIT,
    KERNEL_STATE_RUNNING,
    KERNEL_STATE_PAUSED,
    KERNEL_STATE_SHUTDOWN
} KernelState;

/* ── Çəkirdək strukturu ──────────────────────────────── */
typedef struct {
    KernelState  state;
    uint32_t     tick_count;
    uint32_t     agent_count;
    Agent        agents[KERNEL_MAX_AGENTS];
    uint64_t     uptime_ms;
} Kernel;

/* ── API ──────────────────────────────────────────────── */
int     kernel_init(Kernel *k);
int     kernel_start(Kernel *k);
int     kernel_stop(Kernel *k);
int     kernel_tick(Kernel *k);

int     kernel_register_agent(Kernel *k, const Agent *agent);
int     kernel_unregister_agent(Kernel *k, uint32_t agent_id);
Agent  *kernel_get_agent(Kernel *k, uint32_t agent_id);

void    kernel_log_status(const Kernel *k);

#endif /* KERNEL_CORE_H */
