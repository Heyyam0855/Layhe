/**
 * common.h — Ümumi təriflər və strukturlar
 * Experience Agent Layihəsi
 * Dil: C
 */

#ifndef COMMON_H
#define COMMON_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

/* ── Versiya ──────────────────────────────────────────── */
#define PROJECT_NAME        "Experience Agent System"
#define PROJECT_VERSION     "1.0.0"
#define BUILD_DATE          __DATE__

/* ── Agent növləri ────────────────────────────────────── */
typedef enum {
    AGENT_TYPE_XUSUSI         = 0x01,   /* Xüsusi Agent   */
    AGENT_TYPE_CLAUDE_SONNET  = 0x02    /* Claude 4.6     */
} AgentType;

/* ── Agent statusları ─────────────────────────────────── */
typedef enum {
    AGENT_STATUS_IDLE,
    AGENT_STATUS_RUNNING,
    AGENT_STATUS_WAITING,
    AGENT_STATUS_COMPLETED,
    AGENT_STATUS_ERROR
} AgentStatus;

/* ── Əsas Agent strukturu ─────────────────────────────── */
typedef struct {
    uint32_t    id;
    char        name[64];
    AgentType   type;
    AgentStatus status;
    uint32_t    priority;
    void       *context;        /* agentə xas data        */
} Agent;

/* ── Mesaj strukturu (agentlər arası) ─────────────────── */
typedef struct {
    uint32_t    sender_id;
    uint32_t    receiver_id;
    uint32_t    msg_type;
    uint32_t    payload_size;
    uint8_t     payload[1024];
} AgentMessage;

/* ── Nəticə kodları ───────────────────────────────────── */
#define RESULT_OK           0
#define RESULT_ERROR       -1
#define RESULT_NO_MEMORY   -2
#define RESULT_INVALID     -3

/* ── Yardımçı makrolar ────────────────────────────────── */
#define LOG_INFO(fmt, ...)   printf("[INFO]  " fmt "\n", ##__VA_ARGS__)
#define LOG_WARN(fmt, ...)   printf("[WARN]  " fmt "\n", ##__VA_ARGS__)
#define LOG_ERROR(fmt, ...)  printf("[ERROR] " fmt "\n", ##__VA_ARGS__)

#endif /* COMMON_H */
