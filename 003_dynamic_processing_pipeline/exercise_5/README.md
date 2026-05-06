# Exercise 5 — Dynamic Corporate Processing Pipeline

This exercise marked the point where architectural complexity became the dominant challenge of the evolution path.

At this stage, the problem was no longer centered around:
- map()
- lambda syntax
- isolated transformations

The main challenge became organizing a dynamic processing pipeline with progressively evolving state.

Some stages modified salary values, while others only added metadata.

As the pipeline evolved, multiple transformations started depending on previously processed data, introducing an important architectural challenge:

processing stages needed access to shared and continuously updated state.

One of the biggest difficulties encountered during the exercise was dynamically reusing updated salary values across multiple stages without hardcoding the pipeline structure.

This exposed an important limitation of the current architecture:
- configurable rules alone were no longer sufficient

The system now required:
- dynamic orchestration
- generic execution flow
- shared processing context
- scalable pipeline composition

Another important realization was that the main pipeline still depended too heavily on structural knowledge about:
- previous stages
- intermediate state
- available fields

At this point, the challenge had clearly evolved into a real architectural problem rather than a simple transformation exercise.

This exercise intentionally remained unresolved.

During the exercise, it became clear that the problem had already moved beyond the current stage of learning.
Instead of forcing a solution artificially, the exercise was kept as a documented architectural limitation to revisit in the future with more advanced concepts and tools.

This marked the transition from:
- learning programming tools

to:

- facing real software architecture constraints
