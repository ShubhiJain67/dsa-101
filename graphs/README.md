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


## Traversal
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

## Algorithms
### Topo Sort
- Only in Directed Acyclic Graph (DAG)
- because i undirected graph you cannot tell which node will come first as there is no dorection (1 -> 2 : here we know 1 should come before 2)
- cannot be done in cyclic directed graph because for 1 -> 2 and 2 -> 1 : how will you understand which will ocme first?
- [Kahn's Algo](https://www.geeksforgeeks.org/dsa/topological-sorting-indegree-based-solution/)
- PUT KIDS FIRST AND THE PARENT [Topological Sort using DFS](https://www.geeksforgeeks.org/dsa/topological-sort-using-dfs/)
- There could be multiple topo sort for 1 DAG (0-> 1 2-> 1) 0,2,1 or 2,1,0 both are correct
- Indegree with 0 should ocme first
- If topo sort is not possible hence There is A CYCLE IN THE DIRECTED GRAPH

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

### Practice
| # | Problem | Companies | GFG | Solution |
|---|---------|-----------|-----|----------|
| 1 | Number of proviences (DFS) | Google, Amazon, Microsoft | [Link](https://www.geeksforgeeks.org/problems/number-of-provinces/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/09_number_of_provience_dfs.py) |
| 2 | Number of proviences (BFS) | Google, Amazon, Microsoft | [Link](https://www.geeksforgeeks.org/problems/number-of-provinces/1) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/10_number_of_provience_bfs.py) 
| 3 | Course Schedule (BFS) | Apple, Amazon, Meta, Microsoft, Twitter | [Link](https://leetcode.com/problems/course-schedule/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/11_course_schedule_bfs.py)
| 4 | Course Schedule 2 (BFS) | Apple, Amazon, Meta, Microsoft, Twitter | [Link](https://leetcode.com/problems/course-schedule-ii/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/12_course_schedule_ii_bfs.py) 
| 5 | Course Schedule (DFS) | Apple, Amazon, Meta, Microsoft, Twitter | [Link](https://leetcode.com/problems/course-schedule/description/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/13_course_schedule_dfs.py)
| 6 | Course Schedule 2 (DFS) | Apple, Amazon, Meta, Microsoft, Twitter | [Link](https://leetcode.com/problems/course-schedule-ii/) | [Python](https://github.com/ShubhiJain67/Data-Structures-algorithms/blob/main/graphs/14_course_schedule_ii_dfs.py) 


## Important Points
- Tree os a graph with no cycle
- Tree has a parent child fixed hierarchy
- Graph can either have a cycle or not
- Parent doesn't work for directed graphs because a cycle can return to any ancestor, not just the immediate parent; there is no symmetric "back-to-parent" edge to ignore. ( 0 -> 1 <- 2)
- PathVisited alone doesn't work for undirected graphs because every edge appears in both directions, so the edge back to the parent is always on the current DFS path and would be falsely detected as a cycle. ( 0 - 1 )
