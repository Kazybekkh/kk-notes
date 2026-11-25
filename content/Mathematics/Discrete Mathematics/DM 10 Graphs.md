---
type: course-chapter
course: discrete-mathematics
chapter: 10
tags: [mathematics, discrete-mathematics, graphs]
---
# DM 10 Graphs

Previous: [[DM 09 Recurrences and Asymptotics]] | [[DM 00 Course Map]] | Next: [[DM 11 Trees and Graph Algorithms]]

> [!abstract] One sentence
> A graph is a set of objects with links between some pairs; it models any network, and breadth-first and depth-first search are the two basic ways to explore one.

## Definitions

A **graph** $G=(V,E)$ has a set of **vertices** (nodes) $V$ and a set of **edges** $E$, each edge joining two vertices.

- **Undirected**: edges have no direction. Friendship, road segments, bonds between atoms.
- **Directed** (digraph): each edge goes from one vertex to another. Web links, task dependencies, state transitions.
- **Weighted**: each edge carries a number such as distance, cost or time.
- **Simple**: no loops (edges from a vertex to itself) and no repeated edges. The default here.

**Terms.**

- $u$ and $v$ are **adjacent** if an edge joins them.
- The **degree** $\deg(v)$ is the number of edges at $v$. In a digraph, in-degree and out-degree are counted separately.
- A **path** is a sequence of vertices with each consecutive pair joined by an edge; its **length** is the number of edges.
- A **cycle** is a path that returns to its start without repeating edges or other vertices.
- A graph is **connected** if every pair of vertices is joined by some path. Its maximal connected pieces are its **components**.

**Running example.** $V=\{A,B,C,D,E\}$ and edges $AB, AC, BC, BD, DE$. Degrees: $A{:}2$, $B{:}3$, $C{:}2$, $D{:}2$, $E{:}1$. It is connected, and $A\text{-}B\text{-}C\text{-}A$ is a cycle.

## The handshake lemma

$$
\sum_{v\in V}\deg(v)=2|E|.
$$

Every edge has two ends and adds 1 to the degree of each. Check: $2+3+2+2+1=10=2\times5$.

**Corollary.** The number of odd-degree vertices is even. (The sum is even, so the odd terms must pair up.) For example, there is no group of 7 people in which everyone knows exactly 3 others: the degree sum would be 21, which is odd.

## Special graphs

| Graph | Description | Edges |
|---|---|---|
| complete $K_n$ | every pair joined | $\binom n2=n(n-1)/2$ |
| path $P_n$ | a line of $n$ vertices | $n-1$ |
| cycle $C_n$ | a ring of $n$ vertices | $n$ |
| bipartite | vertices split into two sides, edges only between sides | varies |
| tree | connected, no cycles | $n-1$ |
| grid | lattice of cells | about $2n$ |

A graph is **bipartite** exactly when it has no cycle of odd length. Matching workers to jobs, or users to items, are bipartite problems.

An occupancy grid for robot navigation is a graph: free cells are vertices, and neighbouring free cells are joined by edges.

## Representing a graph in a computer

**Adjacency matrix.** An $n\times n$ matrix with $A_{ij}=1$ if there is an edge from $i$ to $j$. For the running example (order $A,B,C,D,E$):

$$
A=\begin{bmatrix}0&1&1&0&0\\1&0&1&1&0\\1&1&0&0&0\\0&1&0&0&1\\0&0&0&1&0\end{bmatrix}.
$$

Symmetric for undirected graphs. Edge lookup in $O(1)$, but $\Theta(n^2)$ memory.

**Adjacency list.** For each vertex, the list of its neighbours:

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B"],
    "D": ["B", "E"],
    "E": ["D"],
}
```

Memory $\Theta(|V|+|E|)$. The right choice for **sparse** graphs, which is most real ones.

**Algebra bonus.** Entry $(i,j)$ of $A^k$ counts the walks of length $k$ from $i$ to $j$. Matrix multiplication sums over intermediate vertices ([[LA 03 Matrices as Linear Maps]]). The eigenvalues of graph matrices reveal clusters and connectivity, which is the basis of spectral clustering and graph neural networks.

## Breadth-first search (BFS)

Explore in layers: first the start, then all its neighbours, then their unvisited neighbours, and so on. Uses a **queue** (first in, first out).

```python
from collections import deque

def bfs(graph, start):
    dist = {start: 0}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in dist:          # not yet discovered
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist
```

**Trace from $A$.** Queue $[A]$. Pop $A$: discover $B,C$ at distance 1. Pop $B$: discover $D$ at distance 2 ($A$ and $C$ already seen). Pop $C$: nothing new. Pop $D$: discover $E$ at distance 3. Pop $E$: nothing new.

Result: $A{:}0$, $B{:}1$, $C{:}1$, $D{:}2$, $E{:}3$.

> [!important] BFS finds shortest paths in unweighted graphs
> Vertices are discovered in order of distance, so the first time a vertex is reached is by a shortest path. Record each vertex's parent to recover the path itself.

Running time $\Theta(|V|+|E|)$: each vertex is queued once and each edge is examined once from each end.

## Depth-first search (DFS)

Go as deep as possible along one branch, then backtrack. Uses a **stack**, or recursion:

```python
def dfs(graph, u, visited=None):
    if visited is None:
        visited = set()
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs(graph, v, visited)
    return visited
```

**Trace from $A$.** Visit $A$, go to $B$, then from $B$ to $C$ (first unvisited neighbour; $C$'s neighbours are all visited, so backtrack), then from $B$ to $D$, then $E$. Order: $A,B,C,D,E$.

Also $\Theta(|V|+|E|)$. DFS does **not** find shortest paths, but it is the right tool for:

- detecting cycles (an edge to a vertex still on the current path),
- topological sorting of a directed acyclic graph ([[DM 11 Trees and Graph Algorithms]]),
- finding connected components,
- exploring a maze or game tree with backtracking.

## BFS or DFS?

| Need | Use |
|---|---|
| fewest edges from the start | BFS |
| is there any path at all? | either |
| cycle detection, ordering dependencies | DFS |
| low memory on a wide, shallow graph | DFS |
| shortest path with weights | neither: Dijkstra or A* ([[DM 11 Trees and Graph Algorithms]]) |

## Euler and Hamilton

An **Euler circuit** uses every **edge** exactly once and returns to the start. A connected graph has one exactly when **every vertex has even degree**: each visit to a vertex enters on one edge and leaves on another, using edges in pairs. This settled the Königsberg bridges problem in 1736, the founding result of graph theory. Easy to test.

A **Hamiltonian cycle** visits every **vertex** exactly once. It sounds similar, yet no efficient test is known; the problem is NP-complete. The travelling salesman problem asks for the cheapest one. A small change of wording can move a problem from easy to (as far as anyone knows) intractable.

## Common mistakes

- **Forgetting to mark vertices as visited.** On a graph with cycles the search never ends.
- **Using BFS distances on a weighted graph.**
- **Confusing paths and walks.** A walk may repeat vertices; a path may not.
- **Using an adjacency matrix for a huge sparse graph.**

## Learn by doing

1. A graph has degrees $3,3,2,2,2$. How many edges?
2. Can any graph have degrees $3,3,3,2$? Can a simple graph on 4 vertices have degrees $3,3,1,1$?
3. Run BFS from $E$ on the running example. Give each distance.
4. Does the running example have an Euler circuit?

> [!success]- Check your answers
> 1. $12/2=6$.
> 2. First: no. The degree sum is 11, which is odd, so the handshake lemma rules it out. Second: also no, even though the sum 8 is even. With 4 vertices, a degree-3 vertex is adjacent to all three others. Both degree-3 vertices are then adjacent to each degree-1 vertex, giving those vertices degree 2. Passing the handshake test is necessary, not sufficient.
> 3. $E{:}0$, $D{:}1$, $B{:}2$, $A{:}3$, $C{:}3$.
> 4. No. $B$ and $E$ have odd degree.

## Where this shows up

Path planning on grids and roadmaps, scene graphs relating objects, and the transition graph of a Markov chain ([[PS 12 Markov Chains and Information]]) are all graphs. A neural network is a directed acyclic graph of operations, and backpropagation walks it in reverse topological order.
