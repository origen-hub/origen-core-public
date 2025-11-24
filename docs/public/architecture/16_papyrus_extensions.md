# Papyrus Extensions

Papyrus Extensions provide a structured, vendor-friendly mechanism for augmenting a Papyrus dialect without altering core semantics. Extensions enable platforms, tool vendors, and backend authors to introduce additional capabilities, preferences, or metadata while preserving the stability, neutrality, and portability of OriGen’s workflow model.

## 1. Purpose

Extensions allow vendors to:

- add optional, backend-relevant metadata to Maps;
- express capabilities not yet represented in Papyrus;
- refine behavior for specific environments without compromising portability;
- propose new concepts for future Papyrus versions.

Extensions ensure innovation can proceed rapidly while Papyrus evolves at a deliberate, stable pace.

## 2. Design Principles

Extensions must adhere to four principles:

### 2.1 Namespaced

All Extensions must be declared under a vendor or project namespace, such as:

```
x-aws:
  batchSchedulingHints: {...}
```

Namespaces prevent naming conflicts and make Extension ownership explicit.

### 2.2 Non-Mutating

Extensions must not modify:

- Papyrus types
- Papyrus constraints
- Step semantics
- Retry rules
- Isolation models
- Cargo behavior

Extensions only add metadata; they never redefine meaning.

### 2.3 Optional and Safe to Ignore

Backends or Guides that do not implement a given Extension must be able to ignore it without causing failure. Extensions:

- may refine behavior for supported backends;
- must not be required for correct workflow execution;
- must not introduce inconsistencies if removed.

### 2.4 Promotable to Core

Frequently used, widely-accepted Extensions may be proposed for inclusion in future versions of Papyrus. Promotion requires:

- a formal RFC;
- demonstration of ecosystem need;
- agreement across multiple vendors;
- a versioned Papyrus release.

This provides a clean path from experimentation → adoption → standardization.

## 3. Where Extensions Appear

Extensions may appear in:

- **Maps**, where users annotate Steps, dependencies, or workflow intent with vendor capabilities;
- **IR**, where Extensions are preserved verbatim for backend translation.

Extensions DO NOT appear in:

- Papyrus dialect definitions;
- Navigator definitions or templates;
- Guide internals;
- execution outputs.

## 4. Processing Model

### 4.1 During Planning

Extensions are:

- validated for structure (schema-based),
- namespaced and isolated,
- copied into the IR without interpretation.

The Compass does not evaluate or execute Extensions.

### 4.2 During IR-to-Backend Translation

Guides may:

- interpret Extensions they support;
- ignore unsupported Extensions safely.

Guides must never treat missing Extensions as errors.

### 4.3 During Execution

Extensions have no runtime presence. They are compile-time hints only.

## 5. Schema Structure

Extensions follow this general pattern:

```
x-<vendor>:
  <extension-name>:
    <structured-fields>
```

Example:

```
x-github:
  permissions:
    id-token: write
    contents: read
```

## 6. Use Cases

### 6.1 Backend-Specific Capabilities

Vendors may expose features such as:

- affinity/scheduling preferences
- permission or credential scopes
- parallelism or batching hints
- caching options
- ephemeral resource behaviors

### 6.2 Early Prototyping of Future Papyrus Concepts

When a new concept is not yet ready for core inclusion, Extensions provide a safe incubation path.

### 6.3 Multi-Backend Workflows

Extensions allow workflows to remain backend-neutral while enabling enhanced functionality where available.

## 7. Vendor Sovereignty

Pa**pyrus Extensions are fully vendor-owned. V**endors may introduce, modify, or retire Extensions at any time without approval from the OriGen project or any central authority.

Extensions:

- do not require RFCs;
- do not require review;
- do not require coordination;
- may evolve independently of Papyrus releases;
- may remain vendor-specific indefinitely;
- may be experimental or provisional;
- do not impose backward-compatibility obligations on the vendor.

Only Extensions proposed for promotion into core Papyrus enter the formal RFC process.

## 8. Non-Goals

Extensions must not:

- introduce new Step types;
- define new execution semantics;
- mutate Papyrus behavior;
- replace Navigator logic;
- embed backend-specific syntax inside Papyrus itself.

## 9. Lifecycle

Extensions follow a three-stage lifecycle:

1. **Experimental** – introduced by a vendor; unreviewed.
2. **Adopted** – used across multiple projects; stable schemas.
3. **Promotable** – eligible for Papyrus RFC consideration.

Promotion into Papyrus marks the end of the Extension lifecycle.

## 10. Conformance Requirements

A valid Extension must:

- reside under a namespaced key;
- validate against its vendor schema;
- never invalidate or contradict Papyrus;
- be safe to ignore;
- be preserved exactly in IR.

## 11. Summary

Papyrus Extensions enable backend and vendor innovation without compromising OriGen’s determinism or neutrality. By layering optional, structured metadata on top of stable Papyrus semantics, Extensions provide a clean path for experimentation, ecosystem growth, and future standardization.

