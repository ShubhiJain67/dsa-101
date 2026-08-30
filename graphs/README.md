## Representations
### Adjacency Matrix
   - Extra Space watsed when less edges are there
   - Space -> O(v * v) (regardless of numbe of edges)
   - unidirected graphs's matrix is symitrical from diagonal
   - [][]bool
     ```
     [[0,0,0,0],
     [1,0,1,1],
     [1,0,0,1],
     [0,0,0,0]]
     ```
### Adjacency List
  - No extra space wated
  - Space -> O(V + e)
  - map[int][]int
    ```
    {
      1:[0,2,3],
      2:[0,3],
      0:[],
      3:[],
    }
    ```
### Edge List
  - Simple list of all edges: `[(u1, v1, w1), (u2, v2, w2), ...]`
  - Space -> O(E)
  - Used when you need to SORT edges (Kruskal's) or just iterate over every edge once (Bellman-Ford)
  - Bad for "find neighbors of node X" (needs O(E) scan) - use Adjacency List for that instead

---------

## [IMP] How to check if it is a graph's questio
- Entites would be numbered or labeled (example we have n courses labeled distinctly)
- [OR] Can see relations / paths between entities
- [OR] Direct -> Cclic or not, Bipartite or not

---------

## Keyword → Algorithm Cheat Sheet
| Keywords in Question | Algorithm |
|---|---|
| Traverse all paths / all combinations | DFS |
| Shortest path, unweighted | BFS |
| Shortest path, multiple starting points | Multi-source BFS |
| Shortest path, weights are only 0/1 | 0-1 BFS |
| Shortest path, huge search space, source AND destination both known | Bidirectional BFS |
| Graph built implicitly from transformations/states (not given as adjacency list) | BFS on Implicit Graph |
| Shortest path, weighted, single source, no negative edges | Dijkstra |
| Shortest path, weighted, negative edges allowed / detect negative cycle | Bellman-Ford |
| Shortest path, all pairs | Floyd-Warshall |
| Ordering with dependencies (DAG) | Topological Sort |
| Shortest/longest path, graph is a DAG (may have negative edges) | Topo Sort + DP relaxation |
| Cycle detection (directed) | DFS 3-color (white/gray/black) or BFS Kahn's |
| Cycle detection (undirected) | DFS/BFS with parent tracking, or DSU |
| Can graph be divided into 2 groups / no 2 adjacent same group | Bipartite Check |
| Union / grouping / connectivity queries | DSU (Union-Find) |
| Union with a ratio/relation between nodes ("a/b = 2, find a/c") | Weighted DSU |
| Minimum cost to connect all nodes | MST (Prim's / Kruskal's) |
| Node whose removal disconnects the graph | Articulation Point |
| Edge whose removal disconnects the graph | Bridge |
| Cluster of strongly related nodes (directed graph) | SCC (Kosaraju's / Tarjan's) |
| Compress each SCC into 1 node, need it acyclic | Condensation Graph (always a DAG) |
| Boolean satisfiability, exactly 2 vars per clause | 2-SAT (via SCC) |
| Visit every EDGE exactly once | Eulerian Path/Circuit |
| Visit every NODE exactly once | Hamiltonian Path/Cycle (NP-Hard, bitmask DP for small n) |
| Max data that can flow start->end given capacities | Max Flow (Ford-Fulkerson / Edmonds-Karp) |
| All pairs shortest path, SPARSE graph, negative edges | Johnson's Algorithm |
| Shortest path on a grid/map, target node known upfront | A* Search (heuristic-guided Dijkstra) |
| Grid problems (islands, regions, flood fill) | Grid as Graph (BFS/DFS, 4 or 8-directional) |
| Longest path between 2 nodes in a TREE | Tree Diameter (2-BFS/DFS trick) |
| Ancestor queries / distance between 2 nodes in a TREE | LCA (Binary Lifting / Euler Tour + Sparse Table) |
| Need an answer computed with EVERY node as root | Rerooting Technique |

---------

## Algorithms
### DFS
- Depth First Search
- Path questions
- Traversal lengthwise
- This covers all the possible paths
- TC - O(V + E)
  ```
  func dfs(adjList map[int][]int, node int, visited map[int]bool, traversal []int) {
  	if visited[node] {
  		return
  	}
  
  	visited[node] = true
    traversal = traversal.append(node)
  	for _, neighbor := range adjList[node] {
  		if !visited[neighbor] {
  			dfs(adjList, neighbor, visited, traversal)
  		}
  	}
  }
  ```

### BFS
- Breadth First Search
- Traverses level wise (Level order Traversal)
- Used to find shortest path
- Using a visited array does not work for shortest path problems on weighted graphs. A node reached once should not be considered finalized, because another path discovered later through a cycle or a different route may have a smaller total weight. The shortest path is determined by edge weights, not by the number of edges traversed. Hence we use DIJAKSTRA's
- TC - O(V + E)
  ```
    func bfs(adjList map[int][]int, start int, visited map[int]bool, traversal *[]int) {
    	queue := []int{start}
    	for len(queue) > 0 {
    		node := queue[0]
    		queue = queue[1:]
    
    		if visited[node] {
    			continue
    		}
    
    		visited[node] = true
    		*traversal = append(*traversal, node)
    
    		for _, neighbor := range adjList[node] {
    			if !visited[neighbor] {
    				queue = append(queue, neighbor)
    			}
    		}
    	}
    }
  ```

### Multi source BFS
- BFS - is from 1 source, ** Multi Sorce BFS ** Has multiple sources/starting point in a graph
- in BFS -> initally while initialling queue we used to add only 1 source, in mutli we add all. so level 1 of all sources will be processed forst then level 2 and so on..

### 0-1 BFS
- variation of BFS
- used to find single source shortest path (another is Dijkstra)
- EITHER all edges have same weight (in Dijakstra every edge can have diff +ve weight) ** becuase if edge weight is same then the path with less nodes will always be the shortest and hence BFS works ** (all can be onsidered 1 and final answer * the weight)
- OR wieights of the edges are either 0 or 1
- If we have Dijkstra then why this? **0-1 BFS is O(V+E), faster than Dijkstra's O(E log V) - no heap needed, just a deque**
- **At any point in time we have at most 2 distinct distance-levels in the deque**
- **THE ACTUAL MECHANIC (missing above if you just remember "it's like BFS")**: use a DEQUE, not a normal queue
  ```
  deque = [start]
  while deque:
      node = deque.popleft()
      if visited[node]: continue
      visited[node] = true
      for neighbor, weight in adjList[node]:
          if weight == 0:
              deque.appendleft(neighbor)   # push FRONT
          else:
              deque.append(neighbor)       # push BACK
  ```
- Weight-0 edges get processed before anything already queued (pushed to front) - that's the whole trick

### Bidirectional BFS
- Run 2 BFS simultaneously - one from source, one from destination
- Stop as soon as the 2 frontiers meet
- Reduces search space from O(b^d) to O(b^(d/2)) (b = branching factor, d = depth)
- Only works when BOTH source and destination are known upfront (won't work for single-source-to-all-destinations problems)
- Alternate expanding whichever frontier is SMALLER each step (keeps both sides balanced, this is what gives the speedup)
- KEYWORDS - "shortest transformation from A to B", "minimum steps from start to end", word-ladder style problems

### BFS on Implicit Graphs (Build Edges on the Fly)
- Graph is NOT given as an adjacency list/matrix - nodes are STATES, edges are TRANSFORMATIONS between states
- Example: Word Ladder (nodes = words, edge exists if 2 words differ by exactly 1 letter)
- Generate neighbors on the fly instead of looking them up (mutate the state, check if the result is valid/unvisited)
- Still plain BFS underneath - only the neighbor-generation step is different
- KEYWORDS - "minimum operations/steps to transform X into Y"

### Grid as Graph
- Each cell (r, c) is a node, edges connect to 4 (up/down/left/right) or 8 (+ diagonals) neighboring cells
- ALWAYS check grid boundaries before visiting a neighbor
- 4-directional -> Number of Islands, Flood Fill, Rotten Oranges, Walls and Gates
- 8-directional -> only when diagonal movement is explicitly allowed by the problem - **check the problem statement carefully, this is the #1 place people lose marks by assuming the wrong direction set**
- Direction arrays speed up code: `dirs = [(-1,0),(1,0),(0,-1),(0,1)]` (add the 4 diagonals for 8-directional)
- Same DFS/BFS/Multi-source-BFS/Dijkstra concepts from above apply directly - cell = node, nothing new algorithmically

### Topo Sort
- Only in Directed Acyclic Graph (DAG)
- because i undirected graph you cannot tell which node will come first as there is no dorection (1 -> 2 : here we know 1 should come before 2)
- cannot be done in cyclic directed graph because for 1 -> 2 and 2 -> 1 : how will you understand which will ocme first?
- [Kahn's Algo](https://www.geeksforgeeks.org/dsa/topological-sorting-indegree-based-solution/)
- PUT KIDS FIRST AND THE PARENT [Topological Sort using DFS](https://www.geeksforgeeks.org/dsa/topological-sort-using-dfs/)
- There could be multiple topo sort for 1 DAG (0-> 1 2-> 1) 0,2,1 or 2,1,0 both are correct
- Indegree with 0 should ocme first
- If topo sort is not possible hence There is A CYCLE IN THE DIRECTED GRAPH   
   - In BFS the len(topo sort) != number of nodes
   - In DFS you will not be able to tell if it is cyclic or not, DFS Topo algo will still give a response but it might be invalid

### DAG Shortest/Longest Path (via Topological Sort)
- Only works on a DAG (no cycles)
- Get the topo order first, then relax edges in THAT order - 1 pass, no heap needed (unlike Dijkstra)
- TC - O(V + E), faster than Dijkstra AND works with NEGATIVE EDGES (no cycle exists to make them a problem)
- For LONGEST path - negate all weights and run the same relaxation, OR just flip min to max in the relaxation step
- KEYWORDS - "DAG", "shortest/longest path", "critical path", "project scheduling", "minimum/maximum time to complete all tasks"

### Cycle Detection (DFS) - 3 Color Method (White / Gray / Black)
- Alternative to the visited + pathVisited approach used above, cleaner CLRS-standard naming
- **WHITE** -> node not visited yet
- **GRAY** -> node currently in the recursion stack (being processed)
- **BLACK** -> node fully processed (it and all its descendants are done)
- While doing DFS, if you hit a **GRAY** node -> CYCLE FOUND
- If you hit a **BLACK** node -> safe, no cycle (already fully explored, cannot loop back)
- Works directly for DIRECTED graphs (GRAY = same idea as pathVisited)
- For UNDIRECTED graphs still need to ignore the immediate parent edge (same trap as before)

### Bipartite Graph
- Graph's node can be coloured from 2 colors with no 2 adjacent nodes with same color
- If odd length cycle - NOT bipartite otherwise - BIPARTITE
- **Intiution - Dividing a graph/ grouping nodes**
- Can be done using BFS, DFS, DSU

### Disjoint Set Union(DSU) / Union Find
- Bipartite can be done via DSU as well
- Sets with intersection = Null are called disjoint sets
- has 2 main operations (hence called Union Find)
   - Combine 2 sets
   - Tell if 2 members belong to same set or not
- every set has a leader/parent
- whenever a union is done, all elements of the set will have the same leader/parent (directly or indirectly) now (there will be an election in btw 2 leaders of the inital sets)
- **Union by Rank and Path Compression** - If we keep on doing union in a way that the tree becomes an unbalanced tree (more towards 1 side) the the time complexity of finding out the parent would increase O(n), so we perform union base don rank (or size) and path
  - Rank and Path Comporession
     - Rank: the max depth of the parent
     - Path Compression: Keep updating the child nodes about their ultimate parent while you are already traversing in (find)
  - Size and Path Comporession
     - Size : number of nodes in the set
     - Path Compression: Keep updating the child nodes about their ultimate parent while you are already traversing in (find)
- **Always one element with more rank is elected so that the tree depth does not increase any further.**
- **If ranks are same then choose any one and increase the rank of one becoming parent**
- It is not necessary that with path compression at every point in time parents array will have the topmost parent (ony when after updating find is called teh parents are updated)
- **Core find/union (missing above if you've only got the theory)**:
  ```
  func find(x):
      if parent[x] != x:
          parent[x] = find(parent[x])   # path compression - rewires x straight to the root
      return parent[x]

  func union(x, y):
      rootX, rootY = find(x), find(y)
      if rootX == rootY: return
      if rank[rootX] < rank[rootY]: rootX, rootY = rootY, rootX
      parent[rootY] = rootX             # smaller rank hangs under bigger rank
      if rank[rootX] == rank[rootY]: rank[rootX] += 1
  ```

### DSU with Weights/Ratios (Union-Find with Relations)
- Normal DSU only tells you IF 2 nodes are connected
- Weighted DSU also tells you the RELATION/RATIO between 2 connected nodes
- Store a `weight[]` array alongside `parent[]` -> `weight[x]` = ratio of x to its parent
- On `find`, accumulate the ratio while doing path compression
- On `union`, compute the ratio between the 2 leaders using the known ratio on the union edge
- KEYWORDS - "a/b = 2, b/c = 3, find a/c" -> Evaluate Division style problems

### Dijkstra's Algorithm
- SINGLE SOURCE to ALL other nodes (not "1 source and 1 destination" - it naturally computes shortest distance from the source to EVERY reachable node; if you only care about 1 destination you can early-exit the moment you pop it, but that's an optimization, not what the algorithm fundamentally does)
- In weighted graph
- Finds min path weight
- Works on both directed and undirected graphs.
- Uses min heap to get all better paths found in journey
- using min heap so that the paths with less weight is getting prioritised
- While processing curr Min node, there is a posibility that the weighted path of the node could have gotten updated by some other route.
- ** In C++ instead of heaps you can use Ordered sets because there you can delete an element form the set (the one which we are ignoring as someother node's processing could have changed the value and made this insignificant) (This can be safely deleted because if the better one was pushed before then the future bigger values would not have made to the min list)
- In python there are no inbuilt order set hence the timecomplexity would not be improved
- ** KEYWORDS IN QUESTIONS **
   - Source, Dest
   - Shortest Path
   - Weighted Path (if not weighted can be done via BFS as well)
- ** CANNOT WORK WITH NEGATIVE EDGES ** - the real reason: Dijkstra treats a node's distance as FINAL the moment it's popped from the heap (greedy), assuming no future edge could ever improve it. A negative edge encountered later can still find a shorter path to an already-finalized node, but Dijkstra has already moved on and won't revisit it - so it gives a WRONG (not just slow) answer. (With a negative CYCLE specifically, distances can also shrink without bound, which is the "keeps decreasing" case - but the wrong-answer problem exists even with just one negative edge and no cycle at all.)
- **The loop skeleton (the "skip stale heap entries" part is what people forget)**:
  ```
  minHeap = [(0, start)]        # (distance, node)
  dist = {start: 0}
  while minHeap:
      d, node = heappop(minHeap)
      if d > dist.get(node, inf): continue   # STALE entry, a better one already got processed
      for neighbor, weight in adjList[node]:
          nd = d + weight
          if nd < dist.get(neighbor, inf):
              dist[neighbor] = nd
              heappush(minHeap, (nd, neighbor))
  ```
- No separate "visited" set needed if you do the stale-check above - it's what makes revisiting via a better path safe

### A* Search
- Informed version of Dijkstra - uses a HEURISTIC to guide the search toward the destination faster
- Priority = actual cost so far (g) + estimated cost to goal (h) -> `f = g + h`
- Heuristic must be ADMISSIBLE (never overestimates true cost) to guarantee the optimal path - e.g. Manhattan/Euclidean distance on a grid
- If h = 0 always -> A* degrades to plain Dijkstra
- Faster than Dijkstra in practice - explores fewer nodes because it prioritizes ones "closer" to the goal
- KEYWORDS - "shortest path on a grid/map with a KNOWN target", pathfinding-style problems

### Bellman Ford Algorithm
- Works with Negative edges
- Finds min path weight
- Only works for Directed Graph (if an undirected graph is given, ** convert it into directed by adding both edges -> and <- **)
- if you ** RELAX ** all edges (V - 1) times you will get the shortest path (RELAX - when in Dijakstra's algo we used to update the minWeight after poping min heap element)
- The edge order within each pass does NOT need to be fixed/identical across iterations - correctness only requires that EVERY edge gets relaxed at least once per pass, for V-1 passes total. (Keeping the order consistent just makes it easier to reason about "which level got relaxed when" - it's a mental-model convenience, not a correctness requirement.)
- Why (V-1) passes is enough -> each pass guarantees the shortest path is found for all nodes at least 1 hop further than the previous pass guaranteed (1st iteration of relaxation, all nodes 1 edge from source get finalized, and some further nodes may get too)
- Why (V-1) -> if they are lineraly joined then the total number of levels would be V - 1
- If on relaxing Vth time if any distance gets updated then it means ** THERE IS A NEGATIVE CYCLE **

### Floyd Warshall Algorithm
- Multiple source and multiple destinations
- Works with directed graph (for undirected make it directed) then it will work
- Got to every vertex and for each vertex go via each vertex the minimum of all would be the minimum distance.
- **LOOP ORDER MATTERS (silent-bug risk if you mix this up)**: `k` (the intermediate vertex) MUST be the outermost loop
  ```
  for k in range(V):
      for i in range(V):
          for j in range(V):
              dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  ```
- If `i` or `j` is outermost instead of `k`, you get WRONG answers with no error - it just silently computes garbage, so this is worth memorizing exactly
- CAN DETECT NEGATIVE CYCLE - HOW?
  dist from 1 node to itself should be 0. SO IF ANY DIAGONAL ELEMENT IS NOT 0 then it has a negative cycle

### Johnson's Algorithm
- All-pairs shortest path, works with NEGATIVE edges, faster than Floyd-Warshall on SPARSE graphs
- TC - O(V^2 log V + VE) vs Floyd-Warshall's O(V^3) - better when E << V^2
- Steps:
  1. Add a new node connected to every other node with 0-weight edges
  2. Run Bellman-Ford from that new node to get `h[]` (used to reweight edges and remove negative weights)
  3. Reweight every edge: `w'(u,v) = w(u,v) + h[u] - h[v]` (guaranteed non-negative now)
  4. Run Dijkstra from EVERY node on the reweighted graph
  5. Convert distances back using `h[]`
- KEYWORDS - "all pairs shortest path", "sparse graph", "negative edges but no negative cycle"

### Max Flow (Ford-Fulkerson / Edmonds-Karp)
- Given a directed graph with EDGE CAPACITIES, find the max "flow" possible from source to sink
- **Residual Graph**: for every edge u->v with capacity c and flow f, keep a residual capacity (c - f) forward AND a residual capacity f backward (v->u) - the backward edge lets the algo "undo" a bad earlier choice
- **Ford-Fulkerson**: repeatedly find ANY augmenting path (source to sink with residual capacity > 0) via DFS, push the bottleneck (min capacity along the path) as flow, update the residual graph, repeat until no path exists
- **Edmonds-Karp**: same as Ford-Fulkerson but uses BFS to find the augmenting path (shortest path by edge count) - guarantees TC O(V * E^2), avoids Ford-Fulkerson's worst-case slow convergence
- **Max-Flow Min-Cut Theorem**: max flow = min cut (min total capacity of edges that, if removed, disconnect source from sink)
- KEYWORDS - "capacities", "max flow", "bottleneck", "min cut", "maximum number of edge-disjoint paths"

### Spanning Tree
- Graph should be weighted and connected
- If a graph has V vertex and E edge then its conncted sub graph is called a spanning tree when
     - It has all the vertex of the graph
     - It has V - 1 number of edges
- THERE WILL NEVER BE A CYCLE IN A SPANNING TREE
graph -       spanning trees -
    a - b           a - b          a - b          a   b          a - b         
    |   |           |   |              |          |   |          |    
    c - d           c   d          c - d          c - d          c - d

### Minimum Spanning Tree
- Minimum weight spanning (a spanning tree of a graph who's sum weight of all the edges should be minimum)
graph -       spanning trees -
      5               5              5                             5
    a - b           a - b          a - b          a   b          a - b         
  2 |   | 3       2 |   | 3            | 3      2 |   | 3      2 |    
    c - d           c   d          c - d          c - d          c - d
      8                              8              8              8
                     10 (MST)        16             13            15
- Keywords - **minimum cost to make all points connected.**
- This is found with Kruskal and Prims algo

### Prims Algorithm 
- Keep on fetching the lowest neighbour from a node unless all the nodes are connected
- Making the Tree in a connected format (at any point in time the visted nodes are fully connected)

### Kurskal's
- Sort all the weights based on assemnding order
- Here it is not mandatory that at every point the the visited nodes are fully connected
- Keep on fetching the min weight and keep on adding if the 2 nodes are no connected with each other
- Solved using DSU, keep on adding the min popped weighted edge if the 2 nodes connected via it are in different sets

### Strongly Connected Components
- If there is a path from node a to b in a component of graph then there will be a path from b to a
 <img width="914" height="433" alt="Screenshot 2026-07-11 at 10 55 45 PM" src="https://github.com/user-attachments/assets/9e2aa757-58b8-45b4-8f17-d1242816845b" />

### Kosaraju's Algorithm
- to find all strongly connected components
- Find the topological sort
- reverse all the directons of arrows
- apply DFS on nodes in order of topo sort
- The number of times DFS runs -> Number of connected components

### Bridges & Articulation Points (Tarjan's Low-Link Algorithm)
- Both found using 1 DFS pass with 2 arrays: `tin[]` (time of insertion) and `low[]` (lowest tin reachable from the subtree, including via at most 1 back edge)
- `low[node] = min(tin[node], tin of back-edge neighbors, low of child neighbors)`
- **Bridge**: edge (u, v) where v is a child of u in the DFS tree, is a bridge if `low[v] > tin[u]` (child cannot reach u or anything before u WITHOUT this edge)
- **Articulation Point**:
  - Root of the DFS tree is an articulation point if it has MORE THAN 1 child in the DFS tree
  - Any other node u is an articulation point if it has a child v with `low[v] >= tin[u]` (child cannot escape without going through u)
- Ignore the edge back to the immediate PARENT while computing low[] (same parent-edge trap as cycle detection)
- TC - O(V + E)
- KEYWORDS - "critical connections", "removing this edge/node disconnects the graph", single point of failure

### Tarjan's Algorithm (SCC)
- Alternative to Kosaraju's - finds all SCCs in 1 DFS pass (Kosaraju's needs 2 passes + reversing the graph)
- Uses the SAME `tin[]` / `low[]` low-link idea as Bridges/Articulation Points above
- Maintain a stack of nodes currently "in progress" (on the current DFS path and not yet assigned to an SCC)
- A node `u` is the ROOT of an SCC if `low[u] == tin[u]`
- When a root is found - pop the stack until `u` itself is popped, everything popped together = 1 SCC
- TC - O(V + E), Space - O(V) (no need to build a reversed graph like Kosaraju's)

### Condensation Graph (SCC → DAG)
- Compress each SCC into a single node -> the resulting graph is ALWAYS a DAG (if there were a cycle between SCCs, they'd be 1 SCC by definition)
- Built after finding SCCs (Kosaraju's or Tarjan's)
- Once you have this DAG, every DAG technique applies on top (topo sort, DAG shortest/longest path, DP over the DAG)
- KEYWORDS - "condense/compress strongly connected components", "make the graph acyclic", any problem combining SCC + topo sort/DP

### 2-SAT
- Solves boolean satisfiability where each clause has EXACTLY 2 variables, e.g. `(x1 OR x2)`
- Model each variable as 2 nodes: `x` and `NOT x`
- Each clause `(a OR b)` becomes 2 directed implication edges: `(NOT a -> b)` and `(NOT b -> a)` ("if a is false, b must be true")
- Find SCCs of this implication graph
- **UNSATISFIABLE** if any variable `x` and `NOT x` land in the SAME SCC (means x = NOT x, impossible)
- Otherwise **SATISFIABLE** - assign each variable based on topo order of the condensation graph (whichever of x / NOT x appears LATER in topo order gets TRUE)
- KEYWORDS - "boolean satisfiability", "exactly 2 choices per constraint", "assign true/false satisfying all conditions"

### Eulerian Path and Circuit/Cycle
- Works for both Directed and Directed Graph
- A path of edges which visited all the edges in the graph EXACTLY ONCE
- KEYWORDS (visit full path (each edge once))
- **Handshaking Lemma**: sum of all node degrees = 2 * number of edges (each edge contributes to 2 nodes' degree) - quick sanity check for the degree-based Euler conditions below
- Not all graphs have a eularian path
- An eularian Path with Starts and end at the same node -> Eulerian Circuit or Eulerian Cycle
- If your graph has a eulerian cycle then you can start from any node and reach that node by traversing every edge once
- If a GRAPH IS NOT A EULAERIAN CIRCUIT
  - On starting from any node you will not be able to come bac on it
  - OR you won't be able to cover all edges
- NON ZERO DEGREE NODE COMPONENTS MUST BELONG TO A SINGLE CONNECTED COMPONENT
- **AN EULERIAN CIRCUIT will have all nodes with even number of edges (half for going and half for coming back)**
- **AN EULERIAN PATH will have all nodes with even number of edges EXCEPT FOR START AND END NODE**
- If a graph has EULER PATH and not a CIRCUIT -> SEMI EULERIAN GRAPH
- **Not all vertices in the graph need to be connected. Only the vertices that have at least one edge (non-zero degree) must belong to the same connected component.**
- IF THERE IS NO EDGE -> EULER CIRCUIT
- - FOR DIRECTED GRAPH (EULAR PATH)
   - Strat Node : outdegree - indegree = 1 -> THIS SHOULD START THE DFS
   - End Node : indegree - outdegre = 1
   - Rest Nodes : indegree = outdegree
   - IF ALL HAVE indegree = outdegree -> EULER CIRCUIT
- Do not confuse with HAMILTONIAN PATH/CYCLE (visits every NODE once, not every edge - see below)

### Hierholzer's Algorithm
- For directed graph
- Apply DFS (and keep on removing the edge that has already been traversed)
- Ensure you start from the right node

### Hamiltonian Path & Cycle
- Visits every NODE exactly once (Euler = every EDGE exactly once - do not confuse the two)
- NP-Hard in general - no known polynomial solution
- For SMALL n (<= ~20), solved via Bitmask DP: `dp[mask][node]` = can we reach this `node` having visited exactly the nodes in `mask`
- Hamiltonian CYCLE = Hamiltonian path that also returns to the start node
- TC - O(2^n * n^2) with bitmask DP
- KEYWORDS - "visit every city/node exactly once", "shortest route visiting all locations" (classic TSP framing)

---------

## Tree-on-Graph Techniques
(Trees are just acyclic connected graphs - these techniques exploit that structure specifically)

### Tree Diameter
- Longest path between any 2 nodes in a tree
- **2-BFS/DFS trick**: BFS/DFS from ANY node -> find the farthest node A -> BFS/DFS from A -> farthest node found from A is the OTHER end of the diameter, and that distance IS the diameter
- Why it works - in a tree, the farthest node from ANY starting point is always one endpoint of the diameter (known result, not obvious on first look)
- Alternative - DP on tree: for every node, `diameter = max(height of 2 deepest children) + 2`, take the max over all nodes
- TC - O(V) either way
- KEYWORDS - "longest path in a tree", "farthest 2 nodes"

### Lowest Common Ancestor (LCA)
- Deepest node that is an ancestor of BOTH given nodes
- **Binary Lifting**: precompute `up[node][j]` = 2^j-th ancestor of node, via `up[node][j] = up[up[node][j-1]][j-1]`
- To find LCA(u, v) - bring both to the SAME depth first (jump the deeper one up), then binary-jump BOTH up together until they're 1 step from meeting
- Precompute - O(V log V), Query - O(log V)
- **Euler Tour + Sparse Table (RMQ)**: flatten the tree via Euler tour, LCA(u,v) = node with min depth between the first occurrences of u and v in the tour -> becomes a Range Minimum Query problem
- Naive - walk both nodes up to root storing ancestors (or walk one path into a set) - O(V) per query, fine if you only have a few queries
- KEYWORDS - "common ancestor", "distance between 2 nodes in a tree" (`dist(u,v) = depth[u] + depth[v] - 2*depth[LCA(u,v)]`)

### Rerooting Technique
- Used when you need an answer computed for EVERY node treated as the root (e.g. sum of distances from each node to all others)
- Naive - O(V) traversal from every node = O(V^2) total
- Rerooting - 1 DFS to compute the answer for an arbitrary root, then a 2nd DFS to DERIVE every other node's answer from its parent's answer in O(1) per node (using how the answer changes when the root shifts by exactly 1 edge)
- TC - O(V) total instead of O(V^2)
- KEYWORDS - "for every node as root", "sum of distances", any answer that would otherwise need V separate traversals

---------

## Questions
### Concepts Set 1 (Do in order)
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | BFS | - | [Link](https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/01_bfs.py) |
| 2 | DFS | - | [Link](https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/02_dfs.py) |
| 3 | Detect Cycle in Undirected Graph (DFS) | Amazon, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/03_undirected_graph_cycle_detection_dfs.py) |
| 4 | Detect Cycle in Undirected Graph (BFS) | Amazon, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/04_undirected_graph_cycle_detection_bfs.py) |
| 5 | Detect Cycle in Directed Graph (DFS) | Amazon, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/05_directed_graph_cycle_detection_dfs.py) |
| 6 | Topological Sort (DFS) | - | [Link](https://www.geeksforgeeks.org/problems/topological-sort/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/06_topo_sort_dfs.py) |
| 7 | Topological Sort (BFS / Kahn's Algorithm) | - | [Link](https://www.geeksforgeeks.org/problems/topological-sort/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/07_topo_sort_bfs_kahns.py) |
| 8 | Detect Cycle in Directed Graph (BFS / Kahn's Algorithm) | Amazon, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/08_directed_graph_cycle_detection_bfs_kahns.py) |


### Practice Set 1
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Number of proviences (DFS) | Google, Amazon, Microsoft | [Link](https://www.geeksforgeeks.org/problems/number-of-provinces/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/09_number_of_provience_dfs.py) |
| 2 | Number of proviences (BFS) | Google, Amazon, Microsoft | [Link](https://www.geeksforgeeks.org/problems/number-of-provinces/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/10_number_of_provience_bfs.py) 
| 3 | Course Schedule (BFS) | Apple, Amazon, Meta, Microsoft, Twitter | [Link](https://leetcode.com/problems/course-schedule/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/11_course_schedule_bfs.py)
| 4 | Course Schedule 2 (BFS) | Apple, Amazon, Meta, Microsoft, Twitter | [Link](https://leetcode.com/problems/course-schedule-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/12_course_schedule_ii_bfs.py) 
| 5 | Course Schedule (DFS) | Apple, Amazon, Meta, Microsoft, Twitter | [Link](https://leetcode.com/problems/course-schedule/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/13_course_schedule_dfs.py)
| 6 | Course Schedule 2 (DFS) | Apple, Amazon, Meta, Microsoft, Twitter | [Link](https://leetcode.com/problems/course-schedule-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/14_course_schedule_ii_dfs.py) 
| 7 | # Unreachable Pairs of Nodes in an Undirected Graph (DFS) | Microsoft | [Link](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/23_unreachable_pairs_of_nodes_undirected_graph_dfs.py) |
| 8 | # Unreachable Pairs of Nodes in an Undirected Graph (BFS) | Microsoft | [Link](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/24_unreachable_pairs_of_nodes_undirected_graph_bfs.py) |


---------

### Concepts Set 2 (Do in order)
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Bipartite Graph (DFS) | Facebook, Samsung, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/bipartite-graph/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/15_bipartite_graph_dfs.py) |
| 2 | Bipartite Graph (BFS) | Facebook, Samsung, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/bipartite-graph/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/16_bipartite_graph_bfs.py) |
| 3 | Disjoint Set (Union-Find) | Google, Facebook, Apple, Amazon, Netflix, Flipkart | [Link](https://www.geeksforgeeks.org/problems/disjoint-set-union-find/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/17_dsu.py) |
| 4 | Disjoint Set (Union-Find) with Rank and Path Compression | Google, Facebook, Apple, Amazon, Netflix, Flipkart | - | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/18_dsu_with_rank_and_path_compression.py) |
| 5 | Disjoint Set (Union-Find) with Size and Path Compression | Google, Facebook, Apple, Amazon, Netflix, Flipkart | - | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/44_dsu_with_size_and_path_compression.py) |


### Practice Set 2
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Detect cycle in Undirected Graph (DSU) | Google, Amazon, Microsoft | [Link](https://www.geeksforgeeks.org/problems/detect-cycle-using-dsu/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/19_undirected_graph_cycle_detection_dsu.py) |
| 2 | Satisfiability of Equality Equations | Google | [Link](https://leetcode.com/problems/satisfiability-of-equality-equations/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/20_satisfiability_of_equality_equations.py) |
| 3 | # Operations to Make Network Connected | Amazon | [Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/21_operations_to_make_network_connected.py) |
| 4 | # Unreachable Pairs of Nodes in an Undirected Graph (DSU) | Microsoft | [Link](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/22_unreachable_pairs_of_nodes_undirected_graph_dsu.py) |

---------

### Concepts Set 3 (Do in order)
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Dijkstra's Algorithm using Heaps | Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/25_dijkstras_algorithm_heap.py) |
| 2 | Bellman Ford Algorithm | Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/31_bellman_ford_algorithm.py) |
| 3 | 0-1 BFS | - | - | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/34_01_bfs.py) |


### Practice Set 3
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Shortest Path in an Undirected Graph | Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/26_shortest_path_weighted_undirected_path.py) |
| 2 | Network Delay Time | Google | [Link](https://leetcode.com/problems/network-delay-time/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/27_network_delay_time.py) |
| 3 | Shortest Path in Binary Matrix (Dijkstra's) | Google, Meta, Microsoft, Amazon | [Link](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/28_shortest_path_in_binary_matrix_dijkstras.py) |
| 4 | Shortest Path in Binary Matrix (BFS) | Google, Meta, Microsoft, Amazon | [Link](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/29_shortest_path_in_binary_matrix_bfs.py) |
| 5 | Path with minimum effort | Google, Meta, Microsoft, Amazon | [Link](https://leetcode.com/problems/path-with-minimum-effort/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/30_path_with_min_effort.py) |
| 6 | Rotten Oranges (Multi BFS) | Google, TickTock, Adobe, Amazon | [Link](https://leetcode.com/problems/rotting-oranges/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/32_rotten_oranges_multi_source_bfs.py) |
| 7 | Map of Highest Peak (Multi BFS) | Google, Microsoft | [Link](https://leetcode.com/problems/map-of-highest-peak/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/33_map_of_highest_peak_multi_source_bfs.py) |
| 8 | Find a Safe Walk Through a Grid (DFS and DFS with memo) | - | [Link](https://leetcode.com/problems/find-a-safe-walk-through-a-grid) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/35_fiind_a_safe_walk_through_grid_dfs.py) |
| 9 | Find a Safe Walk Through a Grid (Dijkstra's) | - | [Link](https://leetcode.com/problems/find-a-safe-walk-through-a-grid) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/36_fiind_a_safe_walk_through_grid_dijkstras.py) |
| 10 | Find a Safe Walk Through a Grid (01 BFS) | - | [Link](https://leetcode.com/problems/find-a-safe-walk-through-a-grid) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/37_fiind_a_safe_walk_through_grid_01_bfs.py) |


---------

### Concepts Set 4 (Do in order)
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Floyd Warshall Algorithm | Samsung | [Link](https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/38_floyd_warshall.py) |
| 2 | Prim's Algorithm | Amazon, Microsoft, Meta | [Link](https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/39_prims_algorithm.py) |
| 3 | Kruskal's Algorithm | Amazon, Microsoft, Meta | [Link](https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/41_kruskals_algorithm.py) |
| 4 | Kosaraju's Algorithm (Strongly Connected Components) | Amazon, Microsoft, Meta | [Link](https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/43_strongly_connected_components_kosarajus_algorithm.py) |


### Practice Set 4
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Minimum Cost to connect all points (Prim's Algorithm) | Microsoft, Flipkart | [Link](https://leetcode.com/problems/min-cost-to-connect-all-points/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/40_min_cost_to_connect_components_prims.py) |
| 2 | Minimum Cost to connect all points (Kruskal's Algorithm) | Microsoft, Flipkart | [Link](https://leetcode.com/problems/min-cost-to-connect-all-points/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/42_min_cost_to_connect_components_kruskals.py) |


---------

### Concepts Set 5 (Do in order)
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Euler Path and Circuit (Undirected Graph)| - | [Link](https://www.geeksforgeeks.org/problems/euler-circuit-and-path/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/45_euler_path_and_circuit.py) |
| 2 | Euler Path and Circuit (Directed Graph)| - | [Link](https://www.geeksforgeeks.org/problems/euler-circuit-in-a-directed-graph/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/46_euler_path_and_circuit_directed_graph.py) |
| 3  | Hierholzer's Algorithm | - | [Link](https://leetcode.com/problems/valid-arrangement-of-pairs) | 🔲 TODO - not built yet (47_hierholzers_algorithm.py) |


### Practice Set 5
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Valid Arrangement of Pairs | - | [Link](https://leetcode.com/problems/valid-arrangement-of-pairs) | 🔲 TODO - not built yet (48_valid_arrangement_of_pairs_euler.py) |

---------

### Concepts Set 6 (Do in order) - Bridges, Articulation Points, Tarjan's SCC
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Bridges in Graph | Google, Amazon | [Link](https://www.geeksforgeeks.org/problems/bridge-edge-in-graph/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/50_bridges_in_graph.py) |
| 2 | Articulation Points | Google, Amazon, Microsoft | [Link](https://www.geeksforgeeks.org/problems/articulation-point-1/1) | 🔲 TODO - not built yet (51_articulation_points.py) |
| 3 | Strongly Connected Components (Tarjan's Algorithm) | Google, Amazon | [Link](https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1) | 🔲 TODO - not built yet (52_scc_tarjans_algorithm.py) |

### Practice Set 6
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Critical Connections in a Network | Google, Amazon, Meta | [Link](https://leetcode.com/problems/critical-connections-in-a-network/) | 🔲 TODO - not built yet (53_critical_connections_in_a_network.py) |

---------

### Concepts Set 7 (Do in order) - Bidirectional BFS, Implicit Graph BFS, Weighted DSU
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Word Ladder (BFS) | Amazon, Google, Meta | [Link](https://leetcode.com/problems/word-ladder/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/54_word_ladder_bfs.py) |
| 2 | Word Ladder (Bidirectional BFS) | Amazon, Google, Meta | [Link](https://leetcode.com/problems/word-ladder/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/55_word_ladder_bidirectional_bfs.py) |
| 3 | Evaluate Division (Weighted DSU) | Google, Amazon | [Link](https://leetcode.com/problems/evaluate-division/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/56_evaluate_division_weighted_dsu.py) |

---------

### Concepts Set 8 (Do in order) - Max Flow
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Max Flow - Ford Fulkerson | Google, Amazon | [Link](https://www.geeksforgeeks.org/problems/find-the-maximum-flow2126/1) | 🔲 TODO - not built yet (57_max_flow_ford_fulkerson.py) |
| 2 | Max Flow - Edmonds Karp (BFS) | Google, Amazon | [Link](https://www.geeksforgeeks.org/problems/find-the-maximum-flow2126/1) | 🔲 TODO - not built yet (58_max_flow_edmonds_karp.py) |

### Practice Set 8
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Maximum Bipartite Matching | Google | [Link](https://www.geeksforgeeks.org/problems/maximum-bipartite-matching/1) | 🔲 TODO - not built yet (59_maximum_bipartite_matching.py) |

---------

### Concepts Set 9 (Do in order) - Hamiltonian Path/Cycle
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Traveling Salesman Problem (Bitmask DP) | Amazon, Google | [LeetCode 847](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | 🔲 TODO - not built yet (60_tsp_bitmask_dp.py) |

---------

### Concepts Set 10 (Do in order) - DAG Shortest/Longest Path, Condensation Graph
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Shortest Path in Directed Acyclic Graph | Amazon, Microsoft | [Link](https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/61_shortest_path_in_dag.py) |
| 2 | Parallel Courses III (Longest Path in a DAG) | Google, Amazon | [Link](https://leetcode.com/problems/parallel-courses-iii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/62_longest_path_in_dag.py) |
| 3 | Course Schedule IV (Condensation Graph / Reachability) | Amazon, Meta | [Link](https://leetcode.com/problems/course-schedule-iv/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/63_course_schedule_iv_condensation.py) |

---------

### Concepts Set 11 (Do in order) - Tree Diameter, LCA, Rerooting
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Diameter of Binary Tree | Amazon, Microsoft, Google | [Link](https://leetcode.com/problems/diameter-of-binary-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/64_diameter_of_binary_tree.py) |
| 2 | Diameter of N-ary Tree | Google, Amazon | [Link](https://leetcode.com/problems/diameter-of-n-ary-tree/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/65_diameter_of_n_ary_tree.py) |
| 3 | Lowest Common Ancestor (Basic, then re-solve with Binary Lifting) | Google, Amazon, Meta | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/66_lca_binary_lifting.py) |
| 4 | Kth Ancestor of a Tree Node (Binary Lifting) | Google, Amazon | [Link](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/) | 🔲 TODO - not built yet (67_kth_ancestor_binary_lifting.py) |
| 5 | Sum of Distances in Tree (Rerooting) | Google | [Link](https://leetcode.com/problems/sum-of-distances-in-tree/) | 🔲 TODO - not built yet (68_sum_of_distances_in_tree_rerooting.py) |

### Practice Set 11
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Find Minimum Diameter After Merging Two Trees | - | [Link](https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/description/) | 🔲 TODO - not built yet (49_minimum_diameter_after_merging_2_trees.py) |

---------

### Concepts Set 12 (Optional / Lower Priority) - Johnson's, A*, 2-SAT
- Lower interview frequency than everything above - only worth doing once Sets 1-11 are solid
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | A* Search on Shortest Path in Binary Matrix | Google | [Link](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/) | 🔲 TODO - not built yet (69_a_star_search.py) |
| 2 | Johnson's Algorithm (All Pairs Shortest Path) | - | [Link](https://www.geeksforgeeks.org/dsa/johnsons-algorithm/) | 🔲 TODO - not built yet (70_johnsons_algorithm.py) |
| 3 | 2-SAT (Two Sets) | - | [Link](https://codeforces.com/problemset/problem/468/B) | 🔲 TODO - not built yet (71_two_sat.py) |

---------

### Concepts Set 13 (Do in order) - Topo Sort & Constrained Shortest Path
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Alien Dictionary | Amazon, Google, Meta | [Link](https://www.geeksforgeeks.org/problems/alien-dictionary/1) | 🔲 TODO - not built yet (72_alien_dictionary.py) |
| 2 | Cheapest Flights Within K Stops | Amazon, Google, Microsoft | [Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/graphs/73_cheapest_flights_within_k_stops.py) |

---------


## Important Points
- Tree os a graph with no cycle
- Tree has a parent child fixed hierarchy
- Graph can either have a cycle or not
- Parent doesn't work for directed graphs because a cycle can return to any ancestor, not just the immediate parent; there is no symmetric "back-to-parent" edge to ignore. ( 0 -> 1 <- 2)
- PathVisited alone doesn't work for undirected graphs because every edge appears in both directions, so the edge back to the parent is always on the current DFS path and would be falsely detected as a cycle. ( 0 - 1 )
