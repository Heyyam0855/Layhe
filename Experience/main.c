/**
 * main.c — Experience Agent System — Əsas giriş nöqtəsi
 *
 * Bu proqram Çəkirdək (Kernel), Mikro Kod (Microcode),
 * Xüsusi Agent və Claude Sonnet 4.6 Agent modullarını
 * birləşdirib işə salır.
 *
 * Dil: C
 * Tarix: 2026
 */

#include "include/common.h"
#include "kernel/core.h"
#include "kernel/scheduler.h"
#include "kernel/memory.h"
#include "microcode/microcode.h"
#include "microcode/instruction_set.h"
#include "agents/xususi_agent/xususi_agent.h"
#include "agents/claude_sonnet/claude_agent.h"

/* ═══════════════════════════════════════════════════════════
 *  Əsas proqram
 * ═══════════════════════════════════════════════════════════ */
int main(void)
{
    printf("╔═══════════════════════════════════════════════════╗\n");
    printf("║       Experience Agent System v%s           ║\n", PROJECT_VERSION);
    printf("║   Çəkirdək + Mikro Kod + Agent Arxitekturası     ║\n");
    printf("╚═══════════════════════════════════════════════════╝\n\n");

    /* ── 1. Çəkirdəyi başlat ─────────────────────────────── */
    Kernel kernel;
    kernel_init(&kernel);

    /* ── 2. Planlaşdırıcı ────────────────────────────────── */
    Scheduler scheduler;
    scheduler_init(&scheduler, SCHED_PRIORITY);

    /* ── 3. Yaddaş havuzu ────────────────────────────────── */
    MemoryPool *mem = (MemoryPool *)malloc(sizeof(MemoryPool));
    if (!mem) {
        LOG_ERROR("Yaddaş ayırmaq mümkün olmadı!");
        return 1;
    }
    memory_init(mem);

    /* ── 4. Xüsusi Agent yaratmaq ────────────────────────── */
    XususiAgent xususi;
    xususi_agent_init(&xususi, "Analitik-1");

    XususiRule rule1 = {
        .type            = RULE_IF_GREATER,
        .condition_value = 50,
        .action_id       = 1,
        .description     = "Dəyər 50-dən böyükdürsə xəbərdar et",
        .enabled         = true
    };
    xususi_agent_add_rule(&xususi, &rule1);

    XususiRule rule2 = {
        .type            = RULE_ALWAYS,
        .condition_value = 0,
        .action_id       = 2,
        .description     = "Həmişə log yaz",
        .enabled         = true
    };
    xususi_agent_add_rule(&xususi, &rule2);

    /* Çəkirdəyə qeydiyyat */
    kernel_register_agent(&kernel, &xususi.base);

    /* ── 5. Claude Sonnet 4.6 Agent yaratmaq ─────────────── */
    ClaudeAgent claude;
    claude_agent_init(&claude, "Claude-Analitik");

    ClaudeParams params = {
        .temperature = 0.5f,
        .top_p       = 0.85f,
        .max_tokens  = 2048,
        .streaming   = false
    };
    claude_agent_configure(&claude, &params);
    claude_agent_set_system_prompt(&claude,
        "Sən təhlil və kod yaratma üzrə ixtisaslaşmış "
        "Claude Sonnet 4.6 agentisən.");

    /* Claude agentinə tapşırıqlar göndər */
    claude_agent_submit_task(&claude, CLAUDE_TASK_CODE_GENERATION,
        "Fibonacci ardıcıllığını hesablayan C funksiyası yaz");

    claude_agent_submit_task(&claude, CLAUDE_TASK_ANALYSIS,
        "Agent sisteminin performansını təhlil et");

    claude_agent_submit_task(&claude, CLAUDE_TASK_REASONING,
        "Mikro kod arxitekturasının üstünlükləri nədir?");

    /* Çəkirdəyə qeydiyyat */
    kernel_register_agent(&kernel, &claude.base);

    /* ── 6. Çəkirdəyi işə sal ────────────────────────────── */
    kernel_start(&kernel);

    /* Bir neçə tick icra et */
    for (int i = 0; i < 10; i++) {
        kernel_tick(&kernel);

        /* Planlaşdırıcı növbəti agenti seçir */
        Agent *next = scheduler_next(&scheduler, &kernel);
        if (next) {
            LOG_INFO("Planlaşdırıcı seçdi: \"%s\"", next->name);
        }
    }

    /* ── 7. Agentləri icra et ─────────────────────────────── */
    printf("\n--- Xüsusi Agent icra olunur ---\n");
    xususi_agent_evaluate(&xususi, 75);
    xususi_agent_execute(&xususi);

    printf("\n--- Claude Sonnet 4.6 Agent icra olunur ---\n");
    claude_agent_process(&claude);

    /* Nəticəni al */
    char result[CLAUDE_MAX_TOKENS];
    for (uint32_t i = 0; i < claude.task_count; i++) {
        if (claude_agent_get_result(&claude, i, result, sizeof(result)) == RESULT_OK) {
            printf("  Tapşırıq %u nəticəsi: %s\n", i, result);
        }
    }

    /* ── 8. Mikro kod proqramı ────────────────────────────── */
    printf("\n--- Mikro Kod Proqramı ---\n");

    Instruction high_level[] = {
        { INSTR_CREATE_AGENT,  1, 0, "agent_yarat"  },
        { INSTR_CREATE_AGENT,  2, 0, "agent_yarat2" },
        { INSTR_SEND_MESSAGE,  1, 2, "mesaj"        },
        { INSTR_PROCESS_TASK,  1, 0, "icra"         },
        { INSTR_PROCESS_TASK,  2, 0, "icra2"        },
        { INSTR_EVALUATE,      1, 2, "qiymet"       },
        { INSTR_REPORT,        1, 0, "hesabat"      },
    };

    MicrocodeProgram mc_prog;
    instruction_compile(high_level, 7, &mc_prog);
    microcode_run(&mc_prog);
    microcode_dump(&mc_prog);

    /* ── 9. Status hesabatları ────────────────────────────── */
    kernel_log_status(&kernel);
    xususi_agent_status(&xususi);
    claude_agent_status(&claude);
    memory_dump_stats(mem);

    /* ── 10. Təmizləmə ───────────────────────────────────── */
    kernel_stop(&kernel);
    free(mem);

    printf("╔═══════════════════════════════════════════════════╗\n");
    printf("║          Proqram uğurla tamamlandı!              ║\n");
    printf("╚═══════════════════════════════════════════════════╝\n");

    return 0;
}
