<p align="center">
  <img src="docs/public/images/origen-logo.jpg" width="120" alt="OriGen Logo">
</p>

# 📘 OriGen — A Deterministic Workflow Compiler

*(Maps → Route → Backend-native artifacts)*

> **OriGen treats workflows the way compilers treat code:**
> declarative input → deterministic IR → translation-only backends.


OriGen does **not** run workflows.
It compiles declarative **Maps** into a backend-neutral **Route** (IR), and **Guides** translate that IR into native execution artifacts for:

* Kubernetes
* CI/CD systems
* container engines
* VM/embedded runtimes
* or any custom backend

Execution happens entirely outside OriGen.

OriGen provides the **planning layer** modern automation has been missing.

---

## 🌎 What OriGen Is (in one sentence)

OriGen is a deterministic workflow compiler that transforms declarative Maps into backend-agnostic, reproducible execution plans.

---

## 🧭 Core Concepts


- **Map** — Declarative workflow intent: steps, tools, modes, I/O, dependencies.
- **Navigator** — Digest-pinned toolchain definition: image, entrypoints, modes.
- **Backpack** — Immutable resource bundle (fonts, configs, datasets, templates).
- **Route (IR)** — Deterministic, backend-neutral execution graph.
- **Guide** — Translator: Route → native backend artifacts (K8s, CI, VM, scripts).
- **Step** — Unit of execution.
- **Cargo** — Outputs produced by Steps.
- **Execution Boundary** — Where OriGen stops and external systems take over.

This vocabulary prevents domain contamination and creates a stable grammar for workflows across DevOps, data, publishing, ML, scientific work, and more.


---

## 🧱 The OriGen Architecture (Top-Level Overview)

OriGen performs **planning**, not execution:

1. Loads Maps
2. Loads Navigators
3. Resolves Backpacks
4. Validates workflow structure
5. Produces a deterministic Route
6. A Guide translates the Route into backend-native artifacts

Execution is delegated to:

* Kubernetes
* CI/CD
* local container engines
* enterprise backends
* embedded or VM environments

OriGen stays **platform-agnostic** and **toolchain-neutral**.

---

## 🧭 Minimal Mental Model

Workflow intent → deterministic IR → backend outputs.

![](https://origen-hub.github.io/origen-core-public/images/origen-flow.png)

OriGen stops before execution.
Everything that runs, runs elsewhere.

---

## 🔐 Zero-Trust by Design

Zero-trust doesn’t require enforcement here — it emerges from structure:

* explicit, pinned toolchains
* immutable inputs
* pure, environment-free planning
* backend-neutral IR
* strict execution boundary

Nothing is implicit enough to require verification.

OriGen removes the conditions that normally make zero-trust expensive.

---

## The Maintenance Paradox

Pinning everything normally creates maintenance hell.

In OriGen, it does the opposite.

Because every build, digest, and commit is explicit and traceable, the system naturally forms a provenance graph.
This is not an add-on or an integration.

It emerges.

This leads directly to:

---

## 🧬 Automatic Digital Provenance (ADP)

ADP emerges from:

* digest-pinned Navigators & Backpacks
* manifest commits
* deterministic planning
* immutable IR

Provenance becomes:

* complete
* reconstructable
* audit-ready
* derived mechanically from Git

No scanners or instrumentation required.

---

## 🌪️ Downsweep (Org-wide Reverse Dependency Discovery)

Given a vulnerable digest:

1. identify its manifest commit
2. find all Maps referencing that commit
3. enumerate all dependent workflows
4. generate automated PRs
5. produce impact & remediation reports

Downsweep turns supply-chain security into a **mechanical process**.

---

## 🧩 What OriGen Is *Not*

OriGen is not:

* an orchestrator
* a CI/CD runner
* a templating engine
* a workflow wrapper
* a platform-specific DSL
* a runtime or scheduler

OriGen is the **planner** above all of those.

---

## 🧠 Why This Layer Matters

Modern workflows drift because:

* toolchains mutate
* CI YAML diverges
* glue scripts sprawl
* environments leak state
* workflow intent is scattered

OriGen provides:

* deterministic structure
* frozen toolchains
* portable workflow intent
* reproducible failures
* reviewable IR
* backend neutrality

You cannot reason about a workflow until you can describe it deterministically and independent of runtime.


---

## 🚀 Getting Started

Published [documentation](https://origen-hub.github.io/origen-core-public/pages/vocabulary/). Start with:

* **Primer**
* **Value Statement**
* **Top-Level Architecture**
* **Zero-Trust by Design**
* **Automatic Digital Provenance (ADP)**

These form the stable conceptual foundation.

---

## 📌 Project Status

Early stage, architecture-first.

The public docs are stable; implementation is being built carefully to preserve invariants.


---

## 🤝 Contributing

For now:

* open issues
* propose doc improvements
* discuss architectural topics
* review Zero-Trust / ADP / Downsweep ideas

Implementation contributions will open once IR & schemas are finalized.

---

## 📜 License

Apache 2.0 unless noted otherwise.
