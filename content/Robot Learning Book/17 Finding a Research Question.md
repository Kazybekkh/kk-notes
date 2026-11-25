---
type: chapter
chapter: 17
status: not-started
tags: [robot-learning, research-methods]
---
# 17 Finding a research question

[[Home]] | Previous: [[16 Evaluation and Uncertainty]] | Next: [[18 Masters Research and Startup Path]]

A broad topic such as “human video for robots” becomes research when it names a mechanism, a comparison, and a measurable outcome. The useful first question is often why a reproducible baseline fails under a specific condition.

## Turn reading into evidence

For each relevant paper, record the task, assumptions, data, model, evaluation, and limitations with page or section locations. Distinguish an author-stated limitation, your own inference, and a missing experiment. A missing experiment does not establish that no one has studied it.

The current [[Start Here]] collection contains abstract-level notes. Before using one to support novelty, inspect the full paper, its related work, and later papers. The graph of concept links is a thinking aid, not a verified citation graph.

~~~mermaid
flowchart LR
  Read["Read primary evidence"] --> Reproduce["Reproduce baseline"]
  Reproduce --> Failure["Characterize failure"]
  Failure --> Hypothesis["Propose mechanism"]
  Hypothesis --> Ablation["Test controlled change"]
  Ablation --> Update["Update belief and question"]
  Update --> Read
~~~

## A hypothesis template

“Under condition C, changing X while holding Y fixed improves metric M relative to baseline B because mechanism Z addresses failure F.”

Example proposal: “At the same demonstration-minute budget, adding recoveries improves held-out grasp recovery more than adding more nominal successes.” The mechanism is better coverage of states visited after errors. The result may be negative, which is useful if the experiment is sound.

## Choose a project with an exit route

Score feasibility, data access, evaluation clarity, research value, and your interest on a small ordinal scale. These scores organize judgment; they are not probabilities of publication. A project must have a useful outcome if its preferred method does not work.

Define a minimum viable study: one task, one baseline, one intervention, a fixed test set, and a complete failure analysis. Add tasks only after the first result is interpretable.

## Your research record

Use [[Reading Template]] for evidence, [[Experiment Template]] for reproducible runs, and [[Research Dashboard]] to track status. Create a [[Weekly Review Template]] entry answering what you believed, what you tested, and what changed.

**Exercise:** improve “Can AI make SO-101 smarter?” into a measurable question.

> [!success]- Example answer
> “Does a short observation history improve pick-and-place success under temporary gripper occlusion compared with a single-frame policy, using the same architecture budget and demonstrations?”

Explore [[Research Landscape]], [[Recovery Data versus More Demonstrations]], [[Latency and Chunking Study]], and [[Jev for Robot Skill Selection]]. None is a confirmed novel contribution yet.
