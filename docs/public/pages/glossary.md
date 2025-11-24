# Glossary

## A

### Automatic Digital Provenance (ADP)
The emergent provenance graph produced from Maps, Navigators, Backpacks, Papyrus validation, and IR Routes.
ADP tracks all immutable, planning-time resources and semantics.
Cargo is explicitly excluded from ADP.

## B

### Backpack
An immutable, externally provided resource required during planning.
Backpacks are fully known at planning time, versioned or hashed, read-only, and included in ADP.
They must not be created or modified at runtime.

### Backends (Execution Environments)
External systems that execute the backend-native files produced by a Guide.
Backends own all runtime behavior, resource provisioning, and secret management.
OriGen responsibility ends at the Execution Boundary.

## C

### Cargo
Data produced or modified at runtime.
Cargo is mutable, ephemeral, backend-owned, and not part of determinism or ADP.
Cargo edges form the runtime dataflow graph and are distinct from Backpacks.

### Compass
OriGen’s deterministic planner.
Consumes a Map and its Navigators, validates against Papyrus, resolves Backpacks, and produces a fully typed IR Route.
Performs pure planning only, with no execution or environment discovery.

### Conformance
The requirement that Guides, Navigators, Papyrus dialects, Dictionaries, and Extensions adhere to the IR specification and determinism model.
Necessary for backend interoperability and ecosystem stability.

## D

### Determinism
Guarantee that IR Routes and backend-native outputs are identical for identical inputs.
Determinism applies only to planning and file emission, not to runtime execution or external system behavior.

### Dialect (Papyrus Dialect)
See Papyrus.

### Dictionary
A vendor-authored vocabulary that maps Papyrus and IR semantics into backend-native constructs.
Dictionaries evolve independently of OriGen core and must declare compatibility with specific Papyrus versions.
They allow vendors to extend backend behavior without implementing their own Guide.

## E

### Execution Boundary
The point where OriGen stops.
After generating backend-native files, OriGen performs no execution, validation, or environment interaction.
All runtime concerns belong to the backend.

### Extension (Papyrus Extension)
A vendor-authored, namespaced semantic augmentation to a Papyrus dialect.
Extensions do not modify core semantics, are safe to ignore by unsupported backends, and may be promoted into Papyrus through RFC.

## G

### Guide
The translator that converts IR Routes into backend-native configuration using backend Dictionaries.
Guides do not execute workflows or define backend behavior.
They reflect Papyrus, IR, Navigator constraints, and vendor Extensions.

## I

### IR (Intermediate Representation)
A fully typed, deterministic, backend-independent representation of Workflow Intent.
Routes contain no backend-specific fields and form the provenance graph for ADP.

## M

### Map
A declarative expression of Workflow Intent.
Contains Steps, dependencies, arguments, Backpack references, and optional Extensions.
Does not express execution mechanics or backend-specific behavior.

## N

### Navigator
A pinned, immutable specification of how Steps are realized with a particular toolchain.
Defines behavior templates, required Backpacks, and Step-to-Papyrus mappings.
Cannot define new Papyrus types or alter core semantics.

## P

### Papyrus
The semantic substrate that defines workflow meaning.
A Papyrus dialect specifies Step types, retry semantics, isolation rules, Cargo behavior, workspace semantics, and determinism constraints.
Not user-editable; evolution occurs through RFC and versioning.

### Papyri
The complete family of Papyrus dialects.

## R

### Retry Semantics
Dialect-defined rules for retrying Steps.
Part of Papyrus; cannot be altered by Maps, Navigators, or Guides.

### Route (IR Route)
The output of the Compass: a fully validated, typed, deterministic representation of Workflow Intent.
Backend-agnostic and stable across toolchains and environments.

## U

### Upstream Drift
Any mutation of tools, defaults, images, or external environments that would normally destabilize workflow reproducibility.
OriGen neutralizes upstream drift through pinned toolchains and pure planning.

## W

### Workflow Intent
The high-level description of what a workflow should accomplish.
Encoded in a Map; validated through Papyrus; realized through a Route.
