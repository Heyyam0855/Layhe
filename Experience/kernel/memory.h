/**
 * memory.h — Yaddaş idarəetməsi (Memory Manager)
 * Agentlər üçün yaddaş ayırma / geri qaytarma
 */

#ifndef KERNEL_MEMORY_H
#define KERNEL_MEMORY_H

#include "core.h"

/* ── Yaddaş bloku ─────────────────────────────────────── */
#define MEMORY_POOL_SIZE  (64 * 1024)   /* 64 KB */
#define MEMORY_BLOCK_SIZE 256           /* bayt    */
#define MEMORY_BLOCK_COUNT (MEMORY_POOL_SIZE / MEMORY_BLOCK_SIZE)

typedef struct {
    uint8_t  pool[MEMORY_POOL_SIZE];
    bool     used[MEMORY_BLOCK_COUNT];
    uint32_t free_blocks;
} MemoryPool;

/* ── API ──────────────────────────────────────────────── */
int     memory_init(MemoryPool *mp);
void   *memory_alloc(MemoryPool *mp, uint32_t size);
int     memory_free(MemoryPool *mp, void *ptr);
uint32_t memory_available(const MemoryPool *mp);
void    memory_dump_stats(const MemoryPool *mp);

#endif /* KERNEL_MEMORY_H */
