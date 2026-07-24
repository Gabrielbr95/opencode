# Concepts Research

This directory stores the slower-moving idea layer of the research tree.

## What Belongs Here
- durable concepts
- stable boundaries
- architecture principles
- cross-vendor tradeoffs that should survive product churn

Examples:
- agent architectures
- planning systems
- memory systems
- context engineering
- instruction layering

## What Does Not Belong Here
- current product behavior or config details
- reusable subsystem mechanics that deserve a capability note
- repository maps or comparison documents that synthesize several notes

## Common Questions for a Concept Note
- what is this idea?
- what problem does it solve?
- what distinctions matter most?
- what tradeoffs and failure modes keep showing up across products?

## Working Rule
If the note's center of gravity is a reusable mechanism or subsystem, it probably belongs in `../capabilities/` instead.

If the note mainly explains one tool's current behavior, it belongs in `../products/`.
