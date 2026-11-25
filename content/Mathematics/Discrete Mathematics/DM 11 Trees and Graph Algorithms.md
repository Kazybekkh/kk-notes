---
type: course-chapter
course: discrete-mathematics
chapter: 11
tags: [mathematics, discrete-mathematics, graphs, algorithms]
---
# DM 11 Trees and graph algorithms

Previous: [[DM 10 Graphs]] | [[DM 00 Course Map]] | Next: [[DM 12 Boolean Algebra and Automata]]

> [!abstract] One sentence
> A tree is a connected graph with no cycles, and the classic graph algorithms (topological sort, Dijkstra, A*, minimum spanning tree) each build a tree that answers one question about the graph.

## Trees

A **tree** is a connected undirected graph with no cycles. For a graph with $n$ vertices, the following are equivalent; any one of them makes it a tree:

1. Connected and acyclic.
2. Connected with exactly $n-1$ edges.
3. Acyclic with exactly $n-1$ edges.
4. Exactly one path between every pair of vertices.

**Why $n-1$ edges.** Every tree with at least two vertices has a **leaf** (a vertex of degree 1): follow a longest path; its end cannot have another neighbour without creating a longer path or a cycle. Remove the leaf and its edge to get a tree with one fewer vertex and one fewer edge. By induction ([[DM 06 Induction and Recursion]]), starting from one vertex and zero edges, a tree with $n$ vertices has $n-1$ edges.

Trees are minimally connected: remove any edge and the graph splits; add any edge and a cycle appears.

**Rooted trees.** Choose one vertex as the **root**. Every other vertex then has one **parent** (the next vertex toward the root) and possibly **children**. The **depth** of a vertex is its distance from the root; the **height** of the tree is the greatest depth.

A **binary tree** gives each vertex at most two children. A binary tree of height $h$ has at most $2^{h+1}-1$ vertices, so holding $n$ items needs height at least about $\log_2n$. That is why balanced search trees, heaps and binary search all run in $\Theta(\log n)$ ([[DM 09 Recurrences and Asymptotics]]).

**Search trees from BFS and DFS.** Recording, for each discovered vertex, the edge used to discover it produces a spanning tree of the component. BFS gives a tree of shortest paths.

## Topological sort

A **directed acyclic graph** (DAG) has directed edges and no directed cycle. Its edges express dependencies: $u\to v$ means $u$ must come before $v$. A **topological order** lists the vertices so that every edge points forward. It exists exactly when the graph has no directed cycle, and it is a total order extending the partial order of dependencies ([[DM 05 Functions and Relations]]).

**Kahn's algorithm.**

1. Compute every vertex's in-degree.
2. Put all vertices with in-degree 0 in a queue. They depend on nothing.
3. Repeatedly remove a vertex from the queue, append it to the output, and delete its outgoing edges. Any vertex whose in-degree drops to 0 joins the queue.
4. If fewer than $n$ vertices were output, the graph has a cycle.

**Worked example.** Getting dressed: socks $\to$ shoes, trousers $\to$ shoes, trousers $\to$ belt, shirt $\to$ belt, shirt $\to$ tie, tie $\to$ jacket, belt $\to$ jacket.

Start: in-degree 0 are socks, trousers, shirt. Output socks; then trousers (shoes now has in-degree 0, belt has 1); then shirt (belt and tie now 0); then shoes, belt, tie; then jacket.

Order: socks, trousers, shirt, shoes, belt, tie, jacket. Other valid orders exist.

Running time $\Theta(|V|+|E|)$. Used by build systems, spreadsheets recalculating cells, package installers, course prerequisites, and deep learning frameworks scheduling operations.

## Shortest paths with weights: Dijkstra

BFS counts edges. With positive edge weights (distances, times, costs) you need **Dijkstra's algorithm**.

**Idea.** Grow a set of vertices whose shortest distance is final. Repeatedly finalize the unfinalized vertex with the smallest tentative distance, then **relax** its outgoing edges:

$$
\text{if }d(u)+w(u,v)<d(v)\text{ then }d(v)\leftarrow d(u)+w(u,v).
$$

```python
import heapq

def dijkstra(graph, start):          # graph[u] = [(v, weight), ...]
    dist = {start: 0}
    heap = [(0, start)]
    done = set()
    while heap:
        d, u = heapq.heappop(heap)
        if u in done:
            continue
        done.add(u)
        for v, w in graph[u]:
            if d + w < dist.get(v, float("inf")):
                dist[v] = d + w
                heapq.heappush(heap, (d + w, v))
    return dist
```

**Worked example.** Edges: $S\text{-}A$ weight 4, $S\text{-}B$ weight 1, $B\text{-}A$ weight 2, $A\text{-}T$ weight 1, $B\text{-}T$ weight 5.

| Step | Finalize | Tentative distances after relaxing |
|---|---|---|
| 1 | $S$ (0) | $A{:}4$, $B{:}1$ |
| 2 | $B$ (1) | $A{:}\min(4,1+2)=3$, $T{:}1+5=6$ |
| 3 | $A$ (3) | $T{:}\min(6,3+1)=4$ |
| 4 | $T$ (4) | done |

Shortest $S$ to $T$: 4, along $S\to B\to A\to T$. The direct-looking routes $S\to A\to T$ (5) and $S\to B\to T$ (6) are longer.

**Why it is correct.** When $u$ has the smallest tentative distance, any other route to $u$ would leave the finalized set through some vertex already at least as far, and with non-negative weights it can only get longer. So $d(u)$ is final.

> [!warning] Negative weights break Dijkstra
> The argument above needs weights $\ge0$. With negative edges, use Bellman-Ford, which relaxes every edge $|V|-1$ times.

With a binary heap the running time is $O((|V|+|E|)\log|V|)$.

## A*: Dijkstra with a sense of direction

Dijkstra expands outward in all directions. If you know roughly where the goal is, steer toward it. **A\*** orders vertices by

$$
f(v)=g(v)+h(v),
$$

where $g(v)$ is the known cost from the start and $h(v)$ is an estimate of the remaining cost to the goal, the **heuristic**.

If $h$ never overestimates the true remaining cost (it is **admissible**), A\* still returns a shortest path, usually after exploring far fewer vertices. On a grid, straight-line distance to the goal is admissible because no path is shorter than a straight line. With $h=0$, A\* is exactly Dijkstra.

A\* on an occupancy grid is the standard global planner for mobile robots.

## Minimum spanning trees

Connect all vertices with the smallest total edge weight. The result must be a tree: any cycle has an edge you could drop while staying connected and saving weight.

**Kruskal's algorithm.** Sort edges by weight. Go through them in order; add an edge unless it would create a cycle (that is, unless its ends are already connected). Stop at $n-1$ edges.

**Prim's algorithm.** Grow a single tree from any start vertex, always adding the cheapest edge that reaches a new vertex.

Both are **greedy**: they make the locally best choice and never reconsider. That works here because of the **cut property**: for any split of the vertices into two groups, the cheapest edge crossing the split belongs to some minimum spanning tree. Greedy choices are usually not optimal, so this is worth noticing.

**Worked example (Kruskal).** Edges: $AB\,1$, $BC\,2$, $AC\,3$, $CD\,4$, $BD\,5$. Take $AB$ (1), take $BC$ (2), skip $AC$ ($A$ and $C$ are already connected), take $CD$ (4). Three edges for four vertices; total 7.

Applications: designing cheap cable or pipe networks, clustering (build the tree, then cut its most expensive edges), and approximation algorithms for the travelling salesman problem.

## Summary

| Question | Algorithm | Time |
|---|---|---|
| fewest edges, unweighted | BFS | $\Theta(V+E)$ |
| order tasks respecting dependencies | topological sort | $\Theta(V+E)$ |
| shortest path, non-negative weights | Dijkstra | $O((V+E)\log V)$ |
| shortest path toward a known goal | A\* | problem dependent |
| shortest path with negative weights | Bellman-Ford | $O(VE)$ |
| cheapest way to connect everything | Kruskal or Prim | $O(E\log V)$ |

## Common mistakes

- **Running Dijkstra with negative weights.**
- **Using an overestimating heuristic in A\*** and expecting optimal paths.
- **Confusing the shortest-path tree with the minimum spanning tree.** They are different trees: one minimizes distance from a single start, the other total edge weight.
- **Topologically sorting a graph with a cycle.**

## Learn by doing

1. A tree has 20 vertices. How many edges? A connected graph has 20 vertices and 25 edges. How many edges must be removed to make it a tree?
2. Topologically sort: $A\to C$, $B\to C$, $C\to D$, $B\to E$, $E\to D$.
3. Run Dijkstra from $S$: $S\text{-}A\,2$, $S\text{-}B\,6$, $A\text{-}B\,3$, $A\text{-}C\,7$, $B\text{-}C\,1$.
4. Find a minimum spanning tree: $AB\,4$, $AC\,1$, $BC\,2$, $BD\,5$, $CD\,8$.

> [!success]- Check your answers
> 1. 19. Remove $25-19=6$.
> 2. One valid order: $A,B,C,E,D$ (also $B,A,E,C,D$ and others).
> 3. $S{:}0$, $A{:}2$, $B{:}5$ via $A$, $C{:}6$ via $A,B$.
> 4. $AC\,1$, $BC\,2$, skip $AB$ (cycle), $BD\,5$. Total 8.

## Where this shows up

Global path planning ([[15 Robot Systems and Deployment]]), task and motion planning over dependency graphs, and search over action sequences in model-based planning ([[11 World Models and Planning]]).
