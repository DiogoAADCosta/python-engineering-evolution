# Exercise 4 — Configurable Salary Processing Platform

This exercise marked one of the biggest architectural transitions of the entire evolution path.

At this stage, the system was no longer simply processing transformations.

It was attempting to become a reusable and extensible processing platform.

The system already supported:
- configurable rules
- configurable processing stages
- externalized business logic

through structures like:

stages = {...}

However, an important structural limitation became explicit:

the pipeline itself was still hardcoded.

Even though the stages were configurable,
every new processing step still required manually adding:
- a new map() block
- a new intermediate structure
- a new execution stage in the main flow

One of the most important realizations from this exercise was:

configuration alone does not make a system truly extensible.

The rules had become configurable,
but the orchestration layer had not.

This introduced an important architectural distinction between:
- configurable business logic
- configurable execution flow

Another major realization was that the problem had already moved far beyond map() and lambda syntax.

At this stage, the real challenge became:
- dynamic orchestration
- generic pipelines
- scalable execution flow
- reusable processing architecture

The exercise also reinforced another important scalability issue:

each new processing stage increased structural complexity significantly.

For example:
- more intermediate structures
- more positional indexes
- more execution blocks
- more coupling between stages

This was one of the first moments where the system genuinely started resembling:
- configurable processing platforms
- orchestration systems
- extensible transformation pipelines

rather than isolated programming exercises.
