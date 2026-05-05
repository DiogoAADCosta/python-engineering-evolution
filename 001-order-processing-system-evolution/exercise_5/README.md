This exercise marks the first major structural refactor
in the order processing evolution path.

As the workflow became more complex,
processing logic started spreading across the codebase,
making reuse and maintenance harder.

To solve this, the system was reorganized into:
- isolated business rules
- single-order processing
- batch-order processing

This introduced the first reusable processing pipeline
in the project.
