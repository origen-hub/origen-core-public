# Versioning & Evolution

This document defines how OriGen evolves over time: how core IR, Papyrus dialects, Extensions, Navigators, Backpacks, Guide, and Dictionaries change, version, and stabilize. Its purpose is to ensure predictability, long-term interoperability, and backwards‑compatible growth.

## 1. Principles of Evolution

OriGen’s evolution follows four architectural principles:

1. **Determinism First** – No change may compromise reproducible planning or IR stability.
2. **Semantic Minimalism** – Only meaning that is stable, universal, and backend‑agnostic belongs in core or Papyrus.
3. **Independent Lifecycles** – Core, Papyri, Extensions, Guide, and Dictionaries evolve separately.
4. **Forward Migration** – All evolution paths must provide clear, mechanical migration options.

## 2. Versioning Units

OriGen consists of several independently versioned layers:

### 2.1 Core IR

The core IR defines the minimal, cross‑class primitives shared across all Papyri.

- Evolves slowly and conservatively.
- Major versions rare and accompanied by migration tooling.
- Minor versions are additive only.

### 2.2 Papyrus Dialects (Papyri)

Each Papyrus dialect (e.g., `container/v1`, `vm/v1`) defines the semantics of a workflow class.

- Each dialect has its own version stream.
- New versions may introduce new primitives, refine semantics, or deprecate older constructs.
- Dialects do **not** need to stay in sync with one another.

### 2.3 Extensions

Extensions evolve independently of Papyri.

- Versioning is owned by the vendor.
- No central approval required.
- Promotion into Papyrus requires an RFC.

### 2.4 Navigators & Backpacks

Navigators and Backpacks version with their manifests.

- Versions reflect changes to toolkit behavior or resource composition.
- Version bumps are consumer‑driven; OriGen does not enforce version schemes.

### 2.5 Guide

Guide consists of two distinct parts:

1. **Core Translator** – maintained with OriGen core and evolves with IR and Papyrus.
2. **Dictionaries** – vendor‑authored vocabularies for translating Papyrus semantics into backend‑native constructs. Dictionaries evolve independently with backend features, Papyrus dialect changes, and vendor Extensions.

This separation ensures:

- Extensions remain meaningful: any namespaced metadata must be translatable by backend authors without waiting for OriGen releases.
- Papyri can evolve without blocking backend support.
- Backends can adopt new capabilities immediately.

Versioning rules:

- **Core Translator** versions follow OriGen’s release cycle.
- **Dictionary** versions follow the backend’s own lifecycle and must declare compatibility with specific Papyrus versions.

## 3. Stability Policies

### 3.1 Additive Semantics

New fields, primitives, or annotations may be added as long as they:

- do not break existing Maps; and
- do not change the meaning of an existing construct.

### 3.2 Deprecations

When semantics must change:

- The older construct is marked deprecated.
- A migration path is published (Map rewrite or Navigator update).
- Deprecation spans at least one major cycle.

### 3.3 Breaking Changes

Breaking changes are restricted to major version increments and require:

- published rationale;
- explicit migration guides;
- automated suggestions where feasible;
- stability guarantees for older major versions for a defined support window.

## 4. Cross‑Dialect Evolution

Evolution across Papyrus dialects follows these rules:

- No Papyrus may introduce semantics that contradict those of another.
- Papyrus families may converge naturally when semantics overlap.
- Shared abstractions may be promoted to `std` (shared library) only when proven universal across classes.

## 5. Compatibility Matrix

A compatibility matrix is maintained to express:

- which Dictionary versions are compatible with each Papyrus dialect version;
- which Navigator and Backpack versions are compatible with specific Papyrus versions;
- which vendor Extension versions are compatible with specific Papyrus and Dictionary versions.

This matrix enables deterministic planning without runtime surprises.

## 6. Migration Models

OriGen supports three migration models:

### 6.1 Intra‑Dialect Migration

Upgrading within a dialect (e.g., `container/v1 → container/v2`).

- Migration assistant can rewrite Maps.
- Navigator/Backpack manifests updated as needed.

### 6.2 Cross‑Dialect Migration

Changing execution classes (e.g., `vm/v1 → container/v1`).

- A best‑effort mapping is produced.
- Human approval is required for business‑logic‑sensitive transformations.

### 6.3 Dictionary Migration

Adopting a new backend within the same Papyrus.

- No Map changes required.
- Only Guide output changes.

## 7. Governance Responsibilities

Version evolution is governed by the following:

- **Core Team**: maintains core IR and coordinates Papyrus RFCs.
- **Dialect Maintainers**: shepherd Papyrus versioning.
- **Vendor Authors**: own Extensions and dictionaries.
- **Community Reviewers**: provide feedback and participate in RFCs.

## 8. Summary

OriGen’s versioning and evolution model ensures:

- long‑term stability;
- controlled semantic growth;
- clear migration paths;
- interoperability across backends;
- room for innovation via Extensions.

The architecture remains deterministic even as ecosystems evolve, allowing OriGen to span years and multiple backend generations without fragmentation.
