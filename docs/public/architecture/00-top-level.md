# OriGen Architecture — Top-Level Overview

## Purpose of This Document

This document defines the *conceptual foundation* of OriGen:

* What the system *is* and *is not*
* Core architectural philosophy
* The high-level model that drives all design decisions
* The separation of planning vs execution
* Why determinism is a first-class constraint
* The metaphors that guide OriGen’s mental model
* Architectural invariants that should not drift

This is the root of the architecture series and should remain mostly stable after finalization.

---

## 1. What OriGen Is

OriGen is a **deterministic publishing compiler**.

OriGen does not execute tools directly. It:

* loads Maps
* loads Navigators
* resolves dependencies
* normalizes the workflow
* selects Backpacks
* validates structure
* produces a deterministic Route (IR)
* Guide translates Route into native platform formats

Execution is delegated to interchangeable backend drivers.

In summary:

> **OriGen decides *what should happen*, not *how it runs*.**

This keeps the system platform-agnostic, reproducible, and maintainable.

---

## 2. The Compass, Maps, Navigators, Backpacks, Routes, Guides

OriGen uses a consistent metaphor to describe its components.

### Compass (Core Planner)

* Loads Maps
* Loads Navigators
* Resolves Backpacks
* Compiles everything into a Route
The Compass is the heart of OriGen’s planning model.

### Maps (Declarative Workflows)

YAML workflows describing *intent*, not logic:

* steps
* tools
* modes
* inputs/outputs
* order of execution

Maps contain **no imperative code**.

### Navigators (Tool Definitions)

Navigator files define:

* tool containers (by OCI digest, not tag)
* entrypoints
* argument templates
* modes
* backpack requirements

They isolate tooling changes from workflows.

### Backpacks

Backpacks are immutable, versioned, read-only resource bundles carried into execution.

* typesetting engines (LaTeX, typst, HTML→PDF engines, etc.)
* ICC profiles
* font packs
* metadata processors
* templates
* validators
* any future deterministic resource

### Routes

Intermediate Representation (IR): the deterministic, platform-neutral execution graph OriGen compiles from a Map.
A Route defines *how* a workflow should run, independent of any backend system.

### Guides

Translates a Route into native backend execution formats (e.g., GitHub Actions, GitLab CI, Argo, Kubernetes, or local scripts).
Guides perform *translation only* — OriGen does not run workflows.

---

## 3. Why This Architecture Exists
@todo rewrite: domain agnostic now

Modern publishing pipelines are diverse and fragmented:

* Typographic engines (*TeX*, *typst*, *weasyprint*, *princeXML*, etc.)
* Document converters (*Pandoc*, *markdown tooling*, *DocBook*, etc.)
* PDF processors
* Validators (PDF/A, metadata, accessibility)
* Font sets
* Metadata injectors
* Layout preprocessors
* Multiple OS environments
* Multiple container engines

Different teams adopt different tools; tools evolve independently; defaults drift over time.

The result:
**identical sources often fail to produce identical outputs.**

Knuth created TeX so that *the same input produces the same output humanly*.
OriGen generalizes this principle to **entire pipelines**, regardless of what toolchain users choose.

OriGen is explicitly **not tied to LaTeX or any single technology**.
It aims to provide deterministic publishing using:

* LaTeX **or** typst **or** other engines
* markdown-based flows
* pure-PDF workflows
* HTML-to-print pipelines
* anything users declare via Maps + Navigators

OriGen is about **workflow determinism**, not toolchain preference.

---

## 4. Planning vs Execution (Foundational Separation)

OriGen performs planning.
Backend drivers perform execution.

OriGen does not:

* run containers
* manage schedulers
* handle resource allocation
* replace CI/CD systems
* embed a runtime for tools

Instead:

* OriGen outputs a deterministic IR
* A backend driver interprets that IR and performs execution
* Local development and one-click desktop modes use built-in backend drivers
* CI/CD, serverless, and enterprise environments implement their own backend drivers externally

Backend drivers are **peers**, not a hierarchy.

---

## 5. Execution Flow (High-Level)

OriGen produces a deterministic **IR**.
Execution is delegated to a backend driver chosen by the user or environment.

All backend drivers are **peers**.
No backend derives from any other.

> **About the Route.**
> The Route is a structured, machine-readable execution plan describing steps, dependencies, required tools, and deterministic parameters. It is versioned, schema-validated, and serializable. The IR does not encode execution strategy — only intent and structure — ensuring stability across platforms and backends.

```
         Compass
(Maps + Navigators → Route)
             │
             ▼
         Route (IR)
             │
             ▼
 ┌────────────────────────────────────────────────────────────┐
 │                  Guides(Backend Adapters)                  │
 │    (Each driver consumes IR and performs real execution)   │
 └───────┬──────────┬──────────────┬────────┬────────────┬────┘
         │          │              │        │            │
         ▼          ▼              ▼        ▼            ▼
  Local Container   Local VM     CI/CD    Serverless   Enterprise
      Driver        Driver      Driver      Driver       Driver
(development mode) (one-click)
```

### Key points

* **The IR is universal** across all execution environments.
* Backend drivers are interchangeable adapters that accept IR.
* Local container and VM drivers are included for development and desktop use; all others are external.
* OriGen stays independent of container engines, orchestration systems, and toolchains.

This architecture ensures OriGen is reproducible, portable, and flexible.

---

## 6. Backend Landscape

OriGen ships with built-in backend drivers for:

### Local Container Backend (Developer Mode)

Uses whatever OCI-compatible container engine the host provides.

### Local Runtime VM Backend (One-Click Mode)

A sealed VM appliance containing a minimal container engine and backpacks.

### External Backend Drivers

Implemented by CI/CD systems, enterprises, or cloud environments:

* CI/CD
* serverless execution
* hardened enterprise runtimes
* future custom backends

These exist *outside* OriGen Core and consume IR directly.

---

## 7. Determinism

Determinism is a first-class architectural constraint.

Determinism applies to both successful execution and failure states: identical inputs must produce identical outputs *and* identical errors, enabling reproducible debugging and CI behavior.

OriGen enforces:

* identical outputs for identical inputs
* identical failure states for identical inputs
* immutable sidecars
* pinned tool containers (OCI digests)
* controlled mount and directory structure
* stable IR schema
* execution isolation from the host system

If a design conflicts with determinism, the design is rejected.

---

## 8. Non-Goals

OriGen does not attempt to:

* be a container engine
* serve as an orchestrator
* replace CI/CD systems
* mandate a publishing toolchain
* enforce LaTeX-only workflows
* become a monolithic “all-in-one” tool

OriGen focuses on:

* planning
* determinism
* stability
* clarity
* portability
* reproducibility

Execution is always delegated.

---

## 9. Stability and Invariants

This document and **01-contracts.md** define architectural principles that must remain stable:

* planning/execution separation
* backend-agnostic
* toolchain neutrality
* immutability of sidecars
* determinism as a contract
* IR as the canonical output of planning

Future components must conform to these invariants.

---

## 10. Reading Order

Continue with:

* **01-contracts.md** — foundational invariants and system guarantees
* **02-execution-model.md** — the system lifecycle
* **03-ir-specification.md** — the core data structure

…and proceed numerically.
