# Trees

- A hierarchical structure - 1 root, each node has children, no cycles (a tree IS a graph, just an acyclic connected one - see graphs/README.md for the graph-theory side of trees: diameter, LCA via binary lifting, rerooting)
- This README covers TREE-SPECIFIC data structures and techniques not already covered elsewhere: traversals, BST, Trie, Segment Tree/Fenwick Tree, tree construction, and view/projection problems
- **Cross-references** (don't duplicate, go here instead):
  - Tree Diameter, LCA (binary lifting), Rerooting -> `graphs/README.md` - Tree-on-Graph Techniques
  - DP on Trees (House Robber III, Binary Tree Max Path Sum) -> `dynamic-programming/README.md` - DP on Trees

## How to Identify a Tree Question
- Explicit `TreeNode` with `.left` / `.right` (binary) or `.children` (n-ary)
- "BST", "balanced", "traversal", "view from the top/side"
- Prefix-based string problems -> often secretly a Trie question
- Range query + update on an array, repeated many times -> often secretly a Segment Tree / Fenwick Tree question in disguise

---------

## Keyword → Technique Cheat Sheet
| Keywords in Question | Technique |
|---|---|
| Visit node BEFORE its children | Preorder Traversal |
| Visit node AFTER its children | Postorder Traversal |
| Sorted order (for a BST specifically) | Inorder Traversal |
| Level by level | Level Order Traversal (BFS) |
| O(1) space traversal | Morris Traversal |
| Search/insert/delete using ordering, O(log n) | Binary Search Tree (BST) property |
| Validate a BST | Range-passing recursion (NOT just comparing to immediate children) |
| Rebuild a tree from traversal arrays | Preorder+Inorder or Postorder+Inorder construction |
| Save a tree to a string and rebuild it | Serialize/Deserialize |
| Path from root to leaf summing to a target | DFS with running sum (backtrack after each branch) |
| Path between ANY 2 nodes (not just root-to-leaf) | DFS returning (best-through-this-node, best-ending-at-this-node) pair - see DP on Trees in dynamic-programming/README.md |
| Top/Bottom/Left/Right view of a tree | Level order + track first-seen (or last-seen) node per column/level |
| Prefix-based search, autocomplete, "starts with" | Trie (Prefix Tree) |
| Range sum/min/max query + point update, repeated many times | Segment Tree |
| Prefix sum query + point update, repeated many times | Fenwick Tree / Binary Indexed Tree (simpler than Segment Tree when you only need prefix sums) |

---------

## Core Concepts

### Traversals
- **Preorder** (Root -> Left -> Right): used when you need to process a node BEFORE its children (e.g. copying/serializing a tree, prefix expression building)
- **Inorder** (Left -> Root -> Right): for a BST, this visits nodes in SORTED order - the single most useful fact about inorder traversal
- **Postorder** (Left -> Right -> Root): used when you need children's results BEFORE the parent can be processed (e.g. computing subtree sizes/heights, deleting a tree bottom-up, DP on trees)
- **Level Order** (BFS): visit level by level, left to right - use a queue, push both children when you pop a node
- **Iterative traversals** (interviewers sometimes ask you to avoid recursion): use an explicit STACK to simulate the call stack - for inorder specifically, push all left children first, then process, then move to the right subtree
- **Morris Traversal (O(1) space inorder, the non-obvious one)**: instead of a stack, temporarily THREAD the tree - for each node with a left child, find that left subtree's rightmost node (the inorder predecessor) and point ITS right pointer back to the current node. Follow that thread to return to the current node after finishing the left subtree, then remove the thread once used
  ```
  def morris_inorder(root):
      curr = root
      result = []
      while curr:
          if not curr.left:
              result.append(curr.val)
              curr = curr.right
          else:
              # find the inorder predecessor (rightmost node in left subtree)
              pred = curr.left
              while pred.right and pred.right != curr:
                  pred = pred.right
              if not pred.right:
                  pred.right = curr   # create the thread
                  curr = curr.left
              else:
                  pred.right = None   # remove the thread (already used)
                  result.append(curr.val)
                  curr = curr.right
      return result
  ```
- KEYWORDS - "traverse a tree", "iterative traversal", "O(1) space traversal"

### Binary Search Tree (BST)
- Property: for every node, ALL left-subtree values < node < ALL right-subtree values (not just the immediate children - this is the part people get wrong)
- Search/Insert/Delete are O(h) where h = tree height (O(log n) if balanced, O(n) if it degenerates into a line)
- **Validating a BST (the common mistake)**: checking only `node.val > node.left.val and node.val < node.right.val` is WRONG - a deep right-left grandchild could still violate the ancestor's constraint even if it satisfies its immediate parent. Instead pass down a valid `(min, max)` RANGE and shrink it as you recurse
  ```
  def is_valid_bst(node, low=-inf, high=inf):
      if not node: return True
      if not (low < node.val < high): return False
      return is_valid_bst(node.left, low, node.val) and is_valid_bst(node.right, node.val, high)
  ```
- **Delete a node**: 3 cases - leaf (just remove it), 1 child (replace node with its child), 2 children (replace node's value with its INORDER SUCCESSOR - the smallest value in the right subtree - then delete that successor node instead, which is now guaranteed to have at most 1 child)
- **BST to sorted Doubly Linked List**: inorder traversal naturally visits nodes in sorted order - rewire `.left`/`.right` into `.prev`/`.next` as you go
- KEYWORDS - "binary search tree", "validate BST", "kth smallest in BST" (inorder traversal, stop at the kth element)

### Tree Construction
- **From Preorder + Inorder**: preorder's FIRST element is always the root. Find that value's position in inorder - everything to its left is the left subtree, everything to its right is the right subtree. Recurse on both halves
- **From Postorder + Inorder**: same idea, but the root is the LAST element of postorder instead of the first
- Note: preorder + postorder ALONE (without inorder) is NOT enough to uniquely reconstruct a general binary tree (ambiguous when a node has only 1 child) - you specifically need inorder paired with one of the other two
- **Serialize/Deserialize**: preorder traversal + explicit "null" markers for missing children is the simplest scheme - deserializing just replays the same order, consuming null markers to know where to stop
- KEYWORDS - "construct a tree from traversal arrays", "serialize and deserialize a tree"

### Path Sum Problems
- **Root-to-leaf sums to target**: DFS carrying a running sum, check at leaves, backtrack (subtract back out) after returning from each branch
- **Path Sum II (return all paths)**: same DFS, but maintain a running PATH list, append to results at valid leaves, pop after backtracking
- **Path Sum III (path can start/end ANYWHERE, not just root-to-leaf)**: use a prefix-sum HashMap while doing DFS - same idea as "subarray sum equals K" but on a tree instead of an array (`count of valid paths ending here = hashmap[running_sum - target]`)
- KEYWORDS - "path sum", "sum root to leaf", "any path summing to K"

### Structural Comparison Problems
- **Same Tree / Symmetric Tree / Subtree of Another Tree**: all boil down to a recursive "do these 2 (sub)trees match" comparison - Symmetric Tree compares a tree against its OWN mirror (left.left vs right.right, left.right vs right.left)
- **Invert a Binary Tree**: swap `.left` and `.right` at every node, recursively
- **Balanced Binary Tree check**: at each node, the height difference between left and right subtrees must be <= 1, AND both subtrees must themselves be balanced - compute height and check balance in the SAME postorder pass (return -1 as a sentinel the moment imbalance is found, to short-circuit instead of wastefully continuing)
- KEYWORDS - "same tree", "mirror/symmetric tree", "subtree of another tree", "is this tree height-balanced"

### Ancestor Queries (Basic)
- **Lowest Common Ancestor (recursive, single query)**: DFS from the root - if the current node IS one of the 2 targets, return it immediately (don't look further down that branch). Otherwise recurse into both children; if BOTH sides return a non-null result, the current node IS the LCA (the 2 targets are in different subtrees); if only 1 side returns non-null, propagate that result up
- This is NOT the same as the graph-theory LCA techniques (Binary Lifting, Euler Tour + Sparse Table) - those are for REPEATED queries on a static tree at scale, see graphs/README.md - Tree-on-Graph Techniques for those
- KEYWORDS - "lowest common ancestor", single/one-off query on a general binary tree

### Views of a Binary Tree
- **Top View / Bottom View**: assign each node a horizontal distance (HD) relative to root (`root = 0`, `left child = HD-1`, `right child = HD+1`), do a level-order (BFS) traversal, and for each HD keep only the FIRST node seen (top view) or the LAST node seen (bottom view)
- **Left View / Right View**: level-order traversal, keep only the FIRST node (left view) or LAST node (right view) encountered AT EACH DEPTH/level
- **Vertical Order Traversal**: same HD idea as top/bottom view, but group ALL nodes per HD (not just the first/last) - typically also needs a secondary sort by depth, then by value, for nodes sharing the same HD and depth
- **Boundary Traversal**: left boundary (top-down, excluding leaves) + all leaves (left-to-right) + right boundary (bottom-up, excluding leaves) - stitched together, careful with the overlap cases (root as its own boundary, leaf that's already counted as part of a boundary)
- KEYWORDS - "top/bottom/left/right view", "vertical order traversal", "boundary traversal"

### Trie (Prefix Tree)
- A tree where each EDGE represents 1 character - a path from root to a marked node spells out a stored word
- Each node holds a map of `character -> child node` (or a fixed-size array of 26 for lowercase-only alphabets) + an `is_end_of_word` flag
- **Insert**: walk/create nodes character by character, mark `is_end_of_word = True` at the last character
- **Search**: walk character by character, fail if any character's child doesn't exist, succeed only if you reach the end AND `is_end_of_word` is True
- **startsWith (prefix search)**: same walk, but don't check `is_end_of_word` - just confirm the path exists
  ```
  class TrieNode:
      def __init__(self):
          self.children = {}
          self.is_end = False

  def insert(root, word):
      node = root
      for ch in word:
          if ch not in node.children:
              node.children[ch] = TrieNode()
          node = node.children[ch]
      node.is_end = True
  ```
- KEYWORDS - "prefix", "autocomplete", "starts with", "dictionary of words", word search on a grid (Trie + backtracking to prune dead-end paths early)

### Segment Tree
- Answers RANGE queries (sum/min/max over `[L, R]`) with a POINT UPDATE, both in O(log n) - useful when the array changes frequently and you can't afford to recompute a prefix-sum array from scratch each time
- Stored as an array (like a heap) - node at index `i` covers a range, its children at `2*i` and `2*i+1` cover the left and right halves of that range
- **Build**: recursively split the range in half until you hit single elements (leaves), combine children's results going back up - O(n)
- **Query(L, R)**: recursively check if the current node's range is fully inside, fully outside, or partially overlapping `[L, R]` - fully inside returns immediately, fully outside returns the identity value (0 for sum, +inf for min), partial overlap recurses into both children
- **Update(index, value)**: walk down to the leaf for that index, update it, then recompute every ancestor on the way back up
- KEYWORDS - "range sum/min/max query", "mutable array with repeated range queries"

### Fenwick Tree (Binary Indexed Tree)
- A simpler, more compact alternative to a Segment Tree, but ONLY for PREFIX operations (sum, primarily) - can't directly do range MIN/MAX like a Segment Tree can
- Each index stores a partial sum covering a range determined by the LOWEST SET BIT of that index (`i & (-i)`)
- **Update(index, delta)**: repeatedly add `delta`, then move to `index += (index & -index)` until past the end
- **Prefix Query(index)**: repeatedly add the current value, then move to `index -= (index & -index)` until you reach 0
- Both operations are O(log n), and the implementation is notably shorter than a Segment Tree's
- KEYWORDS - "prefix sum with updates", "count of smaller/larger elements after this index" (often solved via a Fenwick Tree over ranks)

---------

## Practice Questions

### Concept Set 1 (Do in order) - Traversals
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Binary Tree Inorder Traversal (Recursive + Iterative) | Amazon, Microsoft, Google, Meta | [LeetCode 94](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/01_binary_tree_inorder_traversal.py) |
| 2 | Binary Tree Level Order Traversal | Amazon, Microsoft, Google, Meta | [LeetCode 102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/04_binary_tree_level_order_traversal.py) |
| 3 | Morris Inorder Traversal (O(1) Space) | Amazon, Microsoft, Google | [GFG](https://www.geeksforgeeks.org/dsa/morris-traversal-for-preorder/) | 🔲 TODO - not built yet (05_morris_inorder_traversal.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Binary Tree Preorder Traversal | Amazon, Microsoft | [LeetCode 144](https://leetcode.com/problems/binary-tree-preorder-traversal/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/02_binary_tree_preorder_traversal.py) |
| 2 | Binary Tree Postorder Traversal | Amazon, Microsoft | [LeetCode 145](https://leetcode.com/problems/binary-tree-postorder-traversal/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/03_binary_tree_postorder_traversal.py) |
| 3 | N-ary Tree Preorder Traversal | Amazon, Google | [LeetCode 589](https://leetcode.com/problems/n-ary-tree-preorder-traversal/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/37_n_ary_tree_preorder_traversal.py) |
| 4 | Maximum Depth of N-ary Tree | Amazon, Google | [LeetCode 559](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/38_max_depth_of_n_ary_tree.py) |

-------

### Concept Set 2 (Do in order) - Binary Search Tree
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Validate Binary Search Tree | Amazon, Microsoft, Google, Meta | [LeetCode 98](https://leetcode.com/problems/validate-binary-search-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/06_validate_bst.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Insert into a Binary Search Tree | Amazon, Microsoft | [LeetCode 701](https://leetcode.com/problems/insert-into-a-binary-search-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/07_insert_into_bst.py) |
| 2 | Delete Node in a BST | Amazon, Microsoft, Google | [LeetCode 450](https://leetcode.com/problems/delete-node-in-a-bst/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/08_delete_node_in_bst.py) |
| 3 | Kth Smallest Element in a BST | Amazon, Microsoft, Google | [LeetCode 230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/09_kth_smallest_in_bst.py) |
| 4 | Convert BST to Sorted Doubly Linked List | Amazon, Google, Microsoft | [LeetCode 426](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/10_bst_to_sorted_doubly_linked_list.py) |
| 5 | Lowest Common Ancestor of a BST | Amazon, Microsoft, Google | [LeetCode 235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/34_lca_of_bst.py) |
| 6 | Largest BST in Binary Tree | Amazon, Google, Microsoft | [GFG](https://www.geeksforgeeks.org/problems/largest-bst/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/39_largest_bst_in_binary_tree.py) |

-------

### Concept Set 3 (Do in order) - Tree Construction
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Construct Binary Tree from Preorder and Inorder Traversal | Amazon, Microsoft, Google, Meta | [LeetCode 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/11_construct_tree_from_preorder_inorder.py) |
| 2 | Serialize and Deserialize Binary Tree | Amazon, Microsoft, Google, Meta | [LeetCode 297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | 🔲 TODO - not built yet (13_serialize_deserialize_binary_tree.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Construct Binary Tree from Postorder and Inorder Traversal | Amazon, Microsoft | [LeetCode 106](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/12_construct_tree_from_postorder_inorder.py) |

-------

### Concept Set 4 (Do in order) - Path Sum
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Path Sum | Amazon, Microsoft, Google | [LeetCode 112](https://leetcode.com/problems/path-sum/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/14_path_sum.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Path Sum II | Amazon, Microsoft, Google | [LeetCode 113](https://leetcode.com/problems/path-sum-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/15_path_sum_ii.py) |
| 2 | Path Sum III | Amazon, Microsoft, Google, Meta | [LeetCode 437](https://leetcode.com/problems/path-sum-iii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/16_path_sum_iii.py) |
| 3 | Sum Root to Leaf Numbers | Amazon, Microsoft | [LeetCode 129](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/17_sum_root_to_leaf_numbers.py) |

-------

### Concept Set 5 (Do in order) - Structural Comparison
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Invert Binary Tree | Amazon, Google, Microsoft | [LeetCode 226](https://leetcode.com/problems/invert-binary-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/18_invert_binary_tree.py) |
| 2 | Balanced Binary Tree | Amazon, Microsoft, Google | [LeetCode 110](https://leetcode.com/problems/balanced-binary-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/22_balanced_binary_tree.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Same Tree | Amazon, Microsoft | [LeetCode 100](https://leetcode.com/problems/same-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/20_same_tree.py) |
| 2 | Symmetric Tree | Amazon, Microsoft, Google | [LeetCode 101](https://leetcode.com/problems/symmetric-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/19_symmetric_tree.py) |
| 3 | Subtree of Another Tree | Amazon, Microsoft, Google | [LeetCode 572](https://leetcode.com/problems/subtree-of-another-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/21_subtree_of_another_tree.py) |

-------

### Concept Set 6 (Do in order) - Views & Projections
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Top View of Binary Tree | Amazon, Microsoft | [GFG](https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/23_top_view_of_binary_tree.py) |
| 2 | Vertical Order Traversal of a Binary Tree | Amazon, Microsoft, Google | [LeetCode 987](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/27_vertical_order_traversal.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Bottom View of Binary Tree | Amazon, Microsoft | [GFG](https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/24_bottom_view_of_binary_tree.py) |
| 2 | Binary Tree Left Side View (also covers Right View) | Amazon, Microsoft, Google, Meta | [LeetCode 199](https://leetcode.com/problems/binary-tree-right-side-view/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/26_right_view_of_binary_tree.py) |
| 3 | Boundary Traversal of Binary Tree | Amazon, Microsoft | [GFG](https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/28_boundary_traversal.py) |

-------

### Concept Set 7 (Do in order) - Trie
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Implement Trie (Prefix Tree) | Amazon, Microsoft, Google, Meta | [LeetCode 208](https://leetcode.com/problems/implement-trie-prefix-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/29_implement_trie.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Word Search II (Trie + Backtracking) | Amazon, Microsoft, Google, Meta | [LeetCode 212](https://leetcode.com/problems/word-search-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/30_word_search_ii_trie_backtracking.py) |
| 2 | Longest Word in Dictionary | Amazon, Google | [LeetCode 720](https://leetcode.com/problems/longest-word-in-dictionary/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/31_longest_word_in_dictionary.py) |

-------

### Concept Set 8 (Do in order) - Segment Tree / Fenwick Tree
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Range Sum Query - Mutable (Segment Tree) | Amazon, Google, Microsoft | [LeetCode 307](https://leetcode.com/problems/range-sum-query-mutable/) | 🔲 TODO - not built yet (32_range_sum_query_mutable_segment_tree.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Count of Smaller Numbers After Self (Fenwick Tree) | Amazon, Google | [LeetCode 315](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | 🔲 TODO - not built yet (33_count_of_smaller_numbers_after_self_fenwick.py) |

---------

### Concept Set 9 (Do in order) - Multi-Source BFS on Trees
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Minimum Time to Burn a Binary Tree from a Given Node | Amazon, Google, Microsoft | [GFG](https://www.geeksforgeeks.org/problems/burning-tree/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/40_minimum_time_to_burn_binary_tree.py) |

---------

### Concept Set 10 (Do in order) - Ancestor Queries (Basic)
- This is the BASIC recursive LCA - for the advanced binary-lifting / sparse-table version (needed for repeated queries at scale), see graphs/README.md - Tree-on-Graph Techniques
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Lowest Common Ancestor of a Binary Tree | Amazon, Microsoft, Google, Meta | [LeetCode 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/trees/35_lca_of_binary_tree.py) |

---------

## Important Points
- Inorder traversal being sorted is ONLY true for a BST - don't assume it for a general binary tree
- Most "hard" tree problems are just a normal traversal (pre/in/post/level) with 1 extra piece of state carried along (a running sum, a depth counter, a parent pointer, a column index) - identify the base traversal first, then figure out what extra state the specific problem needs
- For Diameter, LCA (advanced/binary lifting), Rerooting, and DP-on-Trees (House Robber III, Max Path Sum) - see graphs/README.md and dynamic-programming/README.md respectively, not duplicated here
