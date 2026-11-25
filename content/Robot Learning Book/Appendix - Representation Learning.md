---
type: appendix
status: not-started
tags: [robot-learning, representation-learning]
---
# Representation learning for robots

[[Home]] | [[04 Perception and State]] | [[12 Human Data and Embodiment]]

A representation compresses observations into features useful for downstream decisions. What you preserve matters more than whether an embedding looks neatly clustered.

## Invariance can remove the wrong information

If lighting changes while the task remains the same, robustness to lighting can help. If object position changes, a manipulation policy often needs to preserve that change. A representation invariant to position may be harmful.

**Invariance** means a feature stays the same under a transformation. **Equivariance** means it changes in a predictable corresponding way. For a transform $g$:

$$
f(gx)=f(x)\quad\text{(invariance)},\qquad
f(gx)=\rho(g)f(x)\quad\text{(equivariance)}.
$$

$\rho(g)$ describes the transformation in feature space. These equations specify properties to test; ordinary data augmentation does not guarantee them.

## Contrastive learning

A common contrastive objective makes related examples close and contrasts them with other examples:

$$
L_i=-\log
\frac{\exp(\operatorname{sim}(z_i,z_i^+)/T)}
{\sum_{j\in\mathcal C_i}\exp(\operatorname{sim}(z_i,z_j)/T)}.
$$

$z_i$ is an embedding, $z_i^+$ a positive match, $\mathcal C_i$ the candidate set including the positive, and $T>0$ the temperature. Defining the positive is a scientific assumption. Two nearby video frames may show the same object but different contact states that matter for control.

Masked prediction instead learns to infer missing portions of an input or representation. Predictive learning asks what representation helps predict future observations, rewards, or actions. Different objectives emphasize different information.

## Evaluate features through behavior

Use a simple probe to test whether embeddings contain object position or task-state information, but do not confuse probe performance with closed-loop control. Compare policies trained on frozen versus adapted features with matched data and compute.

For cross-embodiment transfer, ask whether features preserve task progress while reducing irrelevant robot appearance differences. [[Cross-Embodiment Transfer - 2607.27549]] provides a reading lead. Do not assume a visually appealing t-SNE or UMAP plot proves transfer.

**Exercise:** is rotation invariance always desirable for grasping?

> [!success]- Answer
> No. Object orientation may determine the correct gripper pose. Equivariance or an explicit orientation representation may be more appropriate.

Primary reading for a contrastive formulation: [SimCLR](https://arxiv.org/abs/2002.05709). Further concepts connect to [[Autoencoders]] and [[Unsupervised Learning]] in your course notes.
