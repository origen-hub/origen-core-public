# Papyrus — Semantic Substrate for Workflows

*Assumes familiarity with the OriGen planning stack (Map → Navigator → Backpack → Papyrus → Compass → Route → Guide). Refer to the Architecture Overview for the full model.*

## 1. Why Papyrus Exists

Modern execution platforms (Kubernetes, CI systems, VM runners, HPC schedulers, dataflow engines, etc.) all expose their own concepts of:

- **what a "step" is**
- **how workspaces behave**
- **how artifacts move between steps**
- **what failure and retry mean**
- **how resources and isolation work**

Without a shared model, every workflow description ends up entangled with the details of a specific backend. Portability, analysis, and cross-platform tooling become fragile or impossible.

**Papyrus is the layer that fixes this.**

Papyrus defines **typed semantic classes of execution environments** – for example:

- `container/v1` – container-oriented workflows
- `vm/v1` – VM/runner style workflows
- `hpc/v1` – batch/HPC workflows
- `dataflow/v1` – DAG/dataflow engines

Each Papyrus dialect describes *how the world works* in that class of environment. Maps, Navigators, Routes, and Guides are all written *against* a Papyrus dialect.

OriGen uses Papyrus to:

- keep workflow semantics **explicit and analyzable**
- keep IR **portable** across backends in the same class
- keep Guides **honest** about what they can and cannot express
- keep determinism and zero-trust **grounded in structure**, not convention

Papyrus is not optional sugar – it is the **semantic substrate** for everything OriGen does.

---

## 2. Papyrus in the Navigation Metaphor

*For clarity: in the navigation metaphor, Papyrus should be understood strictly as the **semantic substrate**—the rules of the world—not anything related to movement, traversal, or route‑finding. Those behaviors belong exclusively to Maps and Routes. Papyrus defines the environment, not the journey.*

OriGen’s navigation metaphor provides a shared mental model for the entire planning stack. In this metaphor, **Papyrus represents the semantic world in which workflow plans are written**—the rules, constraints, and behaviors that Maps, Navigators, Routes, and Guides must respect.

Papyrus does *not* correspond to movement or pathfinding (those belong to Maps and Routes). Instead, Papyrus describes the **environmental semantics** that make planning possible:

- what kinds of steps exist in that world
- how workspaces and artifacts behave
- how steps may be connected
- how failure, retry, and completion are interpreted

Maps are always authored *within* a Papyrus world. Navigators and Guides operate *according to* that world. The Compass relies on Papyrus rules to validate and produce a correct Route.

With Papyrus, a Map is no longer an abstract sketch; it becomes a plan grounded in a well-defined semantic environment.

---

## 3. What Papyrus Is (and Is Not)

*Papyrus defines **semantics**, not **syntax**. Its role is to describe the meaning and behavioral rules of workflow structures. The **Map Language** is the DSL that expresses intent using Papyrus-defined semantics. Papyrus says **what** concepts mean; the Map Language defines **how** authors write them.*

### 3.1 Papyrus is

- **A typed semantic model** for an execution-class of workflows
- **A contract** between:
  - Map authors
  - Navigator authors
  - Guide / backend implementers
  - OriGen’s Compass and IR
- **A stable language of guarantees**:
  - how steps behave
  - how state flows
  - what failure means
  - what isolation means

### 3.2 Papyrus is not

- **Not a backend product spec.**
  - Papyrus describes *classes* of systems, not individual platforms.
- **Not a user-editable schema.**
  - Users cannot invent local Papyrus dialects; Papyrus changes only via OriGen RFCs.
- **Not a Map or workflow DSL.**
  - Papyrus defines *semantics*; Maps define *intent*.
- **Not an execution engine.**
  - Papyrus never runs anything. It only constrains how plans and IR must look.

Papyrus lives in the same conceptual space as:

- an ISA for a CPU family (what instructions mean)
- a type system for a language (what values mean)
- an ABI for a platform (how components agree to interact)

---

## 4. Papyrus Dialects

A **Papyrus dialect** is a concrete, versioned semantic model for a particular class of environments.

Examples (illustrative, not exhaustive):

- `container/v1`

  - Steps run as containers.
  - Workspaces are volumes or filesystem mounts.
  - Cargo is typically files, images, or blobs.
  - Isolation is process + container boundaries.

- `vm/v1`

  - Steps run on long-lived machines or ephemeral runners.
  - Workspaces may be home directories or attached volumes.
  - Cargo can be files, artifacts, or images passed between machines.

- `hpc/v1`

  - Steps are scheduled jobs.
  - Workspaces are shared filesystems.
  - Queueing, limits, and reservation semantics are explicit.

- `dataflow/v1`

  - Steps are nodes in a DAG/dataflow.
  - Cargo is strongly typed datasets.

Within a dialect, Papyrus defines:

*(Execution strategy is listed here only as a **semantic constraint**, not as a scheduler directive. Papyrus does not dictate how execution is scheduled; it only specifies which scheduling behaviors a dialect must be able to represent.)*

- Step kinds and their fields
- Workspace and artifact semantics
- Allowed edge types between steps (data, control, or both)
- Failure semantics (retryable vs fatal, partial failures, etc.)
- Isolation and resource semantics at a high level
- Execution strategy semantics (sequential, parallel, batched, or scheduler-driven behaviors)

All of this is expressed in a way that is **backend-neutral** within the class. Kubernetes, Nomad, and Argo might all implement `container/v1`; GitHub Actions and GitLab runners might both implement `vm/v1`.

---

## 5. Relationship to Maps, Navigators, Routes, and Guides

Papyrus is the anchor that keeps the rest of the stack honest.

### 5.1 Maps → Papyrus

- Every Map declares exactly one Papyrus dialect it targets.
- The Map vocabulary (steps, dependencies, Cargo flows) is interpreted through that dialect.
- The Compass rejects Maps that violate Papyrus semantics.

### 5.2 Navigators → Papyrus

- Navigators describe how toolkits run *within a Papyrus dialect*.
- A Navigator for `container/v1` cannot silently assume `vm/v1` semantics.
- Navigator authors must map their toolkit’s behavior onto Papyrus semantics, not the other way around.

### 5.3 Routes (IR) → Papyrus

- The Route is a fully-typed, backend-neutral execution graph expressed in Papyrus terms.
- Papyrus defines what a “valid Route” means for a dialect.
- Downstream analysis operates on Routes whose semantics are fixed by Papyrus.

### 5.4 Guides → Papyrus

- Each Guide implements exactly one Papyrus dialect for its backend; backend support is a one‑to‑one mapping between a Guide module and a Papyrus dialect.
- A Guide’s job is:
  - take a valid Route for a Papyrus dialect
  - emit backend-native configs that preserve semantics
- Guides must not:
  - reinterpret the Route as something else
  - add new steps or side effects
  - silently drop semantics

Because of Papyrus, the IR is not “whatever the Guide felt like doing today.” It is a well-defined contract.

---

## 6. Semantic Minimalism

Papyrus deliberately models **only what must be shared** across:

- Maps
- Navigators
- Routes
- Guides
- Backends in the same class

This semantic minimalism is deliberate and enforced:

- Papyrus **only** describes semantics that:
  - are unavoidable for correctness, or
  - are truly common across at least two independent backends in a class.
- Papyrus **does not** try to encode:
  - every feature of every backend
  - every optimization or scheduling trick
  - vendor-specific enhancements

This has two important consequences:

1. **Governance and neutrality.**

   - No single vendor can push their product’s quirks into Papyrus and call it “standard.”
   - The core remains small, understandable, and reviewable.

2. **Ecosystem flexibility.**

   - Backends can innovate freely at the edges without destabilizing the core.
   - Features can be tried as Extensions first and promoted to Papyrus only when they prove general.

Papyrus behaves more like an ISA or ABI than a kitchen-sink spec. It captures **the minimum necessary semantics** to make deterministic, portable workflows possible.

---

## 7. Papyrus Extensions (High-Level Overview)

*Extensions cannot alter or override core Papyrus semantics. This safeguard preserves neutrality, prevents vendor capture, and ensures that Extensions remain additive rather than authoritative.*

Backend vendors and platform authors often need to express **additional, backend-specific semantics** that are:

- meaningful
- important
- widely used

…but not yet universal enough to belong in Papyrus core.

For this, OriGen supports **Papyrus Extensions**:

- Namespaced, vendor-defined semantic additions attached to a Papyrus dialect.
- Safe to ignore by backends that do not recognize them.
- Visible in Maps and Routes, so that analysis can still reason about their presence.
- Eligible for promotion into Papyrus core via RFC and governance process.

Extensions allow innovation and differentiation **without fragmenting the core language**. They are treated as first-class contributions, not afterthoughts.

> The full Extension model, structure, and lifecycle is defined in `16-papyrus-extensions.md`.

---

## 8. Governance and Evolution (Sketch)

*Deprecated Papyrus dialects remain valid indefinitely; they are never removed, but may be superseded by newer dialect versions. This guarantees long-term stability for implementers while allowing the model to evolve.*

Papyrus is not user-editable. It evolves via an explicit, public process:

- Changes to Papyrus dialects happen only through RFCs.
- New dialects (e.g., `hpc/v1`) are proposed and reviewed as part of the same process.
- Backwards-incompatible changes require a new dialect version (e.g., `container/v2`).
- The IR and Papyrus are subject to conformance tests.

The goals of this governance model are to:

- keep IR semantics stable and trustworthy
- avoid vendor capture
- encourage vendors to propose Extensions first, and core changes only when clearly justified

Details of the governance model are described in `15-versioning-evolution.md` and in the future governance charter.

---

## 9. Non-Goals

Papyrus intentionally does **not** aim to:

- Describe every execution product on the market.
- Replace backend-specific configuration languages.
- Act as a general-purpose programming language.
- Model runtime policy engines, identity systems, or network topologies.

Those concerns live in:

- backend implementations
- security and policy layers
- infrastructure and platform design

Papyrus focuses narrowly on **execution semantics for deterministic planning and translation**.

---

## 10. Summary

Papyrus is the semantic bedrock of OriGen:

- It defines the **world models** in which Maps make sense.
- It constrains what a **Route (IR)** is allowed to mean.
- It keeps Navigators and Guides **honest** about how tools behave.
- It allows vendors to innovate through **Extensions** without fragmenting the core.

By keeping Papyrus minimal, typed, and governed, OriGen can offer a deterministic, portable, and vendor-neutral way to express workflows – without sacrificing the freedom to evolve.

