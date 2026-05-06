# Exercise 5 — Simultaneous Campaign Processing

This exercise introduced the first multi-stage processing pipeline of the evolution path.

Until this point, transformations were mostly isolated or executed independently.

Here, multiple campaigns started interacting with the same product sequentially.

This introduced an important architectural concept:

processing stages can propagate transformed state over time.

Example:

price = original_price

↓

price = action(price, category)

Each campaign receives the updated value produced by the previous stage.

This exercise also reinforced the idea that:
- systems can become configurable through external rule structures
- campaigns can be activated or deactivated dynamically
- processing rules can remain separated from execution flow

Another important insight was the growing scalability challenge.

As more campaigns and business rules were introduced, the nested loops and rule structure started becoming harder to maintain and extend.

This was one of the first moments where the system began resembling:
- configurable workflow engines
- rule-processing pipelines
- staged transformation systems

The exercise also introduced:
- intermediate processing state
- cumulative transformations
- sequential rule execution
- configurable campaign activation

