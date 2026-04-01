# Experience — Agent Layihəsi

## Layihə Təsviri
Bu layihə **Xüsusi Agentlər** və **Claude Sonnet 4.6 Agentləri** üçün
çəkirdək kodu (kernel) və mikro kod (microcode) əsaslı arxitekturadır.

Proqramlaşdırma dili: **C**

## Qovluq Strukturu

```
Experience/
├── kernel/              # Çəkirdək kodu (Kernel)
│   ├── core.c
│   ├── core.h
│   ├── scheduler.c
│   ├── scheduler.h
│   ├── memory.c
│   └── memory.h
├── microcode/           # Mikro kod
│   ├── microcode.c
│   ├── microcode.h
│   ├── instruction_set.c
│   └── instruction_set.h
├── agents/
│   ├── xususi_agent/    # Xüsusi Agent modulu
│   │   ├── xususi_agent.c
│   │   └── xususi_agent.h
│   └── claude_sonnet/   # Claude Sonnet 4.6 Agent modulu
│       ├── claude_agent.c
│       └── claude_agent.h
├── include/             # Ümumi başlıq faylları
│   └── common.h
├── main.c               # Əsas giriş nöqtəsi
├── Makefile
└── README.md
```

## Qurma (Build)
```bash
make          # Layihəni qur
make clean    # Təmizlə
make run      # Qur və işə sal
```

## Lisenzia
Bütün hüquqlar qorunur © 2026
