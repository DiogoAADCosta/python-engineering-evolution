# Exercise 4 — Configurable Campaign Rules

This exercise introduced the first configurable rule structure of the evolution path.

The initial implementation relied on direct conditional flow:

- if campaign == ...
- elif campaign == ...

While functional, this approach quickly became harder to scale as more campaigns and business rules were introduced.

To improve organization, the system evolved into a rule-based structure:

(condition, action)

This introduced an important architectural separation between:
- decision logic
- transformation logic

Example:

- condition:
  lambda campaign: ...

- action:
  lambda price, category: ...

This was also one of the first moments where the exercises started resembling real system architecture instead of isolated transformations.

A major insight from this exercise was realizing that:
- lambdas can represent executable rules
- systems can become configurable through external rule structures
- conditions and actions can operate independently

Another important realization was the structural similarity with the rule-processing architecture used in the Guitar Diagnostic System.

Both systems rely on:
- conditional evaluation
- contextual actions
- configurable execution flows

This exercise reinforced the idea that similar architectural patterns can naturally emerge across completely different domains.

Related project:
[Guitar Diagnostic System](https://github.com/DiogoAADCosta/guitar-diagnostic-system)

This exercise marked the transition from:
- simple lambda transformations

to:
- configurable processing systems
