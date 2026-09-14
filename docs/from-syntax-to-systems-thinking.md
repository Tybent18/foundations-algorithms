# From Syntax to Systems Thinking: A Cross-Language Programming Foundation

**T. R. Bentley**  
Repository-grounded technical report | September 2026  
Repository: Tybent18/foundations-algorithms

> [Download the publication PDF](from-syntax-to-systems-thinking.pdf) · [Repository README](../README.md)

## Abstract

This technical report examines a compact collection of C, Python, and Java exercises as evidence of progression from syntax-level reasoning toward algorithmic and debugging practice. The repository is intentionally foundational: its value lies in transparent, inspectable examples rather than scale. The report maps implemented artifacts, distinguishes working examples from deliberate debugging targets, and proposes a reproducible path for strengthening the collection.

## Scope

Programming foundations, low-level reasoning, pairwise operations, and cross-language debugging targets.

Claims are limited to named repository artifacts. Proposed tests, benchmarks, integrations, and research directions are future work—not reported results.

## Repository evidence map

| Cluster | Artifacts | Interpretation |
| --- | --- | --- |
| Core C exercise | `pairwise.c` | Array and pairwise operations; compilation provides direct behavioral evidence. |
| Debugging targets | `debug.c, debug.java, debug.py` | Language-specific failure investigation; some files are intentionally imperfect. |
| Structured debugging | `debug_datastruct.py` | Extends error reasoning into data-structure behavior. |

## Technical questions

- How does the same debugging habit transfer across C, Java, and Python?
- Which failures are caught during compilation, parsing, or runtime?
- How can small examples expose control flow and state clearly?

## Reproducible inspection protocol

A reviewer should clone the repository, record the commit SHA and toolchain versions, inspect each mapped artifact, execute only examples with declared entry points, preserve outputs and errors, and compare observations with stated expectations. A deliberate debugging failure is evidence only when its expected failure class is declared in advance.

## Evidence maturity

| Level | Meaning |
| --- | --- |
| E0 | Artifact listed |
| E1 | Intended behavior described |
| E2 | Environment, command, and output recorded |
| E3 | Repeatable behavioral tests included |
| E4 | Frozen data supports a bounded comparison |

## Limitations

- The repository is a learning artifact, not an algorithm library.
- Several debugging files intentionally contain defects and should not be presented as passing demonstrations.
- Automated tests and recorded outputs are not yet included.

## Development roadmap

- Add expected-outcome fixtures for every debugging target.
- Record compiler/interpreter versions and commands.
- Add a small cross-language failure taxonomy and CI matrix.

## Portfolio role

This repository belongs to the cumulative sequence **Foundations & Algorithms → Data Structures Practice → OOP Concepts → Math for Computing → Practical Utilities**. Advanced repositories carry the stronger systems and empirical-research claims.

## Conclusion

The repository is most credible when each claim points to inspectable code and future measurements can be added without rewriting history. Sophistication comes from traceability, not inflated labels.
