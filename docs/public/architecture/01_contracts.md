# OriGen Architecture — Contracts



## 1. Purpose

This document defines the contractual foundations of the OriGen architecture. These contracts describe the structural commitments that ensure consistency, reliability, and long‑term stability across all components of the system. Their purpose is practical: to give implementers and adopters a clear, coherent framework for understanding how OriGen behaves and why its guarantees hold.

A contract expresses:

- what each layer guarantees,
- what each layer requires,
- what each layer must never do.

The following sections outline these relationships with the same clarity and discipline that underpin the broader architecture, establishing a stable baseline from which the system can grow without compromising its core principles.

---

## 2. Design Principles

OriGen contracts are built on three architectural pillars:

### 2.1 Determinism

The identical set of inputs must produce identical outputs:

- same Map version,
- same Navigators,
- same Backpacks,
- same Papyrus dialect version,
- same Dictionary.

No external state, host environment, or ambient runtime may influence planning or translation.

### 2.2 Immutable Invariants

OriGen enforces a strict separation between:

- **planning** (pure, repeatable)
- **execution** (performed by external platforms)

Any mutation, side effect, or dynamic behavior occurs **outside** OriGen.

### 2.3 Governed Evolution

OriGen semantics, interfaces, and dialects evolve through controlled, explicitly versioned governance processes.

Backwards compatibility must be **deliberate**, **reviewed**, and **documented**.

---

## 3. Planning Boundary Contract

### 3.1 OriGen Performs Planning Only

OriGen’s responsibility ends when platform-native files are written. Planning-time components—Maps, Navigators, Backpacks, and Papyrus dialects—operate exclusively on **declarative structures**, including the semantic definitions of Cargo (its shape, flow, and interface). No runtime data, logs, or state produced by an executed workflow is visible to the planning system.

OriGen MUST NOT:

- execute workflows,
- provision infrastructure,
- call containers, VMs, or APIs,
- mutate remote systems,
- query runtime states or read runtime Cargo,
- introspect the host beyond allowed metadata.

This boundary ensures reproducibility and prevents origin-time nondeterminism.

---

## 4. Semantic Contracts

### 4.1 Map Contract

A Map declares **intent**, not mechanics.

A Map must be:

- declarative,
- free of platform-specific constructs,
- stable under re-evaluation,
- fully serializable.

A Map MUST NOT:

- embed backend configuration,
- embed runtime logic,
- use dynamic/host-derived values.

### 4.2 Navigator Contract

A Navigator defines toolchain behavior templates and interfaces with **abstract Cargo**, not execution-time artifacts.

Navigator invariants apply **only during planning**, where the Navigator must behave as a pure, deterministic function. Navigators operate exclusively on **declarative cargo shapes**—the semantic representations of inputs and outputs—not on physical runtime data.

Navigator invariants:

- deterministic field resolution,
- no network I/O,
- no filesystem access outside declared Backpacks,
- no time-dependent values,
- no branching on host environment,
- may reference **abstract cargo flows**, but not runtime artifacts.

Navigator logic MUST be **pure**. Declarative definitions of cargo interfaces, schemas, and flows are permitted. Accessing or inspecting **runtime-generated Cargo** is forbidden. If logic cannot be expressed without side effects, it must be packaged into a Backpack and treated as data.

### 4.3 Backpack Contract

Backpacks are the **immutable input universe**.

A Backpack:

- MUST be content-addressed or version pinned,
- MUST be fully available at planning time,
- MUST NOT change during planning or between runs,
- MUST NOT be implicitly downloaded, mutated, or assembled by OriGen.

Backpacks are part of **provenance**, so immutability is mandatory.

### 4.4 Papyrus Dialect Contract

Papyrus provides the **execution semantics model**.

A dialect defines:

- task semantics,
- isolation model,
- artifact flow,
- failure conventions,
- workspace rules,
- **step execution strategy** (e.g., linear, fan-in, fan-out, parallel structures).

A dialect MUST:

- be stable and versioned,
- avoid backend-specific constructs,
- avoid execution semantics not representable across multiple environments.

### 4.5 Route (IR) Contract

The Compass produces a fully resolved, deterministic Route:

- all dependencies resolved,
- semantics validated,
- dialect rules applied,
- no unresolved or dynamic fields.

The IR Route:

- MUST NOT reference host state,
- MUST NOT rely on Guide behavior,
- MUST be sufficient for deterministic translation without backtracking.

The IR is the **canonical representation of workflow semantics**.

The IR Route MUST explicitly represent **step execution strategy**, including linear sequencing, fan-in, fan-out, and parallel structures. Execution strategy is derived from Map declarations and dialect semantics and MUST be fully resolved at planning time. The IR MUST encode all dependency and concurrency relationships without requiring backend interpretation.

### 4.6 Dictionary Contract

A Dictionary maps Papyrus semantics to **backend vocabulary**.

It MUST:

- declare compatibility with a dialect version,
- be deterministic,
- never redefine Papyrus meaning,
- never introduce new semantics not permitted by Extensions,
- treat **Extensions as optional, namespaced hints**, not as behavioral overrides.

A Dictionary MAY read Extensions **only** to refine translation where the underlying Papyrus semantics remain intact. Removing all Extensions from a Map or IR MUST NOT change the validity of the workflow under the declared dialect.

### 4.7 Extension Boundary (Non-expansive)

Extensions allow vendors to express additional, backend-relevant metadata without altering Papyrus itself. They exist to support innovation at the edge while keeping the semantic core stable.

Extensions MUST:

- be namespaced,
- be safe for Dictionaries and Guide to ignore,
- never contradict Papyrus semantics,
- never introduce planning-time side effects,
- remain purely declarative and deterministic.

Extensions MAY:

- refine translation in vendor-specific Dictionaries,
- surface optional backend features,
- annotate cargo shapes or step metadata.

Extensions are preserved in IR but are **non-expansive**: they cannot widen or redefine the semantic surface of Papyrus. They inform translation without becoming part of the core contract.

### 4.8 Guide Contract

A Guide translates IR into **platform-native configuration**, unmodified by runtime semantics.

A Guide MUST:

- produce only static files,
- emit only formats the backend would accept verbatim,
- be pure (deterministic),
- implement Dictionary mappings exactly.

A Guide MUST NOT:

- invoke executors, runners, clusters, or remote services,
- embed runtime-generated fields,
- mutate backend configurations post-emission.

---

## 5. Determinism Contract

OriGen guarantees deterministic behavior across both planning and translation. This guarantee applies to the system as a whole, but the inputs that determine planning differ from the inputs that determine translation.

### 5.1 Planning Determinism

Given the same planning-time inputs:

- Map,
- Navigators,
- Backpacks,
- Papyrus dialect version,
- Extensions (as declarative metadata),

OriGen MUST produce a bit-for-bit identical **Route (IR)**. The Guide does not participate in planning determinism, and Dictionaries do not influence IR generation.

### 5.2 Translation Determinism

Given the same translation-time inputs:

- IR (already deterministic),
- Dictionary version,

OriGen MUST produce bit-for-bit identical **backend-native output**.

### 5.3 Determinism Requirements

Determinism requires:

- explicit versioning of all inputs affecting semantics or translation,
- rejection of floating references ("latest"),
- no host environment dependency,
- no uncontrolled randomness,
- stable sorting, normalization, and canonicalization rules.

If determinism cannot be guaranteed at any stage, the system MUST emit a deterministic failure.

---

## 6. Execution Boundary Contract

OriGen does not own or influence execution. Once files are emitted:

- their interpretation is the responsibility of the backend,
- OriGen has no authority beyond the moment of emission.

This limitation is intentional.

Execution drift (platform updates, feature deprecations) is not an OriGen responsibility. Platform behavior SHOULD be captured in versioned Dictionaries to maintain stable translation across time.

---

## 7. Provenance (Informative)

Provenance is an optional, derived product of OriGen’s planning process. It is **not** part of the contractual surface and **does not** influence planning, translation, or execution.

Provenance may be generated by external tooling or by optional OriGen modules, but it MUST remain outside the planning boundary defined in Sections 3 and 6.

Provenance MAY include:

- identifiers of Maps, Navigators, Backpacks, and dialect versions,
- IR identifiers or hashes,
- metadata useful for debugging, auditing, or human inspection.

Provenance MUST NOT:

- alter Compass behavior,
- change determinism guarantees,
- reference runtime or execution-time Cargo,
- create obligations for implementations.

Provenance exists to assist users and implementers, not to define behavior or affect outcomes.

---

## 8. Governance Contract

### 8.1 Versioning Discipline

Every public-facing construct MUST follow:

- SemVer or equivalent,
- monotonic version increments,
- documented changes,
- backwards-compatibility guidance.

### 8.2 Dialect Governance

Dialects evolve slowly under governance:

- changes require review,
- changes MUST preserve cross-backend semantics,
- breaking changes require new dialect versions.

### 8.3 Vendor Implementer Obligations

Vendors implementing Extensions/Dictionaries MUST:

- declare supported dialect versions,
- document deviations,
- avoid redefining or shadowing existing Papyrus semantics,
- avoid proprietary forks of dialects,
- ensure any **new semantic primitives introduced via Extensions** are:
  - namespaced,
  - deterministic,
  - non-conflicting with existing primitives,
  - safe for other implementations to ignore,
  - expressible within the dialect's execution strategy model.

New primitives introduced by Extensions MAY refine or extend workflow semantics, but they MUST NOT override or mutate existing core primitives. Successful primitives MAY be proposed for future inclusion in Papyrus through the governance process.

### 8.4 Neutrality Principle

OriGen maintains vendor neutrality. No Guide or Dictionary should become de facto mandatory.

Governance ensures interoperability without privileging specific runtimes.

---

## 9. Compliance

Components are compliant if:

- they honor all contracts defined herein,
- they pass determinism tests,
- their semantics match dialects exactly.

Non-compliant components SHOULD be rejected by Compass or fail deterministically.

---

## 10. Conclusion

The Contracts model ensures OriGen remains:

- deterministic,
- predictable,
- backend-agnostic,
- reproducible across decades,
- resistant to vendor lock-in,
- governed by a stable semantic foundation.

These contracts form the backbone of OriGen’s specification and MUST remain intact across future architectural evolution.

