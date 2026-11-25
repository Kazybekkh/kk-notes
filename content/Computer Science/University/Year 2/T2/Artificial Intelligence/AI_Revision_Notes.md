# Artificial Intelligence & Applications — Comprehensive Revision Notes

---

## Topic 1: Data Exploration and Visualisation

### Why Data Visualisation?

Summary statistics alone can be misleading — datasets with **identical** summary statistics (mean, standard deviation, correlation) can have completely different distributions. This was demonstrated by Anscombe's Quartet (1973) and the Datasaurus Dozen.

**Key principle:** Always produce both calculations and graphs. Each contributes to understanding.

### Purposes of Visualisation

Data visualisation is a critical tool in AI for identifying summaries, structure, relationships, differences, and abnormalities in data. It communicates complex information effectively.

### Chart Types by Purpose

| Purpose | Chart Types |
|---|---|
| **Relationship** | Scatter plots, bubble charts |
| **Composition** | Pie charts, stacked bar charts |
| **Connection** | Network graphs |
| **Location** | Maps, geographic plots |
| **Comparison** | Bar charts, grouped bar charts |

### Grammar of Graphics

The grammar of graphics is a systematic framework for building plots from components. Learning the grammar helps you think about new graphics beyond pre-existing templates.

**Core components:**

| Component | Role |
|---|---|
| **Data** | The dataset being visualised |
| **Aesthetics** | Mapping variables to visual properties (x, y, colour, shape, size) |
| **Geometries** | The visual marks (points, lines, bars) |
| **Facets** | Subplots for subsets of data |
| **Statistics** | Statistical transformations (smoothing, binning) |
| **Coordinates** | The coordinate system (Cartesian, polar) |
| **Theme** | Non-data visual styling |

### Data Preparation (Data Wrangling)

**Data quality issues to address:**

- **Missing values** — remove or impute
- **Duplicate records** — merge
- **Invalid values** — generate best estimate
- **Noise** — filter or smooth
- **Outliers** — detect and handle

**Feature engineering:**

- **Feature selection** — remove highly correlated features, features with many missing values, irrelevant features (IDs, row numbers)
- **Combining features** — create new informative features
- **Feature transformation** — mapping values to a new representation to make analysis easier (e.g., scaling, normalisation)

---

## Topic 2: Supervised Learning

### What is Machine Learning?

Machine learning is a set of methods that can automatically detect patterns in data. These patterns are then used to predict future data or perform decision-making under uncertainty.

### The Learning Problem

We have a set of training data:

$$\{(X_1, Y_1), (X_2, Y_2), \ldots, (X_n, Y_n)\}$$

We use this data and an ML method to estimate a function $f$ such that $f(X) = Y$.

The relationship is modelled as:

$$Y_i = f(\mathbf{X}_i) + \varepsilon_i$$

where $f$ is an unknown function and $\varepsilon$ is a random error (noise) term.

**Terminology:**

| Term | Also called |
|---|---|
| Input $X$ | Feature, attribute, predictor, independent variable |
| Output $Y$ | Response, dependent variable, label, ground truth |

### Regression vs Classification

| | Regression | Classification |
|---|---|---|
| **Output type** | Continuous (quantitative) | Categorical (qualitative) |
| **Example** | Predicting house price | Spam or not spam? |

### Linear Regression

The model: $\text{Price} = b_0 + b_1 \times \text{Size}$

- $b_0$ = constant (y-intercept)
- $b_1$ = coefficient / slope

**Least Squares Error** — the "best fit" minimises the sum of squared differences between actual and predicted values:

$$\hat{\varepsilon} = \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2$$

This is minimised using **gradient descent**.

**Strengths:** Simple, interpretable, computationally efficient, works well for linearly separable data.

**Limitations:** Assumes linearity, sensitive to outliers, struggles with multicollinearity, poor with complex non-linear data.

### Decision Trees

A decision tree partitions data recursively based on attribute values:

1. Determine the best attribute to select as root (using a goodness measure)
2. Partition examples into subsets according to values of that attribute
3. Construct the tree recursively for each subset
4. Exit when all examples belong to one class

**Attribute Selection — Information Gain:**

Entropy measures impurity:

$$\text{Entropy}(S) = -\sum_{c} p_c \log_2(p_c)$$

where $p_c$ is the proportion of class $c$ in set $S$.

Entropy after splitting on attribute $T$:

$$\text{Entropy}(S, T) = \sum_{v \in \text{values}(T)} \frac{|S_v|}{|S|} \cdot \text{Entropy}(S_v)$$

Information Gain:

$$\text{Gain}(S, T) = \text{Entropy}(S) - \text{Entropy}(S, T)$$

The attribute with the **highest information gain** is chosen as the split.

**Example (Play Tennis):**

| Attribute | Entropy after split | Information Gain |
|---|---|---|
| Outlook | 0.693 | **0.247** (highest) |
| Temperature | 0.911 | 0.029 |
| Humidity | 0.788 | 0.152 |
| Windy | 0.892 | 0.048 |

So **Outlook** is chosen as the root node.

**Strengths:** Easy to visualise and interpret, handles non-linear relationships, no need for data normalisation, handles categorical and continuous data.

**Limitations:** Prone to overfitting (without pruning), sensitive to small data changes.

### Random Forest (Ensemble Classification)

Random Forest combines multiple decision trees to reduce overfitting:

1. **Bootstrapping** — train each tree on a random subset of data with replacement
2. **Feature subsampling** — use a random subset of features at each split
3. **Tree building** — grow individual trees independently
4. **Aggregation** — combine results using majority vote (classification) or averaging (regression)

**Strengths:** Reduces overfitting, handles high-dimensional data.

**Limitations:** Less interpretable, computationally intensive, requires hyperparameter tuning.

### K-Nearest Neighbours (KNN)

A **lazy learning** approach — no model is built; the entire dataset is retained.

**Algorithm:**

1. User inputs $k$ (number of neighbours)
2. For each unlabelled instance, calculate the distance to all training instances
3. Find the $k$ nearest neighbours
4. **Classification:** majority vote among $k$ neighbours
5. **Regression:** average of the target values:

$$y_{\text{pred}} = \frac{1}{K} \sum_{k=1}^{K} y_i$$

**Distance metrics:**

- **Euclidean:** $d(p, q) = \sqrt{\sum_{i=1}^{n}(p_i - q_i)^2}$
- **Manhattan:** $d(p, q) = \sum_{i=1}^{n} |p_i - q_i|$

**Strengths:** Simple, no assumptions about distribution, effective for non-linear problems.

**Limitations:** Computationally expensive at prediction time, performance depends on choice of $k$ and distance metric, sensitive to irrelevant/noisy features.

---

## Topic 3: Unsupervised Learning

### Clustering

Clustering is a type of unsupervised learning that groups similar objects together. The training data contains **no output labels**.

**Goals:** data reduction, outlier detection, missing value imputation, pattern discovery.

**Key principle:** maximise within-cluster similarity, minimise between-cluster similarity.

**Similarity measures** (same as KNN):

- Euclidean distance
- Manhattan distance

### Cluster Quality Measures

- **Cluster centre** — for numeric data, the centre of mass (mean); for nominal data, the mode
- **Within-cluster variation (wc)** — how compact/tight clusters are
- **Between-cluster variation (bc)** — distances between different clusters

### K-Means Algorithm

1. Define the number of clusters $k$
2. Choose $k$ data objects randomly as initial centroids
3. Assign each data object to its nearest centroid
4. Recalculate the centroid of each cluster as the mean of its members
5. Repeat steps 3–4 until cluster membership no longer changes

**Finding optimal $k$ — Elbow Method:**

Plot within-cluster sum of squares (WCSS) against $k$. The "elbow" point where adding more clusters no longer significantly reduces WCSS is the optimal $k$.

$$\text{WCSS}(C) = \sum_{\text{cluster}} \sum_{x \in \text{cluster}} \|x - \mu\|^{2}$$

**Strengths:** Simple, efficient.

**Weaknesses:** Must specify $k$ in advance, sensitive to initialisation, sensitive to noise, struggles with non-globular cluster shapes.

### Agglomerative (Hierarchical) Clustering

A bottom-up approach — no need to specify $k$ beforehand.

**Algorithm:**

1. Treat all $n$ data objects as individual clusters; build an $n \times n$ dissimilarity matrix
2. While number of clusters > 1:
   - Find the pair with minimum distance
   - Merge them into a bigger cluster
   - Update the distance matrix
3. Produces a **dendrogram**

**Measuring distance between clusters:**

| Method | Description |
|---|---|
| **Single link** | Distance between the two closest points |
| **Complete link** | Distance between the two furthest points |
| **Centroid** | Distance between cluster centroids |
| **Group average** | Average of all pairwise distances |

**Strengths:** Deterministic, multiple clustering versions, no need to specify $k$, can create arbitrary cluster shapes.

**Weaknesses:** Does not scale well to large datasets.

---

## Topic 4: Deep Learning and Fully Connected Networks (FCNs)

### Machine Learning vs Deep Learning

| Traditional ML | Deep Learning |
|---|---|
| Raw data → hand-crafted features → classifier | Raw data → learned representations → classifier |
| Requires domain expertise for feature extraction | Features learned automatically from data |
| Shallow representations | Multiple layers of increasingly meaningful representations |

### Biological Inspiration

Neural networks are inspired by the human visual cortex (V1 → V2 → V3 etc.), which performs progressively more complex processing. The basic element in an artificial neural network is the **artificial neuron (node/unit)**.

### Fully Connected Network (FCN) Architecture

A fully connected network has:

- **Input vector:** $\{x_1, x_2, \ldots, x_n\}$
- **Hidden values:** $\{h_1, \ldots, h_m\}$
- **Output value:** $y$

The forward computation:

$$\text{output} = f(\mathbf{W} \cdot \mathbf{input} + \mathbf{b})$$

Without an activation function, this is purely linear. The activation function $f$ introduces **non-linearity**.

### One-Hot Encoding (OHE)

For multi-class classification, class labels are converted to binary vectors:

| Label | OHE Vector |
|---|---|
| 0 (zero) | $[1,0,0,0,0,0,0,0,0,0]$ |
| 3 (three) | $[0,0,0,1,0,0,0,0,0,0]$ |
| 6 (six) | $[0,0,0,0,0,0,1,0,0,0]$ |

### Key Hyperparameters

| Hyperparameter | Description |
|---|---|
| **Epochs** | Number of times the entire training set passes through the network |
| **Batch size** | Number of samples per gradient update |
| **Learning rate** | Scalar that controls the step size of weight updates |
| **Number of hidden units** | Width of each hidden layer |

---

## Topic 5: Activation Functions in FCNs

### Why Activation Functions?

Without non-linearity, no matter how many layers, the entire network collapses to a single linear function. Activation functions:

- Allow backpropagation (derivative is related to input)
- Enable stacking of multiple layers (non-linear combination)

### Activation Functions Summary

| Function | Formula | Range | Pros | Cons |
|---|---|---|---|---|
| **Linear** | $f(x) = x$ | $(-\infty, +\infty)$ | Simple | Cannot learn non-linear patterns |
| **Sigmoid** | $\sigma(x) = \frac{1}{1+e^{-x}}$ | $(0, 1)$ | Smooth, probabilistic output | **Vanishing gradient** for $\|x\| > 3$ |
| **Tanh** | $\tanh(x) = \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}$ | $(-1, 1)$ | Zero-centred, steeper than sigmoid | Vanishing gradient for $\|x\| > 3$ |
| **ReLU** | $f(x) = \max(0, x)$ | $[0, +\infty)$ | Fast, avoids vanishing gradient | **Dying ReLU** (neurons output 0 permanently) |
| **Leaky ReLU** | $f(x) = \max(\alpha x, x)$ | $(-\infty, +\infty)$ | Fixes dying ReLU | Small negative slope $\alpha$ is a hyperparameter |
| **Softmax** | $\sigma(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}$ | $(0, 1)$, sums to 1 | Outputs probabilities | Used only in output layer for multi-class |

### When to Use Which

- **Hidden layers:** ReLU (default), Leaky ReLU if dying neurons are an issue
- **Binary classification output:** Sigmoid
- **Multi-class classification output:** Softmax
- **Regression output:** Linear (no activation)

---

## Topic 6: Loss Functions, Forward and Backpropagation

### Loss Functions

The loss function measures how badly the AI system performed:

$$\ell(\vec{y}_{i}, \vec{y}_i^{\ast}) = \text{a "badness" score}$$

The total loss over the training set:

$$\mathcal{L} = \frac{1}{n} \sum_{i=1}^{n} \ell(\vec{y}_{i}, \vec{y}_i^{\ast})$$

### Binary Cross-Entropy (BCE)

For binary classification (output via sigmoid):

$$\ell_{BCE}(\vec{y}_{i}, \vec{y}_i^{\ast}) = -y_i \log(y_i^{\ast}) - (1 - y_i) \log(1 - y_i^{\ast})$$

$$\mathcal{L}_{BCE} = \frac{1}{n} \sum_{i=1}^{n} \ell_{BCE}(\vec{y}_{i}, \vec{y}_i^{\ast})$$

### Categorical Cross-Entropy (CCE)

For multi-class classification (output via softmax):

$$\ell_{CE}(\vec{y}_{i}, \vec{y}_i^{\ast}) = -\sum_{c=1}^{V} y_{ci} \log(y_{ci}^{\ast})$$

$$\mathcal{L}_{CE} = \frac{1}{n} \sum_{i=1}^{n} \ell_{CE}(\vec{y}_{i}, \vec{y}_i^{\ast})$$

### Mean Squared Error (MSE)

For regression:

$$\ell_{MSE}(\vec{y}_{i}, \vec{y}_{i}^{\ast}) = \frac{1}{V} \sum_{c=1}^{V} (y_{ci} - y_{ci}^{\ast})^2$$

$$\mathcal{L}_{MSE} = \frac{1}{n} \sum_{i=1}^{n} \ell_{MSE}(\vec{y}_{i}, \vec{y}_{i}^{\ast})$$

### Summary: Loss + Output Activation Pairing

| Task | Output Activation | Loss Function |
|---|---|---|
| Binary classification | Sigmoid | Binary cross-entropy |
| Multi-class classification | Softmax | Categorical cross-entropy |
| Regression | Linear (none) | Mean squared error |

### Gradient Descent and Backpropagation

**Gradient** — indicates the direction and rate of steepest ascent of the error function. To minimise the loss, we move in the **opposite direction** of the gradient.

**Backpropagation** computes the gradient of the loss with respect to each weight using the **chain rule**.

**Weight update rule:**

$$W \leftarrow W - \alpha \cdot \nabla_W \mathcal{L}$$

where $\alpha$ is the learning rate.

### SGD vs Mini-Batch SGD

| | SGD | Mini-Batch SGD |
|---|---|---|
| **Samples per update** | 1 random sample | A batch of samples |
| **Gradient estimate** | Noisy | Smoother |
| **Speed** | Fast per step | More stable convergence |

**Training loop:** Input → Predict → Error → Backprop → Update → Repeat

### Dropout (Regularisation)

Dropout randomly drops (zeroes out) some neuron outputs during training with probability $p$. This prevents overfitting by making the model less sensitive to noise and more generic.

```python
model.add(Dropout(0.3))  # 30% dropout probability
```

### Optimisers

| Optimiser | Description |
|---|---|
| **SGD** | Basic stochastic gradient descent |
| **RMSprop** | Adapts learning rate per parameter |
| **Adam** | Combines momentum and adaptive learning rates; often the default choice |

---

## Topic 7: Evaluating ML/DL Models

### Model Validation Strategies

**Goal:** avoid overfitting and find the best hyperparameter combination.

#### Holdout

Split data into three sets:

| Set | Purpose | Typical Split |
|---|---|---|
| Training | Learn model parameters | 60% |
| Validation | Tune hyperparameters, detect overfitting | 20% |
| Test | Final evaluation on unseen data | 20% |

#### K-Fold Cross-Validation

1. Split dataset into $k$ subsets (folds)
2. For each fold: train on $k-1$ folds, validate on the remaining fold
3. Average results across all $k$ runs

### Overfitting vs Underfitting

| | Underfitting | Good Fit | Overfitting |
|---|---|---|---|
| **Training error** | High | Low | Very low |
| **Validation error** | High | Low | High |
| **Model complexity** | Too simple | Just right | Too complex |

**Solutions to overfitting:**

- Early stopping — stop training when validation loss starts increasing
- Regularisation (L2): adds $\lambda \sum w_{i}^2$ penalty to loss
- Dropout
- More training data

### Hyperparameter Optimisation

| Method | Description | Pros | Cons |
|---|---|---|---|
| **Grid Search** | Exhaustive search over all combinations | Systematic, thorough | Expensive for large spaces |
| **Random Search** | Random sampling from distributions | More efficient in high dimensions | No guarantee of finding best |

### Classification Metrics

**Confusion Matrix:**

|  | Predicted Positive | Predicted Negative |
|---|---|---|
| **Actual Positive** | True Positive (TP) | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN) |

**Key metrics:**

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

$$\text{Precision} = \frac{TP}{TP + FP}$$

$$\text{Recall} = \frac{TP}{TP + FN}$$

$$\text{F1-Score} = 2 \cdot \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

**Why accuracy alone is not enough:** In imbalanced datasets (e.g., 91 benign vs 9 malignant tumours), a model that always predicts "benign" achieves 91% accuracy but is useless. Use precision, recall, and F1-score instead.

**AUC-ROC:** Area Under the Receiver Operating Characteristic Curve — measures the model's ability to distinguish between classes across all thresholds.

---

## Topic 8: Convolutional Neural Networks (CNNs)

### Why CNNs?

FCNs treat input as flat vectors, losing **spatial locality** — the relationship between neighbouring pixels. CNNs are designed to preserve and exploit spatial structure.

### CNN Architecture Components

#### 1. Convolutional Layer

A **kernel (filter)** slides over the image, performing element-wise multiplication and summation to produce a **feature map**.

**Key parameters:**

- **Kernel size** — e.g., $3 \times 3$, $5 \times 5$
- **Stride** — step size of the filter movement
- **Padding:**
  - `valid` — no padding, output smaller than input
  - `same` — zero-padding, output same size as input

**Output feature map size:**

$$\text{Output size} = \frac{\text{Input size} - \text{Kernel size} + 2 \times \text{Padding}}{\text{Stride}} + 1$$

**Important:** The filter must have the **same number of channels** as the input (e.g., a $3 \times 3$ filter on an RGB image is actually $3 \times 3 \times 3$).

**Number of learnable parameters in a conv layer:**

$$\text{Params} = \text{kernel height} \times \text{kernel width} \times \text{input channels} \times \text{output channels}$$

#### 2. Pooling Layer

Reduces spatial dimensions while retaining key information. **Max Pooling** takes the maximum value in each pooling window.

```python
MaxPooling2D(pool_size=(2, 2), strides=(2, 2))
```

#### 3. Fully Connected (Classification) Layer

After feature extraction through conv and pooling layers, the feature maps are **flattened** into a 1D vector and fed to dense layers for classification.

### Example: Parameter Calculation

For a 32×32 input image (no padding, stride=1):

| Layer | Config | Output Shape | Parameters |
|---|---|---|---|
| Conv1 | 3×3, 16 filters | 30×30×16 | $3 \times 3 \times 1 \times 16 = 144$ |
| Conv2 | 3×3, 32 filters | 28×28×32 | $3 \times 3 \times 16 \times 32 = 4{,}608$ |
| FC | 10 outputs | 10 | $25{,}088 \times 10 = 250{,}880$ |
| **Total** | | | **255,632** |

Pooling layers help **reduce** the number of parameters in subsequent FC layers.

### LeNet Architecture

A classic CNN for handwritten digit recognition (MNIST):

```
Input (28×28×1)
→ Conv2D(20, kernel=5, valid) → ReLU → MaxPool(2×2)
→ Conv2D(50, kernel=5, valid) → ReLU → MaxPool(2×2)
→ Flatten → Dense(500) → ReLU
→ Dense(10) → Softmax
```

---

## Topic 9: CNNs Part II — Improving Generalisability

### Techniques for Better CNNs

#### Spatial Dropout

Like standard dropout but drops entire feature maps in convolutional layers rather than individual neurons.

#### Batch Normalisation

Normalises the output of each layer within a mini-batch to stabilise training.

**Why it helps:**

- Prevents vanishing/exploding gradients
- Reduces sensitivity to weight initialisation
- Acts as a slight regulariser

**Formula:**

1. **Normalise within mini-batch:**

$$\hat{x}_i = \frac{x_i - \mu_{B}}{\sqrt{\sigma_{B}^{2} + \epsilon}}$$

where $\mu_{B}$ and $\sigma_{B}^{2}$ are the batch mean and variance.

2. **Scale and shift (learnable parameters):**

$$y_i = \gamma \hat{x}_i + \beta$$

where $\gamma$ (scale) and $\beta$ (shift) are learned during training.

**Placement:** Typically after the convolutional/dense layer and before the activation function:

```
Conv2D → BatchNormalization → ReLU
```

---

## Topic 10: Transfer Learning and Pre-trained CNNs

### What is a Pre-trained Model?

A saved network previously trained on a large dataset (e.g., ImageNet with 1.4M images, 1000 classes). Useful when you have a **small dataset** — improves accuracy and saves training time.

**Examples:** VGG-16, GoogLeNet/Inception, ResNet, MobileNet, BERT, GPT.

### Using a Pre-trained Model

#### Feature Extraction (Shallow Mode)

1. Load pre-trained convolutional base **without** the top classifier
2. **Freeze** all convolutional layers (`trainable = False`)
3. Add new custom dense layers on top for your specific task
4. Train only the new dense layers

**Why not reuse the classifier?** The original classifier was trained for 1000 ImageNet classes — not your task.

#### Fine-Tuning (Deep Mode)

Two approaches:

1. **Full fine-tuning:** Set entire model as trainable (`conv_base.trainable = True`), train end-to-end with a low learning rate
2. **Partial fine-tuning:** Freeze early layers, only unfreeze later layers (e.g., from `block5_conv1` onwards)

**Rationale:** Early layers learn generic features (edges, textures) transferable across tasks. Later layers learn task-specific features.

---

## Topic 11: Handling Class Imbalance

### The Problem

When one class vastly outnumbers another (e.g., 998 negatives vs 2 positives), classifiers become biased toward the majority class. A model predicting "always negative" achieves 99.8% accuracy but is useless.

The standard cross-entropy loss is dominated by the majority class gradients.

### Algorithm-Level Solutions

#### Weighted Cross-Entropy

Assign higher weights to minority classes in the loss function:

**Weighted BCE:**

$$\ell = -w_{1} \cdot y \log(y^{\ast}) - w_{0} \cdot (1-y) \log(1-y^{\ast})$$

```python
class_weights = {0: 1.0, 1: 5.0}  # higher weight for minority
model.fit(..., class_weight=class_weights)
```

#### Focal Loss

Reduces the influence of easy (majority) samples and focuses training on hard (minority) samples. Adds a modulating factor $(1 - p_{t})^\gamma$ to cross-entropy.

### Data-Level Solutions

| Technique | Description | Risk |
|---|---|---|
| **Random oversampling** | Duplicate minority samples | Overfitting |
| **Random undersampling** | Remove majority samples | Loss of information |
| **Data augmentation** | Apply transformations (rotation, flip, shift, zoom, shear) | Requires careful tuning |
| **SMOTE** | Synthetically generate minority samples by interpolating between nearest neighbours | Only for structured/tabular data |

### SMOTE (Synthetic Minority Over-sampling Technique)

1. Select a minority class instance
2. Find its $k$-nearest neighbours (from minority class)
3. Create a synthetic sample by interpolating:

$$x_{\text{new}} = x_i + \lambda \cdot (x_{\text{neighbour}} - x_i)$$

where $\lambda \in [0, 1]$ is random.

**Critical rule:** Perform oversampling/augmentation **only on training data**, never on the test set.

### Performance Metrics for Imbalanced Data

Use **precision, recall, and F1-score** rather than accuracy alone.

---

## Topic 12: Autoencoders

### The Curse of Dimensionality

As the number of features increases without increasing training samples, the feature space becomes sparse. Distance metrics lose meaning, and models overfit easily.

**Solution:** Dimensionality reduction.

### What is an Autoencoder?

An unsupervised neural network that learns a compressed representation of input data and then reconstructs it.

**Components:**

| Component | Role |
|---|---|
| **Encoder** | Compresses input into lower-dimensional latent space |
| **Latent space (code)** | Compressed representation |
| **Decoder** | Reconstructs input from latent representation |

**Loss function (MSE):**

$$\mathcal{L}_{MSE} = \frac{1}{n} \sum_{i=1}^{n} \sum_{j=1}^{d} (x_{ij} - \hat{x}_{ij})^2$$

**Key idea:** The network is trained to reproduce its own input ($x \to \hat{x}$), forcing the latent space to capture essential features.

### Types of Autoencoders

#### 1. Vanilla Autoencoder

Fully connected layers. Input → Encoder (Dense) → Latent code → Decoder (Dense) → Reconstructed output.

#### 2. Denoising Autoencoder

Input is a **noisy** version of the data; the network learns to reconstruct the **clean** version. This improves robustness.

#### 3. Convolutional Autoencoder (CAE)

Uses Conv2D layers in the encoder and either **UpSampling2D** (fixed) or **Conv2DTranspose** (learnable) in the decoder.

**Encoder:** Conv2D + MaxPooling (downsample)
**Decoder:** Conv2D + UpSampling/Conv2DTranspose (upsample)

### Applications

- **Denoising** — remove noise/artefacts from images
- **Image colourisation** — convert grayscale to colour
- **Dimensionality reduction** — alternative to PCA
- **Anomaly detection** — high reconstruction error = anomaly

---

## Topic 13: Object Detection and Segmentation

### Computer Vision Task Hierarchy

| Level | Task | Output |
|---|---|---|
| **Classification** | What is in the image? | Class label |
| **Object Detection** | Where are the objects? | Bounding boxes + labels |
| **Semantic Segmentation** | Pixel-wise classification | Class label per pixel |
| **Instance Segmentation** | Pixel-wise + distinguish instances | Mask per object instance |

### R-CNN (Region-based CNN)

1. Generate ~2000 region proposals using **Selective Search**
2. Warp each region to fixed size
3. Extract features using a CNN (e.g., AlexNet)
4. Classify each region with an SVM
5. Refine bounding boxes with regression

**Cons:** Very slow — requires ~2000 CNN forward passes per image.

### Fast R-CNN

**Key improvement:** Run the CNN only **once** per image to produce a shared feature map.

1. Generate region proposals with Selective Search
2. Run entire image through CNN → feature map
3. For each proposal, extract features via **RoI (Region of Interest) Pooling**
4. Classify and refine bounding boxes in one unified network

**Con:** Still uses slow Selective Search for proposals.

### Faster R-CNN

Replaces Selective Search with a **Region Proposal Network (RPN)** — a small CNN that generates proposals from the feature map itself.

**Architecture:**

1. Backbone CNN → shared feature map
2. **RPN** → generates proposals from the feature map
3. **RoI Pooling** → extracts fixed-size features for each proposal
4. **Classification head** → classifies and refines boxes

Everything is end-to-end trainable.

### U-Net (Semantic Segmentation)

An encoder-decoder architecture with **skip connections** between corresponding encoder and decoder layers.

- **Encoder (downsampling path):** extracts context using Conv + MaxPool
- **Decoder (upsampling path):** restores spatial resolution
- **Skip connections:** combine location information from the encoder with context from the decoder

**Advantages:** No dense layers (input can be any size), combines localisation and context.

### Mask R-CNN (Instance Segmentation)

Extends Faster R-CNN by adding a **mask branch** that outputs a binary segmentation mask for each detected object, providing pixel-level segmentation alongside bounding boxes and class labels.

---

## Topic 14: Natural Language Processing (NLP)

### NLP vs LLMs

- **NLP** — the broader field of techniques for analysing human language (includes statistical models like N-gram, TF-IDF, BoW)
- **LLMs** — a specific type of deep learning model within NLP, trained on massive datasets (e.g., GPT, BERT)

### Levels of Linguistic Analysis

- **Syntax** — what is grammatically correct
- **Semantics** — what is the meaning

### Ambiguity Types

| Type | Description | Example |
|---|---|---|
| **Lexical** | Words with multiple meanings | "bank" (financial vs river) |
| **Semantic** | Sentences with multiple meanings | "I saw him with a telescope" |
| **Anaphoric** | Pronouns referring to earlier mentions | "He told his dog to sit, and it did" |

### NLP Pipeline

1. **Sentence segmentation** — split text into sentences
2. **Tokenisation** — split sentences into words/tokens
3. **Stemming** — crude chopping of word endings (e.g., "eating" → "eat")
4. **Lemmatisation** — proper reduction using vocabulary (e.g., "better" → "good", "drove" → "drive")
5. **Stop word removal** — remove common words ("the", "a", "is")
6. **POS tagging** — assign part of speech (noun, verb, adjective, etc.)
7. **Named Entity Recognition** — identify persons, locations, times

### Bag of Words (BoW)

Represents a document as a vector of word frequencies. Ignores word order entirely.

**Process:**

1. Build a vocabulary of known words
2. For each document, count occurrences of each vocabulary word
3. Resulting vector represents the document

### TF-IDF (Term Frequency — Inverse Document Frequency)

Measures importance of a word to a document within a corpus.

$$\text{TF}(t, d) = \frac{\text{count of } t \text{ in } d}{\text{total words in } d}$$

$$\text{IDF}(t) = \log\left(\frac{\text{total documents}}{\text{documents containing } t}\right)$$

$$\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t)$$

Words that appear frequently in one document but rarely across the corpus get **high** TF-IDF scores.

### Cosine Similarity

Measures similarity between two document vectors:

$$\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$

### N-gram Language Models

Uses the probabilities of word sequences to predict the next word.

**Markov assumption:** the probability of a word depends only on the previous $N-1$ words:

$$P(W_n | W_1 \ldots W_{n-1}) \approx P(W_n | W_{n-N+1} \ldots W_{n-1})$$

**MLE for conditional probabilities:**

$$P(W_n | W_1 \ldots W_{n-1}) = \frac{C(W_1 \ldots W_n)}{C(W_1 \ldots W_{n-1})}$$

**Types:**

- **Unigram:** $P(\text{dog})$
- **Bigram:** $P(\text{dog} | \text{big})$
- **Trigram:** $P(\text{dog} | \text{the, big})$

**Limitations:** Computationally expensive for large $N$; gives zero probability to unseen sequences (sparsity).

---

## Topic 15: Regression and Text Classification with FCNs

### Regression with Deep Learning

For regression tasks, the output $y$ is continuous.

**Key differences from classification:**

| | Classification | Regression |
|---|---|---|
| **Output activation** | Softmax / Sigmoid | Linear (none) |
| **Loss function** | Cross-entropy | MSE |
| **Output units** | Number of classes | 1 (or number of target values) |

### Data Normalisation for Regression

When features have different scales, normalisation is essential:

**Min-Max Scaling:**

$$X_{\text{scaled}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$$

**Z-Score (Standardisation):**

$$X_{\text{standard}} = \frac{X - \mu}{\sigma}$$

**Important:** Compute normalisation statistics ($\mu$, $\sigma$, min, max) on the **training set only**, then apply to test set.

### Text Classification with FCNs

**Approach (e.g., IMDB sentiment analysis):**

1. Load pre-processed text data (each review = list of word indices)
2. **One-hot encode** the word sequences into fixed-size binary vectors (dimension = vocabulary size)
3. Build an FCN with Dense layers and appropriate activation

**Binary classification (IMDB):**

```
Dense(16, relu) → Dense(16, relu) → Dense(1, sigmoid)
Loss: binary_{c}rossentropy
```

**Multi-class classification (Reuters, 46 topics):**

```
Dense(64, relu) → Dense(64, relu) → Dense(46, softmax)
Loss: categorical_crossentropy
```

---

## Topic 16: Recurrent Neural Networks (RNNs)

### Why RNNs?

FCNs treat input as flat vectors — they discard **sequential information**. Word order matters in NLP: "not bad" ≠ "bad".

### RNN Architecture

An RNN processes sequences **one element at a time**, maintaining a **hidden state** that acts as memory.

At each time step $t$:

- Input: $x(t)$
- Hidden state: $h(t) = f(W \cdot h(t-1) + U \cdot x(t))$
- Output: $y(t) = V \cdot h(t)$

The **same weights** ($U$, $V$, $W$) are shared across all time steps.

### Backpropagation Through Time (BPTT)

The RNN is "unrolled" across time steps, and gradients are computed backwards through all steps. This is how RNNs learn temporal dependencies.

### Padding Sequences

Since neural networks expect fixed-size inputs, sequences of different lengths are **padded** (typically with zeros) to the same length:

```
[1, 2, 3]    → [0, 1, 2, 3]
[4, 5]       → [0, 0, 4, 5]
[6, 7, 8, 9] → [6, 7, 8, 9]
```

### Word Embeddings

Instead of sparse one-hot vectors, word embeddings map each word to a **dense vector** where similar words have similar representations.

**Embedding layer:**

```python
Embedding(vocab_size, embedding_dim, input_length=max_len)
```

- `vocab_size` — number of distinct words
- `embedding_dim` — size of each embedding vector
- `input_length` — length of input sequences

### Word2Vec

A method for learning word embeddings from context:

- **CBOW (Continuous Bag of Words):** predicts target word from context words
- **Skip-gram:** predicts context words from target word

### RNN for Text Classification (IMDB)

```
Embedding(10000, 300, input_length=200)
→ SimpleRNN(32)
→ Dense(1, sigmoid)
```

The final hidden state $h_T$ summarises the entire input sequence into a fixed-size vector for classification.

**Stacking RNNs:** Use `return_sequences=True` for intermediate RNN layers to pass full sequence to the next RNN layer.

### RNN for Word Prediction

```
Embedding(vocab_size, embedding_dim, input_length=max_len)
→ SimpleRNN(hidden_units)
→ Dense(vocab_size, softmax)
```

Output: probability distribution over entire vocabulary for the next word.

### LSTM (Long Short-Term Memory)

Standard RNNs suffer from the **vanishing gradient problem** — gradients decay exponentially over long sequences, making it hard to learn long-term dependencies.

LSTMs solve this with a **memory cell** and **gates**:

| Gate | Function |
|---|---|
| **Forget gate** | Decides what to discard from memory |
| **Input gate** | Decides what new information to store |
| **Output gate** | Decides what to output from memory |

---

## Topic 17: Actionability in AI — Search Algorithms

### Search Problem Definition

| Component | Description |
|---|---|
| **Initial state** | Starting point |
| **State space** | All reachable states |
| **Actions** | Operations available at each state |
| **Goal state** | Desired endpoint |
| **Goal test** | Check if current state is the goal |
| **Path cost** | Cost associated with a path |

### Search Algorithm Properties

| Property | Description |
|---|---|
| **Completeness** | Will it find a solution if one exists? |
| **Optimality** | Will it find the best (lowest-cost) solution? |
| **Time complexity** | How long does it take? |
| **Space complexity** | How much memory does it need? |

### Uninformed (Blind) Search

#### Breadth-First Search (BFS)

Explores all neighbours at the current depth before moving deeper. Uses a **queue** (FIFO).

| Property | BFS |
|---|---|
| Complete | Yes |
| Optimal | Yes (if all actions have equal cost) |
| Strategy | Shallowest node first |

#### Depth-First Search (DFS)

Explores as deep as possible along one branch before backtracking. Uses a **stack** (LIFO).

| Property | DFS |
|---|---|
| Complete | No (can get stuck in infinite loops) |
| Optimal | No |
| Strategy | Deepest node first |

#### Uniform Cost Search (UCS)

Expands the node with the **lowest cumulative path cost**. Uses a **priority queue**.

$$\text{cost}(\text{node}) = \text{cumulative cost from root}$$

| Property | UCS |
|---|---|
| Complete | Yes |
| Optimal | Yes |

### Informed Search

Uses a **heuristic function** $h(x)$ — an estimate of the distance from node $x$ to the goal.

#### Greedy Search

Expands the node with the **lowest heuristic value** $h(x)$.

| Property | Greedy |
|---|---|
| Complete | No |
| Optimal | No |
| Strategy | Closest to goal (by heuristic) |

#### A* Search

Combines UCS and Greedy. Evaluation function:

$$f(x) = g(x) + h(x)$$

where:
- $g(x)$ = backward cost (cumulative cost from start to $x$)
- $h(x)$ = forward cost (heuristic estimate from $x$ to goal)

Always expands the node with the **lowest** $f(x)$.

| Property | A* |
|---|---|
| Complete | Yes |
| Optimal | Yes (if $h(x)$ is admissible — never overestimates) |

### Search Algorithms Comparison

| Algorithm | Complete | Optimal | Uses Heuristic |
|---|---|---|---|
| BFS | Yes | Yes (equal costs) | No |
| DFS | No | No | No |
| UCS | Yes | Yes | No |
| Greedy | No | No | Yes |
| A* | Yes | Yes | Yes |

---

## Topic 18: Uncertainty Quantification and Explainability (XAI)

### Monte Carlo Dropout for Uncertainty

Deep learning models are typically "black boxes" — they give predictions but no confidence measure.

**MC Dropout method:**

1. Train the model with dropout as usual
2. At inference, keep dropout **active** (don't disable it)
3. Run **multiple forward passes** on the same input → different predictions each time
4. **Average** the predictions → final output
5. **Standard deviation** of the predictions → uncertainty estimate

High std = model is uncertain; Low std = model is confident.

### Explainable AI (XAI)

XAI aims to make AI decisions interpretable and understandable to humans.

### Grad-CAM (Gradient-weighted Class Activation Mapping)

Provides visual explanations for CNN decisions by highlighting important image regions.

**How it works:**

1. Take the **feature maps from the last convolutional layer**
2. Compute the **gradient of the predicted class** with respect to each feature map
3. Compute a **weighted sum** of feature maps using these gradients → produces a 2D heatmap
4. **Upsample** the heatmap to match the original image size
5. **Overlay** the heatmap on the original image

The result shows which regions contributed most to the prediction — warm colours indicate high importance.

---

*End of revision notes.*
