---
type: research-dashboard
tags: [robot-learning, research]
---
# Research dashboard

[[Home]] | [[17 Finding a Research Question]] | [[Research Landscape]]

## Current candidates

| Question | Status | Next evidence | Hardware fit |
|---|---|---|---|
| [[Recovery Data versus More Demonstrations]] | Proposed; novelty unchecked | Reproducible baseline and failure taxonomy | Strong initial SO-101 fit |
| [[Latency and Chunking Study]] | Proposed; novelty unchecked | Timestamped deployment trace | Strong initial SO-101 fit |
| [[Jev for Robot Skill Selection]] | Proposed; access and novelty unchecked | Labeled offline states and non-API baselines | Start offline |
| Human-to-robot transfer | Reading stage | Identify obtainable human data and alignment assumptions | More dependencies |

## The evidence ladder

1. Observation: a behavior or failure you can reproduce.
2. Hypothesis: a possible explanation with a predicted result.
3. Experiment: a controlled comparison that could disprove it.
4. Result: measured evidence with uncertainty and a recorded protocol.
5. Research claim: the narrow conclusion supported by that evidence.

Move a note up this ladder only when the missing evidence exists. A limitation cluster from the paper-mining pipeline is a reading lead; it is not a novelty certificate.

## Live vault searches

The native Base below organizes idea and experiment properties as editable rows:

![[Research Board.base]]

These are built-in Obsidian search embeds and need no community plugins.

~~~query
path:"Robot Learning Book" tag:#research-idea
~~~

~~~query
path:"Robot Learning Book" tag:#experiment
~~~

## Working habits

Use [[Experiment Template]] before running a comparison. Attach logs, configuration hashes, dataset manifests, videos, and analysis plots after it. Use [[Reading Template]] to keep author claims separate from your interpretation.

Each week create a [[Weekly Review Template]] entry and identify one result that changed your belief. Unchecked tasks live in [[Mastery Tracker]]. Completed reading alone does not establish mastery.
