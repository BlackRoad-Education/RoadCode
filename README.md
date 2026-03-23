# RoadCode

> Canonical RoadCode workspace and automation hub for BlackRoad-Education.

Part of the [BlackRoad OS](https://blackroad.io) ecosystem — [BlackRoad-Education](https://github.com/BlackRoad-Education)

---

# BlackRoad-Education — RoadCode

> Learning & Tutoring division of [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc)

RoadWork tutoring platform, adaptive learning, FSRS spaced repetition, and code challenges. Free for K-12. All learning data stays on your device, your data, your agents.

## Products

| Product | What It Does |
|---------|-------------|
| **RoadWork** | Adaptive tutoring platform — math, science, reading, coding |
| **Code Challenge** | Interactive programming exercises with local AI grading |
| **FSRS Engine** | Spaced repetition scheduler (Free Spaced Repetition Scheduler) |
| **Adaptive Learning** | Adjusts difficulty in real-time based on student performance |

## Org Hierarchy

```
BlackRoad-OS-Inc (Parent — 254 repos, 67 agents, 7 nodes)
  └── BlackRoad-Education (Learning & Tutoring)
      ├── RoadCode          ← this repo (workspace + automation)
      ├── roadwork           ← RoadWork tutoring platform
      ├── code-challenge     ← interactive coding exercises
      └── operator           ← CLI tools + deployment
```

## Repos in This Org

- [`RoadCode`](https://github.com/BlackRoad-Education/RoadCode) — Workspace hub (this repo)
- [`roadwork`](https://github.com/BlackRoad-Education/roadwork) — RoadWork tutoring platform
- [`code-challenge`](https://github.com/BlackRoad-Education/code-challenge) — Programming exercises + grader
- [`operator`](https://github.com/BlackRoad-Education/operator) — CLI + automation scripts

## How It Works

1. **Student opens RoadWork** — picks a subject (math, science, reading, coding)
2. **FSRS schedules reviews** — spaced repetition ensures long-term retention
3. **Adaptive engine adjusts** — too easy? harder problems. Struggling? more scaffolding.
4. **Local AI grading** — Ollama models on the device grade written responses
5. **No data leaves the device** — progress stored locally, syncs only if student opts in

## How It Connects

- **Parent**: [BlackRoad-OS-Inc](https://github.com/BlackRoad-OS-Inc) — central coordination
- **AI**: [BlackRoad-AI](https://github.com/BlackRoad-AI) — Lucidia models power tutoring explanations
- **Foundation**: [BlackRoad-Foundation](https://github.com/BlackRoad-Foundation) — Amundson Framework math research
- **Gov**: [BlackRoad-Gov](https://github.com/BlackRoad-Gov) — civic literacy content

## Pricing

Free for K-12 students. Always.

## License

Proprietary — BlackRoad OS, Inc. See [LICENSE](./LICENSE).

---

*Remember the Road. Pave Tomorrow.*
