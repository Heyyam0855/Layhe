# ═══════════════════════════════════════════════════════════
#  Makefile — Experience Agent System
#  Çəkirdək + Mikro Kod + Agent Arxitekturası
#  Dil: C
# ═══════════════════════════════════════════════════════════

CC       = gcc
CFLAGS   = -Wall -Wextra -std=c11 -Iinclude
LDFLAGS  =
TARGET   = experience

# ── Mənbə faylları ────────────────────────────────────────
SRCS = main.c \
       kernel/core.c \
       kernel/scheduler.c \
       kernel/memory.c \
       microcode/microcode.c \
       microcode/instruction_set.c \
       agents/xususi_agent/xususi_agent.c \
       agents/claude_sonnet/claude_agent.c

OBJS = $(SRCS:.c=.o)

# ── Əsas hədəflər ─────────────────────────────────────────
all: $(TARGET)
	@echo "=== Qurma tamamlandı: $(TARGET) ==="

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

# ── Təmizləmə ─────────────────────────────────────────────
clean:
	rm -f $(OBJS) $(TARGET)
	@echo "=== Təmizləndi ==="

# ── Qur və işə sal ────────────────────────────────────────
run: all
	@echo ""
	@echo "=== İcra başlayır ==="
	@echo ""
	./$(TARGET)

# ── Yenidən qur ───────────────────────────────────────────
rebuild: clean all

.PHONY: all clean run rebuild
