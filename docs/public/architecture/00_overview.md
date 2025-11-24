# OriGen Architecture — High-Level Overview

## 1. Purpose of This Document

This document defines the *core conceptual architecture* of OriGen. It establishes the mental model, system boundaries, and structural invariants that guide every other part of the specification. The goal is to provide a stable, enduring foundation against which the rest of the system can evolve.

A core architectural premise underpins everything in this document:

> **You cannot reason about a workflow robustly until you can describe it fully, deterministically, and independent of runtime.**



OriGen’s top-level architecture explains:

- What OriGen is — a deterministic workflow compiler
- What OriGen is not — an executor, orchestrator, or environment manager
- The layers of the planning model
- How workflows become typed IR
- How backend-native files are produced
- The separation between planning and execution
- The role of Papyrus dialects in defining workflow meaning
- The principles that guarantee stability and reproducibility

A core architectural premise underpins everything that follows:

> **You cannot reason about a workflow until you can describe it fully, deterministically, and independent of runtime.**



---

## 2. What OriGen Is

OriGen is a **deterministic workflow planning engine**. It transforms declarative workflow intent into a fully‑typed, backend‑agnostic representation called the **Route**. A separate translation step then converts the Route into backend‑native configuration.

OriGen’s core responsibilities are:

- Accepting workflow intent as a **Map**
- Applying toolchain semantics via **Navigators**
- Incorporating immutable planning-time resources via **Backpacks**
- Allowing Maps to declare intended **Cargo** flow shape (which Steps emit or consume runtime artifacts) at the semantic level permitted by their Papyrus dialect
- Validating workflow meaning through **Papyrus dialects**
- Producing a **typed IR Route** with complete semantics
- Passing the Route to a **Guide**, which uses vendor **Dictionaries** to generate backend‑native files

OriGen does **not**:

- Track, hash, or predict runtime Cargo contents or state
- Model execution-time dataflow beyond intent-level Cargo flow
- Execute workflows
- Provision infrastructure
- Fetch remote toolchains
- Inspect runtime environments
- Manage containers, machines, or CI agents

OriGen is a *compiler*, not a runtime.

---

## 3. Architecture at a Glance

OriGen architecture consists of eight conceptual layers:

1. **Map** — Declarative workflow intent
2. **Navigator** — Toolchain behavior and Step realization rules
3. **Backpack** — Immutable planning-time inputs
4. **Papyrus Dialect** — Typed semantics for a workflow class
5. **Compass** — Pure deterministic planner
6. **Route** — Typed IR capturing the complete workflow logic
7. **Dictionary** — Backend‑native vocabulary
8. **Guide** — IR → backend‑native translation using Dictionaries

Each layer has a single responsibility and clear boundaries.

---

## 4. The Planning Model

### 4.1 Map — Workflow Intent

A Map expresses *what* a workflow should do, not *how* to execute it. It provides:

- Steps
- Dependencies
- Arguments
- Backpack references
- Optional vendor Extensions

Maps are intentionally simple and backend‑neutral.

Maps may also declare the *shape of Cargo flow* — which Steps are expected to emit or consume runtime artifacts — but only at the level permitted by their Papyrus dialect. Maps describe **intended data flow**, not the concrete form or contents of runtime Cargo.

---

### 4.2 Navigator — Toolchain Semantics

Navigators define *how* each Step in a Map is realized using a particular toolchain. They:

- Provide execution templates
- Define required Backpacks
- Map Steps into Papyrus Step semantics

They do not modify core Papyrus semantics.

---

### 4.3 Backpack — Immutable Inputs

Backpacks provide read‑only resources used during planning. Their immutability ensures:

- reproducibility
- provenance
- determinism

Backpacks are part of planning‑time semantics, not runtime Cargo.

---

### 4.4 Papyrus — Workflow‑Class Semantics

Papyrus dialects define what workflow Steps *mean*. A dialect specifies:

- Step types and constraints
- Retry semantics
- Isolation rules
- Cargo behavior
- Workspace rules
- Determinism constraints

Maps are always written against a specific Papyrus dialect.

Papyrus evolution is conservative, versioned, and governed through RFCs.

---

### 4.5 Compass — Pure Planning

Compass performs deterministic planning with **no execution**. It:

- Validates the Map against its Papyrus dialect
- Resolves Navigators and Backpacks
- Applies all semantics defined by Papyrus
- Produces a fully typed IR Route

Compass does not:

- run commands
- inspect the host environment
- fetch external tools
- interact with backends

It is a pure function: `Map → Route`.

---

### 4.6 Route — Typed IR

The Route is the complete, deterministic representation of the workflow. It includes:

- typed Step semantics
- dependencies
- Backpack and Navigator pins
- preserved Extensions

The Route contains **no backend‑native fields** and makes no assumptions about runtime.

---

### 4.7 Dictionary — Backend Vocabulary

Dictionaries define backend-native constructs and how Papyrus semantics map onto them. They are:

- vendor-authored
- independently versioned
- validated against Papyrus compatibility constraints

Dictionaries allow backends to expose features without mutating Papyrus.

---

### 4.8 Guide — IR Translation

The Guide transforms a Route into backend-native files using Dictionaries. The Guide is not part of the semantic lineage; it performs translation only and introduces no new meaning. The Guide:

- interprets IR
- applies backend vocabularies
- emits files that backends can execute

The Guide does not execute anything.

---

## 5. Planning vs Execution

OriGen’s architecture draws a strict boundary between planning and execution.

### Planning (OriGen)

- Reading Maps
- Validating semantics
- Resolving Navigators/Backpacks
- Producing IR
- Translating IR via Guide

### Execution (Backend)

- Fetching artifacts
- Running commands
- Scheduling jobs
- Allocating compute
- Managing secrets and environments

This boundary is essential for reproducibility. OriGen never interacts with remote systems during planning; all external behavior belongs to the backend.

---

## 6. Determinism

Determinism applies to the **planning phase only**. Given the same:

- Map
- Navigators
- Backpacks
- Papyrus dialect
- Dictionary versions

OriGen will always produce the same Route and the same backend-native files.

Determinism does **not** apply to runtime execution.

(Determinism reflects the exact set of Dictionary versions supplied at planning time.)

---

## 7. Emergent Properties

OriGen’s strict planning boundary and semantic model enable several emergent behaviors:

### 7.1 Automatic Digital Provenance (ADP)

A complete provenance graph can be reconstructed from Routes, Backpacks, Navigators, and Maps.

### 7.2 Downsweep

The ability to resolve partial dependencies back to required inputs, independent of backend.

These are outcomes of the architecture, not formal invariants.

---

## 8. Extensions

Extensions allow vendors to add optional, namespaced metadata without altering Papyrus. They:

- are safe to ignore
- evolve independently
- may be promoted to Papyrus
- must never mutate core semantics

Extensions preserve backend-neutrality while enabling rapid innovation.

---

## 9. Invariants

The following properties define OriGen’s architectural stability:

- Maps express intent, not execution
- Navigators do not introduce new semantics
- Backpacks are immutable
- Papyrus defines all workflow-class meaning
- Compass is pure
- Routes contain no backend fields
- Dictionaries define backend behavior, not Guides
- Guides never execute workflows
- Execution Boundary is strict
- Extensions are non-mutating and namespaced

These invariants anchor the rest of the specification.

If any proposed change conflicts with determinism, the change is rejected. Determinism is the boundary that cannot be crossed.

---

