# Exercise 3 — Corporate Benefits Pipeline

This exercise introduced the first true multi-stage transformation pipeline of the evolution path.

Until this point, transformations were mostly isolated.

Here, each processing stage became dependent on the result produced by the previous stage:

salary adjustment
→ bonus calculation
→ salary classification

One of the most important realizations from this exercise was that:

some transformations only exist because previous transformations already happened.

For example:
- bonus calculation depends on adjusted salary
- classification depends on the final salary after bonus application

This introduced an important architectural concept:

progressive state propagation across processing stages.

The system also became explicitly pipeline-oriented:

employees_adjustment
→ employees_bonus
→ employees_classification

Each map() operation became an independent transformation stage responsible for producing the input of the next stage.

Another important realization was the growing discomfort with positional indexing:

employee[3]
employee[4]
employee[5]

As more stages were introduced, tuple-based structures started becoming:
- harder to read
- harder to maintain
- increasingly fragile

This exercise reinforced an important idea:

the main challenge was no longer using map(),
but organizing transformation pipelines and evolving data structures in a scalable way.

It was also one of the first moments where lambda functions started feeling optional instead of essential, as the growing transformation complexity naturally increased the need for more explicit structure and organization.
