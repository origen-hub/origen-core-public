# 📚 OriGen Glossary

A reference list of all core terms and concepts used across the OriGen documentation.
This glossary is domain-agnostic and reflects the finalized terminology model: **Maps → Route → Guide**, supported by **Navigators** and **Backpacks**.

---

# A

### **Adapter**

See **Guide**. A component that translates a Route into native execution artifacts for a specific runtime or platform.

---

# B

### **Backpack**

An **immutable, versioned, read-only resource bundle** carried into execution.
Contains static dependencies such as templates, datasets, fonts, configs, metadata, or any other deterministic material.
Backpacks are pinned by digest, never mutated, and never produced by Steps.

### **Cargo**

Any output produced by a Step — files, directories, images, binaries, datasets, or generated artifacts.
Cargo is mutable and may be consumed by later Steps.

---

# C

### **Compass**

OriGen’s core planning engine.
Loads Maps, Navigators, and Backpacks; resolves dependencies; validates structure; and compiles the workflow into a deterministic **Route**.
The Compass performs **pure planning only**: no execution, discovery, or environment interaction.

### **Commit Reference**

A Git commit hash recorded in a Map or manifest to bind a workflow to a specific version of a Navigator, Backpack, or build manifest.
Used heavily in ADP and downsweep.

---

# D

### **Determinism**

A first-class architectural constraint.
Identical inputs must produce identical outputs **and** identical failures across all backends and environments.

### **Digest**

A content-addressed identifier (typically OCI-style) used to pin toolchains, Backpacks, or other resources.
Provides immutability and guarantees that upstream drift cannot alter execution.

### **Downsweep**

An organizational-scale capability enabled by ADP.
Triggered when a vulnerable or outdated digest is found.
Locates every Map referencing the corresponding commit, enumerates dependent workflows, and generates automated updates or remediation reports.

---

# E

### **Execution Boundary**

The point where OriGen stops.
Beyond this boundary, external runtimes (CI systems, orchestrators, VMs, embedded platforms, etc.) execute the artifacts emitted by Guides.

---

# G

### **Guide**

A backend adapter that converts a Route into native execution artifacts (Kubernetes manifests, CI jobs, Podman commands, VM task files, embedded-runner scripts, etc.).
Guides **translate**, never execute.

---

# I

### **Immutable Intent**

The complete, backend-neutral representation of a workflow as encoded in the Route.
Once produced, intent cannot mutate downstream.

### **Intermediate Representation (IR)**

See **Route**.

---

# M

### **Map**

A declarative specification of workflow intent.
Defines Steps, tools, modes, I/O relationships, and dependencies.
Maps contain **no imperative code** and serve as the human-authored source of truth.

---

# N

### **Navigator**

A pinned tool definition describing how a tool behaves: container/VM image (or other runnable form), entrypoint, modes, argument templates, and required Backpacks.
Navigators decouple tool definitions from workflow logic.

---

# O

### **OriGen**

A deterministic workflow compiler.
Produces a stable, reviewable, platform-agnostic Route from declarative Maps.
OriGen does not run workflows — it plans them.

---

# P

### **Pure Planning**

A hard guarantee that OriGen performs **no execution**, **no discovery**, and **no I/O** during planning.
All behavior is explicit and determined by Maps + Navigators + Backpacks.

### **Provenance (Automatic Digital Provenance, ADP)**

The structural property where toolchain lineage, workflow definitions, and execution intent can be reconstructed mechanically from Git and digests, without additional instrumentation.
ADP emerges naturally from OriGen’s determinism and immutability.

---

# R

### **Route**

OriGen’s canonical **Intermediate Representation (IR)** — a deterministic, platform-neutral execution graph compiled from a Map.
Encodes workflow structure, dependencies, toolchains, and immutable intent.
Consumed by Guides.

---

# S

### **Schema**

The formal definition that validates Maps, Navigators, Backpacks, and Route structures.
Ensures that workflow intent is unambiguous and stable.

### **Sidecar (Deprecated Term)**

A legacy term referring to what are now called Backpacks.
Remains in older discussions or prototypes but should not appear in current documentation.

### **Step**

The smallest unit of execution in a workflow.
Each Step invokes a Navigator in a specific mode with defined inputs and outputs.

---

# T

### **Topology**

The dependency structure of a workflow: ordering, fan-in, fan-out, and graph shape.
The Compass resolves topology strictly and deterministically.

---

# U

### **Upstream Drift**

Changes introduced by external systems (toolchain upgrades, default changes, environment mutations) that normally cause inconsistent workflows.
OriGen prevents drift through digest pinning and immutable artifact definitions.

---

# W

### **Workflow Intent**

The high-level description of what should happen in a workflow — steps, tools, dependencies, outcomes — independent of environment or runtime.
Captured in Maps and frozen into the Route.

---

End of glossary.
