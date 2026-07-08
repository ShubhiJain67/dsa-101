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

## Questions
### Concepts Set 1
1. BFS - [GFG Link](https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1)
2. DFS - [GFG Link](https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1)
3. Detect Cycle in Undirected Graph using BFS (Amazon, Microsoft, Flipkart) [GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1)
4. Detect Cycle in Undirected Graph using DFS (Amazon, Microsoft, Flipkart) [GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1)
5. Detect Cycle in Directed Graph using DFS (Amazon, Microsoft, Flipkart) [GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1)
6. Detect Cycle in Directed Graph using BFS (Amazon, Microsoft, Flipkart) [GFG Link](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1)
7. Topological Sort using BFS [Khans Algo](https://www.geeksforgeeks.org/dsa/topological-sorting-indegree-based-solution/) [GFG Link](https://www.geeksforgeeks.org/problems/topological-sort/1)
8. [Topological Sort using DFS](https://www.geeksforgeeks.org/dsa/topological-sort-using-dfs/) [GFG Link](https://www.geeksforgeeks.org/problems/topological-sort/1)

### Practice
1. Number of proviences (Google, Amazon, Microsoft) [GFG Link](https://www.geeksforgeeks.org/problems/number-of-provinces/1) [Leetcode Link](https://leetcode.com/problems/number-of-provinces/)



## Important Points
- Tree os a graph with no cycle
- Tree has a parent child fixed hierarchy
- Graph can either have a cycle or not
