# Exercise 6 — Campaign Priority System

This exercise introduced the first priority-resolution layer of the evolution path.

Until this point, the system only focused on applying transformations sequentially.

Now the system also needed to decide:
- which campaigns could coexist
- which campaigns should be ignored
- which rules had execution priority

This introduced an important architectural separation between:
- transformation logic
- decision logic

One of the main insights from this exercise was realizing that:

calculating discounts and deciding which discounts survive are completely different problems.

The exercise also introduced:
- campaign conflict resolution
- execution filtering
- priority handling
- dynamic campaign activation

Another important structural improvement was replacing iterative rule searches with direct dictionary lookups:

price_rules[campaign]

This significantly simplified the processing flow by:
- removing unnecessary iterations
- reducing lookup complexity
- improving readability
- separating configuration from execution

However, this exercise also exposed an important scalability limitation.

The campaign priority system still relied on hardcoded decision rules:

if 'black_friday' in active_campaigns and 'christmas' in active_campaigns:

This worked for a small number of campaigns,
but would become increasingly difficult to maintain as:
- new campaigns
- new coexistence rules
- new priorities
- new exceptions

were introduced.

This was one of the first moments where the system started resembling:
- configurable policy engines
- execution orchestration systems
- dynamic rule-priority architectures

Another important realization was that the exercise had already moved beyond "learning lambda syntax".

At this stage, the main challenge was no longer the lambda function itself,
but the architecture required to organize increasingly dynamic business rules.
