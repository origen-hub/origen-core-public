# Automatic Digital Provenance (ADP)

### *Provenance That Emerges From Determinism*

---

ADP is not a feature added to OriGen.
It is a pattern that **falls out of the architecture** once workflows become explicit, immutable, and deterministic.

This document defines ADP, explains why it emerges naturally from OriGen’s model, and introduces **downsweep** — the organizational capability that ADP unlocks.

---

## 1. What ADP Is

Automatic Digital Provenance (ADP) is a workflow property where:

* toolchains are defined in Git,
* builds are pinned by digest,
* rebuilds are deterministic,
* and provenance can be reconstructed automatically from the commit graph.

ADP transforms provenance from a reactive security practice into an **automatic structural consequence** of how workflows are defined.

---

## 2. Why ADP Emerges From Cheap Zero-Trust

ADP depends on four architectural guarantees:

### 2.1 Explicit Toolchains

Tools are declared in Navigators, not inferred or discovered.

### 2.2 Immutable Digests

Every referenced tool and resource is pinned by digest.

### 2.3 Pure Planning

The Compass does not execute, mutate, or discover anything at runtime.

### 2.4 Immutable Intent (Route)

Execution intent becomes a complete, stable artifact.

When these conditions hold:

* the workflow graph becomes stable,
* toolchain definitions are versioned,
* provenance becomes derivable from Git,
* and verification becomes trivial.

ADP is the natural result.

---

## 3. The ADP Model

ADP describes a simple chain:

![The ADP Model](../../images/adp-graph.png "The ADP Model")

Each link is:

* immutable,
* content-addressed,
* reconstructable.

This makes provenance:

* complete,
* inspectable,
* mechanically verifiable.

There is no hidden behavior, no dynamic resolution, and no untracked state.

---

## 4. ADP Workflow

An ADP-enabled workflow produces a natural provenance trail:

1. A maintainer updates a Navigator or Backpack.
2. A new build produces a new digest.
3. A CI job commits a manifest with metadata.
4. Consumers reference the commit hash in their Maps.
5. The Compass produces a Route that records the exact digest.
6. Any future audit can trace:

   * which tools were used,
   * which version produced them,
   * who built them,
   * and which commits referenced them.

This requires no special tooling.
It emerges from deterministic architecture and Git hygiene.

---

## 5. What ADP Enables

ADP turns provenance into a structural capability.

### 5.1 Automatic Rebuild Lineage

A digest can always be traced back to its Navigator/Backpack definition.

### 5.2 Historical Reconstruction

Any historical Route carries complete provenance.

### 5.3 Audit-Ready Workflow Definitions

Maps become self-contained compliance artifacts.

### 5.4 Organizational Impact Analysis

You can identify everywhere a digest appears across repositories by searching for the commit hash.

These capabilities set the stage for downsweep.

---

## 6. Downsweep: Organizational Reverse Dependency Discovery

Downsweep is the operational capability unlocked by ADP.

A downsweep is triggered when a vulnerable or outdated digest is identified.
From there, the process is:

1. **Identify the vulnerable digest (D1).**
   This may come from a CVE scanner, policy engine, or periodic audit.

2. **Locate the manifest commit (C2) that published D1.**
   This is the commit that contains the manifest referencing the digest,
   produced by the automated build pipeline.

3. **Search all Maps for references to C2.**
   Each Map that references C2 is a consumer of the vulnerable toolchain or resource.

4. **Enumerate every affected workflow.**
   Each Map → Route → backend execution path represents a workflow that needs updating.

5. **Generate automated PRs to update each Map to a safe commit.**
   The system proposes a new commit reference (C2′ or C3) containing patched digest(s).

6. **Produce organization-wide impact and remediation reports.**
   Security, platform, and compliance teams receive complete visibility into:

   * which workflows are affected
   * which repos are impacted
   * which PRs were generated
   * what was remediated and what is still pending

> **Downsweep operationalizes ADP by turning provenance information into automated, organization-wide updates.**

![Downsweep in action](../../images/adp-downsweep.png "Downsweep in action")

It is simple, mechanical, and requires no human knowledge transfer.

---

## 7. Implications for Supply-Chain Security

ADP and downsweep together offer:

* complete toolchain lineage,
* org-wide vulnerability propagation mapping,
* automated corrective PR generation,
* tamper-resistant historical records,
* and predictable security posture.

This elevates provenance from a best-effort practice to a guaranteed property.

---

## 8. ADP Is General — OriGen Is the First ADP-Native System

ADP is not proprietary to OriGen.
It is a general pattern that any deterministic, digest-pinned, Git-defined toolchain system can adopt.

OriGen simply happens to be:

* the first system designed for ADP from the beginning,
* the cleanest implementation,
* and the reference mental model for the pattern.

---

## 9. Summary

ADP redefines provenance by removing the ambiguity that makes provenance hard.
Downsweep operationalizes that provenance at scale.

Together they offer:

* structural transparency,
* deterministic security,
* and a clear pathway to organizational integrity.

OriGen is the architecture that makes ADP possible.
ADP is the pattern that brings OriGen to the world.

---

**Intrigued? Explore the [Architecture Overview][origen-architecture-top-level-overview].**
