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

---------

## [IMP] How to check if it is a graph's questio
- Entites would be numbered or labeled (example we have n courses labeled distinctly)
- [OR] Can see relations / paths between entities
- [OR] Direct -> Cclic or not, Bipartite or not

---------

## Algorithms
### DFS
- Depth First Search
- Path questions
- Traversal lengthwise
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
- If we have Dijkstra then why this? **This has less time complexity**
- **At any point in time we have 2 levels in the queue of BFS**
- Dijkstra (O(ElogV))
- DIJKSTRA WITH NO MIN HEAP, BUT A PRIORITY QUEUE


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
- **Union by Rank and Path Compression** - If we keep on doing union in a way that the tree becomes an unbalanced tree (more towards 1 side) the the time complexity of finding out the parent would increase O(n), so we perform union base don rank and path
  - Rank: the max depth of the parent
  - Path Compression: Keep updating the child nodes about their ultimate parent while you are already traversing in (find)
- **Always one element with more rank is elected so that the tree depth does not increase any further.**
- **If ranks are same then choose any one and increase the rank of one becoming parent**
- It is not necessary that with path compression at every point in time parents array will have the topmost parent (ony when after updating find is called teh parents are updated)

### Dijkstra's Algorithm
- In weighted graph
- Finds min path wieght
- Uses min heap to get all beter paths found in journey
- using min heap so that the paths with less weight is getting prioritised
- While processing curr Min node, there is a posibility that the weighted path of the node could have gotten updated by some other route.
- ** In C++ instead of heaps you can use Ordered sets because there you can delete an element form the set (the one which we are ignoring as someother node's processing could have changed the value and made this insignificant) (This can be safely deleted because if the better one was pushed before then the future bigger values would not have made to the min list)
- In python there are no inbuilt order set hence the timecomplexity would not be improved
- ** KEYWORDS IN QUESTIONS **
   - Source, Dest
   - Shortest Path
   - Weighted Path (if not weighted can be done via BFS as well)
- ** CANNOT WORK WITH NEGATIVE EDGES ** as this will keep on updating the min path and keep on pushing it in min heap (more the number of times you traverse a negative edge the weight sum keeps on decreasing)

### Bellman Ford Algorithm
- Works with Negative edges
- Finds min path weight
- Only works for Directed Edge (if an undirected graph is given, ** convert it into directed by adding both edges -> and <- **)
- if you ** RELAX ** all edges (V - 1) times you will get the shortest path (RELAX - when in Dijakstra's algo we used to update the minWeight after poping min heap element)
- ^ Why? -> 

--------- 

## Questions
### Concepts Set 1 (Do in order)
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | BFS | - | [Link](https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/01_bfs.py) |
| 2 | DFS | - | [Link](https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/02_dfs.py) |
| 3 | Detect Cycle in Undirected Graph (DFS) | Amazon, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/03_undirected_graph_cycle_detection_dfs.py) |
| 4 | Detect Cycle in Undirected Graph (BFS) | Amazon, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/04_undirected_graph_cycle_detection_bfs.py) |
| 5 | Detect Cycle in Directed Graph (DFS) | Amazon, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/05_directed_graph_cycle_detection_dfs.py) |
| 6 | Topological Sort (DFS) | - | [Link](https://www.geeksforgeeks.org/problems/topological-sort/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/06_topo_sort_dfs.py) |
| 7 | Topological Sort (BFS / Kahn's Algorithm) | - | [Link](https://www.geeksforgeeks.org/problems/topological-sort/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/07_topo_sort_bfs_kahns.py) |
| 8 | Detect Cycle in Directed Graph (BFS / Kahn's Algorithm) | Amazon, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/08_directed_graph_cycle_detection_bfs_kahns.py) |


### Practice Set 1
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Number of proviences (DFS) | Google, Amazon, Microsoft | [Link](https://www.geeksforgeeks.org/problems/number-of-provinces/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/09_number_of_provience_dfs.py) |
| 2 | Number of proviences (BFS) | Google, Amazon, Microsoft | [Link](https://www.geeksforgeeks.org/problems/number-of-provinces/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/10_number_of_provience_bfs.py) 
| 3 | Course Schedule (BFS) | Apple, Amazon, Meta, Microsoft, Twitter | [Link](https://leetcode.com/problems/course-schedule/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/11_course_schedule_bfs.py)
| 4 | Course Schedule 2 (BFS) | Apple, Amazon, Meta, Microsoft, Twitter | [Link](https://leetcode.com/problems/course-schedule-ii/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/12_course_schedule_ii_bfs.py) 
| 5 | Course Schedule (DFS) | Apple, Amazon, Meta, Microsoft, Twitter | [Link](https://leetcode.com/problems/course-schedule/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/13_course_schedule_dfs.py)
| 6 | Course Schedule 2 (DFS) | Apple, Amazon, Meta, Microsoft, Twitter | [Link](https://leetcode.com/problems/course-schedule-ii/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/14_course_schedule_ii_dfs.py) 
| 7 | # Unreachable Pairs of Nodes in an Undirected Graph (DFS) | Microsoft | [Link](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/23_unreachable_pairs_of_nodes_undirected_graph_dfs.py) |
| 8 | # Unreachable Pairs of Nodes in an Undirected Graph (BFS) | Microsoft | [Link](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/24_unreachable_pairs_of_nodes_undirected_graph_bfs.py) |


---------

### Concepts Set 2 (Do in order)
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Bipartite Graph (DFS) | Facebook, Samsung, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/bipartite-graph/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/15_bipartite_graph_dfs.py) |
| 2 | Bipartite Graph (BFS) | Facebook, Samsung, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/bipartite-graph/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/16_bipartite_graph_bfs.py) |
| 3 | Disjoint Set (Union-Find) | Google, Facebook, Apple, Amazon, Netflix, Flipkart | [Link](https://www.geeksforgeeks.org/problems/disjoint-set-union-find/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/17_dsu.py) |
| 4 | Disjoint Set (Union-Find) with Raknk and Path Compression | Google, Facebook, Apple, Amazon, Netflix, Flipkart | - | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/18_dsu_with_rank_and_path_compression.py) |


### Practice Set 2
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Detect cycle in Undirected Graph (DSU) | Google, Amazon, Microsoft | [Link](https://www.geeksforgeeks.org/problems/detect-cycle-using-dsu/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/19_undirected_graph_cycle_detection_dsu.py) |
| 2 | Satisfiability of Equality Equations | Google | [Link](https://leetcode.com/problems/satisfiability-of-equality-equations/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/20_satisfiability_of_equality_equations.py) |
| 3 | # Operations to Make Network Connected | Amazon | [Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/21_operations_to_make_network_connected.py) |
| 4 | # Unreachable Pairs of Nodes in an Undirected Graph (DSU) | Microsoft | [Link](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/22_unreachable_pairs_of_nodes_undirected_graph_dsu.py) |

---------

### Concepts Set 3 (Do in order)
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Dijkstra's Algorithm using Heaps | Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/25_dijkstras_algorithm_heap.py) |
| 2 | Bellman Ford Algorithm | Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/31_bellman_ford_algorithm.py) |
| 3 | 0-1 BFS | - | - | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/34_01_bfs.py) |


### Practice Set 3
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Shortest Path in an Undirected Graph | Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/26_shortest_path_weighted_undirected_path.py) |
| 2 | Network Delay Time | Google | [Link](https://leetcode.com/problems/network-delay-time/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/27_network_delay_time.py) |
| 3 | Shortest Path in Binary Matrix (Dijkstra's) | Google, Meta, Microsoft, Amazon | [Link](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/28_shortest_path_in_binary_matrix_dijkstras.py) |
| 4 | Shortest Path in Binary Matrix (BFS) | Google, Meta, Microsoft, Amazon | [Link](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/29_shortest_path_in_binary_matrix_bfs.py) |
| 5 | Path with minimum effort | Google, Meta, Microsoft, Amazon | [Link](https://leetcode.com/problems/path-with-minimum-effort/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/30_path_with_min_effort.py) |
| 6 | Rotten Oranges (Multi BFS) | Google, TickTock, Adobe, Amazon | [Link](https://leetcode.com/problems/rotting-oranges/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/32_rotten_oranges_multi_source_bfs.py) |
| 7 | Map of Highest Peak (Multi BFS) | Google, Microsoft | [Link](https://leetcode.com/problems/map-of-highest-peak/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/33_map_of_highest_peak_multi_source_bfs.py) |
| 8 | Find a Safe Walk Through a Grid (DFS) | - | [Link](https://leetcode.com/problems/find-a-safe-walk-through-a-grid) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/35_fiind_a_safe_walk_through_grid_dfs.py) |
| 9 | Find a Safe Walk Through a Grid ( 01 BFS) | - | [Link](https://leetcode.com/problems/find-a-safe-walk-through-a-grid) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/36_fiind_a_safe_walk_through_grid_01_bfs.py) |


---------


## Important Points
- Tree os a graph with no cycle
- Tree has a parent child fixed hierarchy
- Graph can either have a cycle or not
- Parent doesn't work for directed graphs because a cycle can return to any ancestor, not just the immediate parent; there is no symmetric "back-to-parent" edge to ignore. ( 0 -> 1 <- 2)
- PathVisited alone doesn't work for undirected graphs because every edge appears in both directions, so the edge back to the parent is always on the current DFS path and would be falsely detected as a cycle. ( 0 - 1 )
