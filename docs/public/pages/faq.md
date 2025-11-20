# 🧠 **OriGen FAQ — Comprehensive Architectural Reference**

*A single page answering every question reviewers will ask in the first 30 minutes.*

---

## 🧭 What is OriGen, in one sentence?

OriGen is a **workflow compiler**:
it transforms declarative Maps into deterministic Routes, which Guides translate into backend-native execution.

OriGen does **not** run workflows.

---

## 🧱 Is OriGen an orchestrator?

**No.**
OriGen does not run, schedule, retry, or orchestrate anything.

Execution is handled entirely by:

* GitHub Actions
* GitLab CI
* Argo / Kubernetes
* Containers / VMs
* Bare-metal scripts

OriGen only produces configuration for these systems.

---

## 📘 What does a Map define?

A Map defines **intent**:

* steps
* dependencies (DAG)
* toolchains (Navigators)
* resources (Backpacks / Cargo)
* parameterization
* artifact flow structure

Maps contain **no** runtime behavior and depend on **zero** environment state.

---

## 🚧 What is a Navigator?

A Navigator defines a **frozen toolchain**:

* pinned container image digest
* entrypoints
* available modes
* deterministic configuration

Navigators participate in ADP and Downsweep because they define immutable inputs.

---

## 🚚 What is Cargo?

Cargo is the **unified abstraction for all mounted resources** in a workflow.

Cargo can originate from:

* a Backpack (immutable input)
* a Navigator-provided static resource
* a runtime artifact produced by an earlier step

Cargo defines **flow**, not data.

---

## 🎒 What is a Backpack?

**Backpack = Cargo with enforced immutability.**

Backpacks represent **immutable, digest-pinned inputs** made available to steps.

Compass enforces:

* Backpacks are **always read-only**
* Backpacks must reference manifests
* Users cannot override mount modes
* Backpacks can never contain runtime outputs

Backpacks are part of planning-time provenance (ADP).

---

## 🧩 How do Backpacks and Cargo differ?

Backpack **is** Cargo — with extra rules:

| Property                | Backpack      | Runtime Cargo             |
| ----------------------- | ------------- | ------------------------- |
| Origin                  | manifest      | workflow execution        |
| Immutable?              | **Yes**       | mutable by producer only  |
| Mode                    | **forced RO** | producer RW, consumers RO |
| Known at planning time? | Yes           | No                        |
| Digest-pinned?          | **Yes**       | No                        |
| ADP participant?        | **Yes**       | No                        |

---

## 🔒 Can users override Backpack mount modes?

**No.**
Compass enforces Backpack immutability:

* Any `rw` request is rejected
* Any attempted override is normalized back to `ro`
* Backpacks never accept updates or mutations

This preserves determinism, reproducibility, and ADP correctness.

---

## 🔄 What is a Route?

A Route is OriGen’s **intermediate representation (IR)**:

* deterministic
* fully expanded
* backend-neutral
* explicit DAG
* immutable

Guides consume Routes and produce backend-native execution configs.

---

## 🧭 Are Routes DAGs or lists?

Routes are **DAGs**.

They support:

* sequential steps
* parallelism
* fan-in/fan-out
* conditional dependencies

The structure is abstract; backends interpret it in their own execution model.

---

## 🧪 What does a Guide do?

Guides **translate** Routes into backend-native configs.

Guides must **not**:

* add steps
* modify behavior
* retry
* discover environment details
* reinterpret Maps or Routes
* inject implicit logic

Guides are translators, not planners.

---

## 🔐 How does OriGen handle secrets?

It doesn’t.

Maps may reference **secret names**, but:

* OriGen never reads secret values
* OriGen never fetches or decrypts secrets
* Backends inject secrets at execution time

This preserves zero-trust boundaries.

---

## 🔄 **How does OriGen handle state? **

OriGen distinguishes **structural state** from **runtime state**:

### **1. Structural state (planning-level)**

Maps define **Cargo flows**:

* which step produces which artifact
* which steps consume those artifacts
* Backpack mounts
* dependency graph edges
* resource paths and names

OriGen validates and compiles this into a deterministic Route.

**OriGen cares about the *shape* of artifact flow, not the data.**

### **2. Runtime state (execution-level)**

Actual artifacts produced by execution — files, logs, binaries, models, PDFs — are handled entirely by the backend.

OriGen does **not**:

* store
* hash
* track
* manage
* inspect
* retain

**any runtime data.**

Backends own:

* artifact stores
* workspaces
* caches
* retention policies
* access control

> **Users plan Cargo flows in maps; backends handle Cargo contents.**

---

## 🧬 Does OriGen guarantee deterministic results?

OriGen guarantees **deterministic planning**, not deterministic execution.

Execution depends on:

* tool behavior
* randomness
* time-based functions
* external APIs
* backend-specific quirks

OriGen is not a build system and does not enforce reproducible computation.

---

## 🧱 What are OriGen’s main limitations?

OriGen does **not**:

* run workflows
* orchestrate tasks
* manage secrets
* manage state
* hash outputs
* track runtime artifacts
* guarantee deterministic outputs
* replace CI systems
* replace Kubernetes

It sits *above* execution systems.

---

## 🔐 Why does OriGen make zero-trust cheap?

Zero-trust emerges from:

* immutable toolchains
* digest-pinned Backpacks
* explicit Cargo flows
* pure, environment-free planning
* no hidden dependencies
* no global state
* no runtime inference
* enforced boundaries

OriGen removes the conditions that require validation in the first place.

---

## 🧾 What is Automatic Digital Provenance (ADP)?

ADP emerges naturally:

1. Navigators/Backpacks produce digests
2. Builds commit manifests
3. Maps reference manifest commits
4. Routes embed exact input identities

This creates:

* full dependency lineage
* reconstruction of any workflow
* complete toolchain traceability
* audit-ready compliance

ADP requires no additional system.
OriGen’s architecture already guarantees it.

---

## 🍂 What is Downsweep?

Downsweep is the reverse of ADP:

1. Identify vulnerable digest
2. Find the manifest commit that introduced it
3. Discover all Maps referencing that commit
4. Enumerate affected workflows
5. Generate PRs to update Maps
6. Produce impact reports

Downsweep makes org-wide remediation automatic.

---

## 🧨 What breaks ADP?

Only user violations:

* not committing manifests
* referencing digests manually
* mixing Backpack and Cargo types
* embedding tags instead of digests
* using Backpacks as mutable state
* skipping Navigator/Backpack abstraction

ADP itself is robust — misuse breaks provenance.

---

## 🧨 What breaks Downsweep?

Downsweep requires:

* manifests to exist
* Maps to reference commits
* Navigators/Backpacks to pin digests

If teams inline digests or skip manifest commits, coverage shrinks.

---

## 🧭 How do I actually use OriGen?

You usually:

1. Write a Map
2. Reference Navigators and Backpacks
3. Run Compass → generate Route
4. Feed Route into a Guide
5. Run the resulting config in your backend

Most daily work happens in Maps.

---

## 📘 What should I read first?

1. Primer
2. Top-Level Architecture
3. Zero-Trust-by-Design
4. Automatic Digital Provenance (ADP)
5. This FAQ

---

## 🎯 Summary

OriGen’s model is:

* **Maps**: intent
* **Navigators/Backpacks**: immutable inputs
* **Cargo**: unified mount abstraction
* **Compass**: pure planning
* **Route**: deterministic IR
* **Guides**: backend translators
* **Backpack = cargo with forced immutability**
* **Zero-trust emerges naturally**
* **ADP emerges structurally**
* **Downsweep scales remediation across orgs**

Everything fits together cleanly.
