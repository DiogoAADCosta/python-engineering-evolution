# 002 — Dynamic Pricing Engine

## Overview

This evolution path started as a simple lambda exercise focused on applying discounts to product prices.

As new business requirements were introduced, the system progressively evolved into a configurable pricing and campaign-processing engine.

The goal of this path was not simply learning lambda syntax, but understanding how dynamic business rules naturally create the need for:
- configurable systems
- separation of responsibilities
- processing pipelines
- orchestration layers
- scalable rule structures

Throughout the exercises, the focus gradually shifted from:
- syntax

to:

- system architecture
- rule organization
- execution flow
- scalability limitations

---

## Evolution Path

### Exercise 1 — Simple Price Transformation

The system starts with a basic promotional campaign:
- apply a fixed discount to all products

At this stage, the focus is:
- first contact with lambda
- isolated transformations
- simple processing flow

The lambda function behaves as a compact transformation tool.

---

### Exercise 2 — Contextual Transformations

The pricing system evolves to support conditional discounts:
- different discounts depending on price range

This introduces:
- contextual transformations
- conditional lambdas
- separation between iteration and transformation logic

An important realization also emerged:
- compact code is not always better code
- readability matters

This was one of the first moments where lambda usage became a design decision instead of just syntax experimentation.

---

### Exercise 3 — Product Processing with Context

The system stops processing only prices and starts handling structured product data:
- name
- category
- price

Business rules now depend on contextual information.

This exercise introduced:
- contextual business logic
- unpacking for readability
- separation between processing flow and transformation logic

It also exposed an important scalability limitation:
- conditional structures become increasingly difficult to maintain as categories and rules grow.

This was one of the first moments where scalability concerns emerged naturally from the system itself.

---

### Exercise 4 — Configurable Campaign Rules

The pricing system evolves into a configurable campaign engine.

Instead of directly hardcoding campaign logic inside conditional flows, the system starts externalizing behavior using:
- condition lambdas
- action lambdas

Example:

(condition, action)

This introduced:
- configurable execution rules
- separation between decision logic and transformation logic
- reusable behavioral structures

At this stage, the exercises started resembling real system architecture instead of isolated transformations.

---

### Exercise 5 — Simultaneous Campaign Processing

The system now supports multiple active campaigns executed sequentially.

This introduced:
- cumulative transformations
- sequential processing stages
- intermediate processing state
- configurable campaign activation

The pricing flow started behaving like a real processing pipeline.

The exercise also exposed new structural challenges:
- nested execution flow
- growing rule complexity
- scalability limitations

This was one of the first moments where the system began resembling:
- workflow engines
- staged transformation systems
- configurable processing pipelines

---

### Exercise 6 — Campaign Priority System

The pricing engine evolves into a priority-based campaign system.

The system must now decide:
- which campaigns can coexist
- which campaigns must be ignored
- which rules have priority

This introduced a major architectural transition:

the system no longer only transforms data —
it also orchestrates execution decisions.

The exercise introduced:
- conflict resolution
- execution filtering
- priority handling
- policy-like behavior

It also reinforced an important realization:

the main challenge was no longer lambda syntax itself,
but organizing increasingly dynamic business rules in a scalable way.

---

## Key Concepts Explored

Throughout this evolution path, the exercises progressively introduced:

- lambda transformations
- contextual processing
- conditional behavior
- sequential transformations
- configurable rules
- dynamic execution flow
- processing pipelines
- intermediate state propagation
- execution orchestration
- priority resolution
- scalability concerns
- configuration-driven behavior

---

## Main Insight

One of the most important lessons from this evolution path was understanding that architectural complexity often emerges naturally from growing business requirements.

The exercises intentionally evolved from:
- simple transformations

into:
- configurable processing systems

allowing scalability problems to appear organically through:
- rule accumulation
- coexistence conflicts
- processing dependencies
- orchestration complexity

This created a much more realistic understanding of why software architecture becomes necessary.

---

## Final Note

This path represents the transition from:

simple lambda usage
→ contextual business rules
→ configurable campaign systems
→ dynamic execution orchestration

The focus was never simply learning lambda syntax,
but understanding how real systems evolve as business rules become increasingly dynamic and interconnected.
