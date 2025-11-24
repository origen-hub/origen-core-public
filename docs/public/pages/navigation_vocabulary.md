# Navigation Vocabulary — Why OriGen Uses These Terms

Modern workflows span publishing pipelines, data pipelines, CI/CD systems, ML training, scientific computation, and infrastructure automation. Each domain comes with its own terminology:

- “jobs,” “tasks,” “steps,” “actions”
- “operators,” “pods,” “stages,” “runners”
- “flows,” “targets,” “nodes,” “executors”

These terms collide, overlap, and contradict one another. A model that tries to unify these systems using domain-specific vocabulary collapses under the weight of the assumptions each domain brings with it.

OriGen solves this by using a **navigation metaphor** — a set of neutral, domain-agnostic terms that map directly to the architecture’s boundaries and contracts.

The metaphor is conceptual, not cosmetic. It feels natural to most readers because it mirrors how people already think about planning, direction, and translation. Each term anchors a specific responsibility in the system. 

---

## 1. Why This Metaphor Exists

The navigation vocabulary serves three purposes: to create clean boundaries, avoid domain jargon, and make workflows universally understandable.

### 1.1 To create clean mental boundaries

Most workflow frameworks fail because their concepts bleed into one another:

- intent mixed with execution
- steps mixed with toolchains
- runtime artifacts mixed with inputs
- backend semantics mixed with planning semantics

OriGen separates these concerns sharply. The navigation terms visually and conceptually reinforce those boundaries.

### 1.2 To avoid domain-specific jargon

DevOps terminology doesn’t map cleanly to ML pipelines.
Scientific workflow terminology doesn’t map cleanly to CI systems.
Publishing workflows don't resemble data engineering pipelines.

Neutral vocabulary allows OriGen to describe **all workflows with one conceptual model**.

### 1.3 To make users workflow generalists

Instead of thinking:

- GitHub Actions
- Kubernetes
- GitLab CI
- Jenkins
- Argo
- Airflow
- Nextflow
- Snakemake

…users think in a consistent conceptual layer cake:

- Map
- Navigator
- Backpack
- Papyrus
- Compass
- Route
- Dictionary
- Guide

Once internalized, this model lets users reason about any workflow system using the same mental tools.

---

## 2. The Vocabulary at a Glance

Each term in the navigation vocabulary is both:

- an **architectural boundary**, and
- part of a **coherent mental model** for reasoning about workflows.

Below is the vocabulary presented in a single unified view — what each term *is*, how it fits into the conceptual chain, and why the model tends to feel intuitive in practice.

### Map — What you want to happen *(intent)*

Declarative workflow intent. Pure description. No execution semantics.

### Navigator — How steps are realized *(behavior)*

Defines toolchain behavior. Maps a Map Step into Papyrus semantics.

### Backpack — What you need at planning time *(resources)*

Immutable planning-time resources. Always known, always pinned.

### Papyrus — What workflow steps mean *(semantics)*

Typed semantic model. Defines retry semantics, isolation, Cargo behavior, and Step types.

### Compass — How it is validated and typed *(planning)*

Pure deterministic planner. Turns Map + Navigators + Backpacks + Papyrus semantics into a fully typed Route.

### Route — What the workflow is *(representation)*

The complete, backend-neutral IR. No execution semantics, no runtime assumptions.

### Dictionary — How a backend expresses meaning *(vocabulary)*

Vendor-authored mapping from Papyrus semantics into backend-native constructs.

### Guide — How meaning becomes runnable files *(translation)*

Reads the IR and Dictionaries. Emits backend-native configuration. Adds no semantics — it applies backend vocabularies but introduces no meaning of its own.

---

## 3. Why These Terms Improve Reasoning

Traditional workflow systems mix concepts:

- “tasks” express both intent and execution
- “jobs” include both toolchain and semantics
- “steps” blur runtime actions with planning descriptions
- “actions” carry implicit container behavior
- “operators” assume Kubernetes-style runtime

You can’t reason about correctness or determinism in that soup.

The navigation vocabulary:

- enforces separation of concerns,
- encodes architecture into language,
- makes invariants obvious,
- reduces ambiguity,
- lowers cognitive load across domains,
- makes portability and reproducibility tractable.

Once internalized, it becomes the fastest way to reason about workflows.

---

## 4. The Payoff

After a short learning curve, the metaphor becomes intuitive:

- Maps are intent
- Navigators define behavior
- Backpacks provide resources
- Papyrus defines meaning
- Compass plans
- Routes describe
- Dictionaries translate
- Guides emit

The vocabulary makes complex workflows predictable, portable, and deterministic.

It is not an ornament. It is the cognitive geometry of OriGen.

