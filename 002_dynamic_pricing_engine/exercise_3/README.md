# Exercise 3 — Contextual Product Processing

This exercise marked an important conceptual transition in the use of lambda functions.

Until this point, lambdas were mostly treated as compact syntax for simple transformations.

Here, the transformation logic started depending on contextual information:
- product category
- business rules
- multiple input values

One important insight was realizing that:

lambda x: ...

is conceptually very close to:

def function(...):

Another major insight emerged when testing inline lambdas directly inside the processing flow:

(lambda ...)(...)

This introduced the idea that lambdas can exist as immediate contextual operations instead of only named reusable functions.

However, this exercise also exposed an important limitation:

compactness does not necessarily improve code quality.

As the inline lambda became larger, readability started degrading significantly.

This led to one of the most important insights of the evolution path:

- compact code is not always better code
- clarity is often more important than reducing lines

The exercise also introduced:
- contextual transformations
- unpacking for readability
- separation between processing flow and transformation logic

This was one of the first moments where lambda usage became a design decision instead of just a syntax feature.

Another important limitation became visible during this exercise:

the current implementation only works well with a small number of categories.

As more categories and business rules are introduced, the conditional logic would quickly become harder to maintain and scale.

This was one of the first moments where scalability limitations started becoming visible even in otherwise functional code.
