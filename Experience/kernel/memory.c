/**
 * memory.c — Yaddaş idarəetməsi implementasiyası
 */

#include "memory.h"

/* ─────────────────────────────────────────────────────────
 *  memory_init
 * ───────────────────────────────────────────────────────── */
int memory_init(MemoryPool *mp)
{
    if (!mp) return RESULT_INVALID;

    memset(mp->pool, 0, MEMORY_POOL_SIZE);
    memset(mp->used, 0, sizeof(mp->used));
    mp->free_blocks = MEMORY_BLOCK_COUNT;

    LOG_INFO("Yaddaş havuzu başladı  (%d blok, hər biri %d bayt)",
             MEMORY_BLOCK_COUNT, MEMORY_BLOCK_SIZE);
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  memory_alloc  —  Yaddaş ayır
 * ───────────────────────────────────────────────────────── */
void *memory_alloc(MemoryPool *mp, uint32_t size)
{
    if (!mp || size == 0) return NULL;

    uint32_t blocks_needed = (size + MEMORY_BLOCK_SIZE - 1) / MEMORY_BLOCK_SIZE;
    if (blocks_needed > mp->free_blocks) return NULL;

    /* Ardıcıl boş blok axtar */
    uint32_t consecutive = 0;
    uint32_t start = 0;

    for (uint32_t i = 0; i < MEMORY_BLOCK_COUNT; i++) {
        if (!mp->used[i]) {
            if (consecutive == 0) start = i;
            consecutive++;
            if (consecutive >= blocks_needed) {
                /* Tapıldı — işarələ */
                for (uint32_t j = start; j < start + blocks_needed; j++)
                    mp->used[j] = true;
                mp->free_blocks -= blocks_needed;
                return &mp->pool[start * MEMORY_BLOCK_SIZE];
            }
        } else {
            consecutive = 0;
        }
    }
    return NULL;   /* kifayət qədər ardıcıl yer yox */
}

/* ─────────────────────────────────────────────────────────
 *  memory_free  —  Yaddaşı geri qaytar
 * ───────────────────────────────────────────────────────── */
int memory_free(MemoryPool *mp, void *ptr)
{
    if (!mp || !ptr) return RESULT_INVALID;

    uintptr_t offset = (uintptr_t)ptr - (uintptr_t)mp->pool;
    if (offset >= MEMORY_POOL_SIZE) return RESULT_INVALID;

    uint32_t block = (uint32_t)(offset / MEMORY_BLOCK_SIZE);
    if (!mp->used[block]) return RESULT_ERROR;

    /* Bu blokdan başlayaraq ardıcıl istifadə olunanları azad et */
    while (block < MEMORY_BLOCK_COUNT && mp->used[block]) {
        mp->used[block] = false;
        mp->free_blocks++;
        block++;
    }
    return RESULT_OK;
}

/* ─────────────────────────────────────────────────────────
 *  memory_available  —  Boş baytlar
 * ───────────────────────────────────────────────────────── */
uint32_t memory_available(const MemoryPool *mp)
{
    if (!mp) return 0;
    return mp->free_blocks * MEMORY_BLOCK_SIZE;
}

/* ─────────────────────────────────────────────────────────
 *  memory_dump_stats
 * ───────────────────────────────────────────────────────── */
void memory_dump_stats(const MemoryPool *mp)
{
    if (!mp) return;
    printf("\n=== Yaddaş Statistikası =========================\n");
    printf("  Ümumi       : %d bayt\n", MEMORY_POOL_SIZE);
    printf("  Boş         : %u bayt\n", mp->free_blocks * MEMORY_BLOCK_SIZE);
    printf("  İstifadədə  : %u bayt\n",
           (MEMORY_BLOCK_COUNT - mp->free_blocks) * MEMORY_BLOCK_SIZE);
    printf("  Bloklar     : %u / %d boş\n",
           mp->free_blocks, MEMORY_BLOCK_COUNT);
    printf("=================================================\n\n");
}
