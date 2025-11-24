# Governance Principles

OriGen is designed as a neutral, deterministic workflow compiler that supports multiple backends, toolchains, and execution environments. Long-term stability depends on a clear, transparent, and vendor-inclusive governance model. This document defines the public principles guiding the evolution of Papyrus, IR, Extensions, versioning, and backend interoperability.

## 1. Purpose of Governance

The goal of OriGen governance is to ensure that:

- Papyrus dialects remain stable, predictable, and interoperable.
- IR remains a consistent, deterministic contract across backends.
- Vendor participation is encouraged without compromising neutrality.
- Extensions can evolve safely into future versions.
- Backends and tool vendors can integrate without risk of fragmentation.
- Users can rely on OriGen for reproducible workflows over long timescales.

These principles ensure that OriGen remains a trusted component of multi‑environment workflow ecosystems.

## 2. Evolution of Papyrus

Papyrus dialects form the semantic substrate for all workflow meaning in OriGen. Each dialect defines Step types, retry semantics, isolation rules, Cargo behavior, workspace rules, and determinism constraints.

Papyrus evolves under the following principles:

- Stability First: dialect semantics change only through formal RFCs.
- Backward Compatibility: existing workflows must continue to function.
- Semantic Minimalism: Papyrus captures only backend‑agnostic semantics.
- Vendor Neutrality: dialects cannot embed backend‑specific semantics.

## 3. Extensions

Extensions provide a mechanism for vendors to introduce structured, namespaced additions on top of a Papyrus dialect without altering core semantics.

Extensions follow these principles:

- Namespaced: ownership is explicit and collision‑free.
- Non‑Mutating: Extensions cannot alter Papyrus semantics.
- Optional: unsupported backends must ignore them safely.
- Promotable: widely used Extensions may be proposed for core inclusion.

Extensions enable innovation while preserving stability.

## 4. Vendor Sovereignty of Extensions

Papyrus Extensions are fully vendor‑owned. Vendors may introduce, change, or retire Extensions at any time without approval from the OriGen project or any central authority.

Extensions:

- do not require RFCs;
- do not require review;
- do not require coordination;
- may evolve independently of Papyrus releases;
- may remain vendor‑specific indefinitely;
- may be experimental or provisional;
- do not impose backward‑compatibility obligations on the vendor.

Only Extensions proposed for promotion into Papyrus core enter the formal RFC process.

## 5. IR Stability

The Intermediate Representation (IR) is a deterministic, backend‑agnostic form of Workflow Intent. Governance ensures that:

- IR remains typed, declarative, and stable.
- IR contains no backend‑specific fields.
- IR evolves conservatively and predictably.
- Routes generated from IR behave consistently across environments.

## 6. Guide Responsibilities

The Guide performs translation using backend Dictionaries. Vendors provide Dictionaries, not Guide.

- implement translation faithfully without altering semantics;
- respect Papyrus and Navigator rules;
- interpret supported Extensions;
- ignore unsupported Extensions safely.

## 7. Versioning and Releases

OriGen uses a structured versioning model:

- Major Versions: new dialects or significant semantic changes.
- Minor Versions: new Extensions, additive features, Guide capabilities.
- Patch Versions: bug fixes and documentation.

Backward compatibility is prioritized.

## 8. Conformance

Conformance testing ensures interoperability across backends and vendors.

Conformance rules include:

- IR Conformance: Routes must match Papyrus semantics.
- Guide Conformance: the core translator must emit backend-native structures that precisely reflect IR meaning.
- Dictionary Conformance: vendor-authored dictionaries must correctly map Papyrus and IR semantics into backend-native constructs without altering core meaning.
- Navigator Conformance: toolchains must be pinned, deterministic, and Papyrus-legal.
- Extension Conformance: Extensions must be valid, namespaced, non-mutating, and safely ignorable.


## 9. Summary

This governance model provides a transparent, vendor‑neutral foundation for the long‑term evolution of OriGen and its ecosystem.
