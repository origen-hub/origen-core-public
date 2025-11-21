# OriGen - Executive Overview

## The 30-Second Summary

**OriGen is a deterministic workflow compiler.**

You define *what* should happen using a simple declarative Map, and OriGen generates native execution artifacts (Kubernetes manifests, container scripts, etc.).

OriGen does **not** run workflows.
It produces **portable, reproducible, reviewable plans** that your existing tools execute.

**Kubernetes is the first backend. More backends follow through a simple adapter interface.**

---

## One-Minute Mental Model

![One-Minute Mental Model](../images/origen-flow.png "One-Minute Mental Model")

OriGen stops here.
Your existing systems handle execution.

---

## What Problems Does OriGen Solve?

Across industries, teams repeatedly face the same workflow issues:

### 1. Drift

Tool versions, CI YAML, environment defaults, and small script changes produce inconsistent results over time.

### 2. Duplication

Teams re-implement identical workflow logic across:

* GitHub Actions
* GitLab CI
* Argo
* Airflow
* Tekton
* Makefiles / Bash

OriGen removes this duplication: **one Map → many backends.

### 3. Fragile Glue Code

Organizations build wrappers, DSLs, and generators that are brittle and hard to maintain.
OriGen replaces ad-hoc glue with a stable, versionable model.

### 4. No Portable Workflow Description

Workflows often exist only as:

* tribal knowledge
* comments
* platform-specific YAML
* private scripts

OriGen provides a **single declarative description of workflow intent**, independent of runtime.

---

## Plain-English Components

| Component     | What it is in practice                                                     |
| ------------- | -------------------------------------------------------------------------- |
| **Map**       | Declarative YAML describing workflow steps, inputs, outputs, dependencies. |
| **Navigator** | A pinned tool definition (container image + argument template, by digest). |
| **Backpack**  | Immutable resource bundle (fonts, configs, templates, data, etc.).         |

Together, they encode the entire workflow in a stable, versionable form.

---

## End-to-End Example #1 — Publishing Workflow

Convert Markdown → LaTeX → PDF.

**Map:**

```yaml
steps:
  - tool: pandoc
    mode: md-to-tex
    input: doc.md
    output: build/doc.tex

  - tool: texlive
    mode: xelatex
    input: build/doc.tex
    output: build/doc.pdf
```

**Compile with OriGen:**

```
origen render-k8s maps/publish.yml --out .kube/publish/
```

**Output (native Kubernetes Jobs):**

```
.kube/publish/
  00-pandoc.yaml
  01-texlive.yaml
```

Apply normally:

```
kubectl apply -f .kube/publish/
```

No new runtime. No new controller.

---

## End-to-End Example #2 — DevOps Workflow

Build → Scan → Publish a container image.

**Map:**

```yaml
steps:
  - tool: buildkit
    mode: build
    input: Containerfile
    output: image:my-app:latest

  - tool: trivy
    mode: scan
    input: image:my-app:latest
    output: scan-report.json

  - tool: crane
    mode: push
    input: image:my-app:latest
    output: registry.internal/my-app:stable
```

OriGen can compile this into Kubernetes Jobs or container-execution scripts.
One Map → multiple runtimes.

---

## End-to-End Example #3 — Data Pipeline Workflow

Extract → Transform → Upload.

**Map:**

```yaml
steps:
  - tool: fluentbit
    mode: extract
    output: raw-logs/

  - tool: spark
    mode: transform
    input: raw-logs/
    output: processed/

  - tool: awscli
    mode: s3-upload
    input: processed/
    output: s3://analytics/processed/
```

OriGen renders this into:

* Kubernetes Jobs, or
* local container-run scripts

Same Map, different backends.

---

## Developer Experience (DX)

Workflows live directly in the repo:

```
repo/
  maps/
  navigators/
  backpacks/
  routes/
  guides/
```

Developers:

* edit Maps
* preview outputs locally
* review diffs
* commit deterministic plans

OriGen feels like part of standard development, not a new platform.

---

## Backend Extensibility (Open by Design)

Guides translate **Route → native artifacts**.

They are intentionally simple to implement:

* K8s (MVP)
* Podman/Docker
* Serverless runners
* Data/ML platforms
* HPC/Batch environments

The architecture encourages community and enterprise-specific backends.

---

## Governance & Lock-In

Enterprises can host everything privately:

* Maps
* Navigators
* Backpacks

There is:

* **no OriGen runtime**
* **no controller**
* **no SaaS dependency**
* **no proprietary service**
* **no lock-in**

OriGen adds **zero new infrastructure**.

All outputs are plain files you own.

---

## Incremental Adoption

OriGen can be adopted gradually:

* per workflow
* per team
* per repository

No need for organizational coordination or CI/CD replacement.
You can start with a single Map and expand as needed.

---

## FAQ (Executive-Focused)

### Does OriGen replace CI/CD?

No. OriGen only generates the plan. CI/CD still runs it.

### Do developers need to learn a new language?

No. Maps are standard YAML.

### Where do workflow assets live?

In your repos and registries, like any other versioned artifacts.

### Is Kubernetes required?

No — it’s simply the first backend.

### Is there lock-in?

No. OriGen outputs native, human-readable files.

### Can teams preview plans locally?

Yes. Developers can render and validate outputs before committing.

---

## Why Kubernetes First

Kubernetes is:

* declarative
* widely adopted
* deterministic at the interface level
* already home for most containerized workflows

This makes it the best proving ground for deterministic planning.
Additional backends build on the same model.

---

## Where to Go Next

Continue to:

➡ [Value Statement][origen-value-statement] — a deeper explanation of OriGen’s philosophy, architecture, and long-term vision.
