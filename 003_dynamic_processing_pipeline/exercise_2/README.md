# Exercise 2 — Employee Processing by Department

This exercise marked an important transition in the evolution path:

the system stopped processing isolated values and started processing complete entities.

Instead of transforming simple numbers, the processing flow now handled structured employee data:
- name
- department
- salary

One important realization from this exercise was that:
- business rules become easier to maintain when separated from processing flow

This led to the creation of an external rule structure:

rules = {...}

where department-specific salary adjustments became configurable independently from the transformation pipeline itself.

Another important insight was the growing discomfort with positional tuples:

employee[0]
employee[1]
employee[2]

As the structures became more complex, positional indexing started becoming:
- harder to read
- less semantic
- more difficult to maintain

This was one of the first moments where the limitations of tuple-based modeling became explicit.

The exercise also reinforced an important architectural pattern already explored in previous projects and exercises:
- externalized business rules
- configuration-driven behavior
- separation between execution and logic

At this stage, the main challenge was no longer simply using map(),
but organizing increasingly dynamic transformations in a maintainable way.
