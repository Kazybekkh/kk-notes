---
type: appendix
status: not-started
tags: [robot-learning, deep-learning, transformers]
---
# Neural networks and attention

[[Home]] | [[05 Training Neural Policies]] | [[07 ACT and Action Sequences]] | [[13 Vision Language Action Models]]

## Start with a layer

A dense layer computes $h=\sigma(Wx+b)$. The matrix mixes input coordinates, the bias shifts them, and the nonlinear function $\sigma$ allows composition to represent more than a single linear map. Without nonlinearities, a stack of dense linear layers collapses to one linear transformation.

Training differentiates a scalar objective through these operations. A minibatch approximates a full-dataset gradient; stochasticity can make optimization efficient but produces noisy updates. Validation and deployment behavior, not architecture size, determine whether the representation is useful.

## Why attention is useful

A robot may need to combine an instruction token, an object image patch, and joint-state information. Attention lets a token retrieve weighted information from other tokens.

For $n$ tokens represented by $X\in\mathbb R^{n\times d_{\rm model}}$:

$$
Q=XW_Q,\quad K=XW_K,\quad V=XW_V,
\qquad
\operatorname{Attention}(Q,K,V)
=\operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V.
$$

$Q$ contains queries, $K$ keys, and $V$ values. For a single head with matching query/key dimension $d_k$, the score matrix is $n\times n$. Softmax operates across keys for each query. The scaling prevents dot-product magnitudes from growing unnecessarily with dimension under common assumptions.

With cross-attention, queries and key/value tokens can come from different sources. For example, action queries may attend to encoded camera and language features. Multi-head attention repeats the process with different learned projections and combines the results.

## Sequence order and visibility

Attention without positional information does not by itself know token order. Position encodings provide temporal or spatial structure. A causal mask prevents a token from attending to future tokens during autoregressive prediction. A robot sequence model's mask must reflect the intended information flow, or training can leak future observations.

![[appendix_attention_mask.mp4]]

*Six tokens that alternate observations and actions, with random embeddings and projections (the computation, not a trained model). The $6\times6$ score matrix becomes attention weights after a softmax across each row. Without a mask, the row for act 2 puts 37% of its weight on later tokens. The causal mask sets those weights to 0. Editing only obs 3 then changes act 2's output by 0.24 without the mask and by exactly 0 with it. Source: `Tools/animations/appendix_attention_mask.py`.*

Residual connections and normalization help train deep stacks. A feed-forward block transforms each token after attention. These details matter, but understanding the input/output shapes and visibility pattern should come first.

## Robot-specific traps

More tokens increase compute, and ordinary full attention has a quadratic token-pair matrix. High-resolution multi-camera histories can therefore become expensive. Reducing tokens changes what the robot can perceive; measure both runtime and failure modes.

An attention heatmap is a visualization of model weights, not by itself a causal explanation of the action. Interventions and ablations provide stronger evidence about which information matters.

**Exercise:** for 64 tokens and a head dimension of 32, what is the shape of $QK^\top$? Does doubling the number of tokens double its entries?

> [!success]- Answer
> The matrix is $64\times64$. Doubling to 128 tokens quadruples its entries.

Primary reference: [Attention Is All You Need](https://arxiv.org/abs/1706.03762). Connect to your existing [[Deep Learning and FCNs]] and [[Recurrent Neural Networks]].
