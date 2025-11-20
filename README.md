# **README.md**

<p align="center">
  <img src="docs/public/images/origen-logo.jpg" width="120" alt="OriGen Logo">
</p>

<h1 align="center">OriGen</h1>
<p align="center"><strong>Deterministic Workflow Plans • Zero-Trust by Design • Automatic Digital Provenance</strong></p>

---

## What Is OriGen?

OriGen is a lightweight, deterministic workflow planner.

It separates intent from execution:

```

Map → Compass → Route → Guide → (your backend)

````

OriGen never runs workflows.
It **compiles** them.

Maps declare intent.
Navigators and Backpacks freeze tools and resources by digest.
The Compass plans deterministically.
Guides translate the plan into backend-native execution artifacts.

The result is a workflow model that is:

- explicit
- reproducible
- backend-agnostic
- structurally zero-trust
- inherently provenance-rich

OriGen is not an orchestrator.
It is not a runner.
It is not CI/CD.

OriGen is the **missing compiler** between declarative workflow intent and real execution.

---

## Core Concepts

**Map**
Declarative workflow intent (your source of truth).

**Navigator**
Digest-pinned toolchain or executor definition.
Examples: compilers, PDF engines, linters, transformers.

**Backpack**
Immutable resource bundle (fonts, templates, configs, datasets).

**Compass**
Pure planner: converts Map + Navigators + Backpacks → Route.

**Route**
An explicit, immutable, backend-neutral plan.

**Guide**
Backend adapter: translates Route into GitHub Actions, GitLab CI, Kubernetes jobs, Argo workflows, or local scripts.

OriGen produces plans.
Other systems execute them.

---

## Minimal Mental Model

![](https://origen-hub.github.io/origen-core-public/images/origen-flow.png)

---

## Why OriGen Exists

Modern DevOps has grown brittle, implicit, and opaque:

* tools mutate silently
* CI contexts drift
* environments leak state
* security becomes reactive
* provenance is bolted on after the fact

OriGen’s architecture flips the model:

* **everything is explicit**
* **everything is digest-pinned**
* **planning is pure and deterministic**
* **execution is isolated and external**

This makes zero-trust not a policy, but a structural side-effect.

---

## Zero-Trust by Design

OriGen removes the trust surfaces that zero-trust frameworks usually defend.

- No mutable toolchains.
- No inherited environments.
- No runtime discovery.
- No global state.
- No cross-step mutation.
- No hidden behavior.

Zero-trust stops being expensive.

It becomes cheap.

> Curious how?
> Read **[Zero-Trust by Design](docs/public/security/zero-trust-by-design.md)**.

---

## The Maintenance Paradox

Pinning everything normally creates maintenance hell.

In OriGen, it does the opposite.

Because every build, digest, and commit is explicit and traceable, the system naturally forms a provenance graph.
This is not an add-on or an integration.

It emerges.

This leads directly to:

---

## Automatic Digital Provenance (ADP)

ADP is the structural consequence of OriGen’s immutability and determinism.

Every digest maps to:

* the commit that built it
* the manifest that published it
* the Maps that consume it
* the Routes they produce

With this graph, organizations gain **instant, reconstructable lineage**.

> Learn more: **[Automatic Digital Provenance](docs/public/security/adp/automatic-digital-provenance.md)**

---

## Downsweep: Organization-Wide Reverse Dependency Discovery

ADP enables “downsweeps”:
Given a vulnerable digest, OriGen can:

1. identify the manifest commit that introduced it
2. discover all Maps referencing that commit
3. enumerate every affected workflow
4. generate automated PRs
5. produce impact and remediation reports

Downsweep turns security from reactive to mechanical.

---

## Getting Started

OriGen is in early development.
The architecture is public and stable; the codebase will follow.

For now, start with:

* **[Primer](docs/public/overview/origen-primer.md)**
* **[Values](docs/public/overview/value-statement.md)**
* **[Top-Level Architecture](docs/public/overview/00-top-level.md)**

---

## Intrigued?

OriGen is small, but the consequences are large.

If you want to understand *why the system behaves the way it does*, begin here:

➡ **[Architecture Overview](docs/public/architecture/00-top-level.md)**

---

## Status

OriGen is actively being developed.
Public docs are available; the public codebase will follow.

---

## Contributing

OriGen welcomes:

* feedback
* discussions
* Navigator / Backpack definitions
* Guide adapters
* security and provenance reviewers

Open an issue or join the discussions.
The project grows concentrically—start small, end inevitable.

---

## License

Apache 2.0 unless otherwise noted.

```
