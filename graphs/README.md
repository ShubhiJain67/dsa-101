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

## [IMP] How to check if it is a graph's questio
- Entites would be numbered or labeled (example we have n courses labeled distinctly)
- [OR] Can see relations / paths between entities
- [OR] Direct -> Cclic or not, Bipartite or not


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
- Traverses level wise
- Used to find shortest path
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

### Concepts Set 2 (Do in order)
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Bipartite Graph (DFS) | Facebook, Samsung, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/bipartite-graph/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/15_bipartite_graph_dfs.py) |
| 2 | Bipartite Graph (BFS) | Facebook, Samsung, Microsoft, Flipkart | [Link](https://www.geeksforgeeks.org/problems/bipartite-graph/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/16_bipartite_graph_bfs.py) |
| 3 | Disjoint Set (Union-Find) | Google, Facebook, Apple, Amazon, Netflix, Flipkart | [Link](https://www.geeksforgeeks.org/problems/disjoint-set-union-find/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/17_dsu.py) |
| 4 | Disjoint Set (Union-Find) with Raknk and Path COmpression | Google, Facebook, Apple, Amazon, Netflix, Flipkart | - | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/18_dsu_with_rank_and_path_compression.py) |


### Practice Set 2
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Detect cycle in Undirected Graph (DSU) | Google, Amazon, Microsoft | [Link](https://www.geeksforgeeks.org/problems/detect-cycle-using-dsu/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/19_undirected_graph_cycle_detection_dsu.py) |
| 2 | Satisfiability of Equality Equations | Google | [Link](https://leetcode.com/problems/satisfiability-of-equality-equations/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/20_satisfiability_of_equality_equations.py) |
| 3 | # Operations to Make Network Connected | Amazon | [Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/21_operations_to_make_network_connected.py) |
| 4 | # Unreachable Pairs of Nodes in an Undirected Graph (DSU) | Microsoft | [Link](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/22_unreachable_pairs_of_nodes_undirected_graph_dsu.py) |


## Important Points
- Tree os a graph with no cycle
- Tree has a parent child fixed hierarchy
- Graph can either have a cycle or not
- Parent doesn't work for directed graphs because a cycle can return to any ancestor, not just the immediate parent; there is no symmetric "back-to-parent" edge to ignore. ( 0 -> 1 <- 2)
- PathVisited alone doesn't work for undirected graphs because every edge appears in both directions, so the edge back to the parent is always on the current DFS path and would be falsely detected as a cycle. ( 0 - 1 )
