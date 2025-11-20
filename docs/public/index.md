# Welcome to OriGen

This page is a short orientation guide — the **Alohas, Holas, and Hello Worlds of OriGen**.
It introduces a small set of terms that help you roam the docs comfortably.
Think of it as a legend for the map.

OriGen uses a light navigation metaphor — **Maps** define intent, **Routes** describe the path, **Navigators** provide the tools, and **Backpacks** carry the supplies.
This framing helps the terminology feel intuitive before you encounter it in context.

These snippets of **OriGen Speak** appear throughout the documentation and make the Primer, Value Statement, and Architecture easier to follow.

---

## Core Concepts

**Map** — A declarative definition of workflow intent (your source of truth).

**Navigator** — A tool or action used within Steps (executables, compilers, transformers).
Navigators describe *how* individual Steps operate.

**Backpack** — Immutable Resource Bundle: a versioned, read-only bundle of supporting assets carried into execution.
Backpacks contain static, immutable materials such as datasets, configuration files, templates, or fonts.
They are **defined ahead of time**, **never mutated**, and **not produced** by any Step.

**Route** — Intermediate Representation (IR): the deterministic, platform-neutral execution graph OriGen compiles from a Map.
A Route defines *how* a workflow should run, independent of any backend system.

**Guide** — Backend Adapter: Translates a Route into native backend execution formats
(e.g., GitHub Actions, GitLab CI, Argo, Kubernetes, or local scripts).
Guides perform *translation only* — OriGen does not run workflows.

**Step** — A smallest unit of execution in a workflow.

**Cargo** — Outputs produced by Steps: files, directories, images, binaries, datasets, or other generated results.
Cargo is **created during execution**, **mutable**, and often consumed by later Steps.

**Topology**  — The structure of workflow dependencies (DAG, fan-in, fan-out).

**Execution Boundary** — The boundary at which a Route, transformed by a Guide into backend-native form, leaves OriGen and is executed by the target platform.

---

## You Are Good to Go

With these foundational concepts in mind, you’re ready for the deeper sections.
The paths in-front of you are:

* **[Primer][origen-executive-overview]** - for the big idea
* **[Value Statement][origen-value-statement]** - for philosophical reason
* **[Top-Level Architecture][origen-architecture-top-level-overview]** — for a peek under the hood
* **[MVP][origen-minimum-viable-product]** — for roadmap

---

## Project Status

> Early stage, but conceptually solid.

Upfront clarity, downstream simplicity is OriGen’s official motto.
We front-load the architecture intentionally so the implementation can proceed without churn.

 ---

## (Optional) CLI Usage Preview

**This section is optional, but many readers find that a quick glance at real CLI commands helps anchor the terminology in practical use.**

```
origen survey
```

Discover Maps in the current repository.

```
origen topo route
```

Visualize the topology (DAG) of a compiled Route.

```
origen pathfinder
```

Analyze dependencies and determine execution order.

```
origen bearing
```

Explain what happens next or what’s blocking progress.

```
origen backpack inspect
```

Inspect the immutable supplies bundled in a Backpack.
