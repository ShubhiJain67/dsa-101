# Linked List

- A sequence of nodes, each holding data + a pointer to the next (and previous, for doubly linked)
- No random access (unlike arrays) - to reach node i you MUST walk from the head, that's why most tricks here revolve around clever POINTER MANIPULATION instead of indexing

## How to Identify a Linked List Question
- Explicit `ListNode` / `Node` with a `.next` (and maybe `.prev`) pointer
- "Reverse", "cycle", "middle", "merge sorted lists", "kth from the end"
- Cannot use indexing - only pointer-following - forces O(1) extra space tricks that arrays don't need

---------

## Keyword → Technique Cheat Sheet
| Keywords in Question | Technique |
|---|---|
| Reverse a list (fully or between positions) | Iterative 3-pointer reversal (prev/curr/next) |
| Reverse in groups of K | Recursive reversal + counting K nodes per group |
| Detect a cycle | Floyd's Fast & Slow Pointer |
| Find WHERE the cycle starts | Floyd's + reset-one-pointer-to-head trick |
| Find the middle node | Fast & Slow Pointer (fast moves 2x speed) |
| Kth node from the end | Two pointers with a K-gap between them |
| Merge 2 sorted lists | Dummy node + compare-and-attach |
| Merge K sorted lists | Min-Heap of size K (see heaps/README.md) or divide-and-conquer pairwise merge |
| Check palindrome | Find middle -> reverse 2nd half -> compare |
| Remove duplicates / Nth node | Dummy node to handle head-removal edge case cleanly |
| Clone/copy a list with a random pointer | Interleaving technique (weave copies into the original list) |
| LRU / LFU cache | Doubly Linked List + HashMap |
| Flatten a nested/multilevel list | Recursive DFS-style flatten, similar to tree flattening |
| Add 2 numbers represented as lists | Simulate elementary addition with a carry, digit by digit |
| Sort a linked list in O(n log n) | Merge Sort (no random access, so array-style quicksort/heapsort don't fit naturally) |

---------

## Core Concepts

### Dummy Node Technique
- Create a fake node BEFORE the real head (`dummy.next = head`), do all your operations, return `dummy.next` at the end
- Fixes the annoying "what if I need to remove/change the HEAD itself" edge case - with a dummy node, the head is never a special case, it's just `dummy.next`
- Used in: remove Nth node from end, merge sorted lists, remove duplicates, partition list
- KEYWORDS - basically any problem where the head node might need to change

### Reversal (Iterative 3-Pointer)
- The core mechanic - track `prev`, `curr`, and `next` as you walk the list, flipping each `.next` pointer as you go
  ```
  def reverse(head):
      prev = None
      curr = head
      while curr:
          next_node = curr.next   # save before overwriting
          curr.next = prev        # flip the pointer
          prev = curr             # advance prev
          curr = next_node        # advance curr
      return prev                 # prev is the new head
  ```
- **Reverse in groups of K**: recursively reverse the first K nodes (fail fast / leave as-is if fewer than K remain), then recursively call on the rest and attach it to the tail of the reversed group
- **Reverse between positions L and R**: walk to position L-1, then apply the same 3-pointer reversal only for the L-to-R window, reconnect both ends
- KEYWORDS - "reverse a linked list", "reverse in groups/between positions"

### Fast & Slow Pointers (Floyd's Algorithm)
- 2 pointers, `slow` moves 1 step, `fast` moves 2 steps per iteration
- **Find the middle**: when `fast` reaches the end, `slow` is at the middle (works for both odd/even length with a small boundary tweak)
- **Detect a cycle**: if there's a cycle, `fast` will eventually LAP `slow` and they meet - if `fast` hits `None`, there's no cycle
- **Find WHERE the cycle starts (the non-obvious part)**: once `slow` and `fast` meet inside the cycle, reset ONE pointer back to the `head`, then move BOTH pointers 1 step at a time - they meet exactly at the cycle's start node
  ```
  slow = fast = head
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
          # cycle found - now find the start
          slow = head
          while slow != fast:
              slow = slow.next
              fast = fast.next
          return slow   # start of the cycle
  return None   # no cycle
  ```
- Why the "reset to head" trick works: this is a mathematical property of the meeting point distance relative to the cycle length - worth memorizing the mechanic even if the proof isn't intuitive
- KEYWORDS - "detect a cycle", "find the start of a cycle", "find the middle node"

### Merging Sorted Lists
- **2 lists**: dummy node + walk both lists simultaneously, always attach the smaller head, advance that list - O(n+m)
- **K lists**: DON'T merge them 1-by-1 in a loop (that's O(N*K) where N is total nodes) - instead use a MIN-HEAP holding the current head of each list, pop the smallest, push its `.next` - O(N log K). Alternative: divide-and-conquer pairwise merging, same O(N log K)
- KEYWORDS - "merge sorted lists", "merge k sorted lists/arrays"

### Copy List With Random Pointer (Interleaving Technique)
- Each node has a `.next` AND a `.random` (pointing to ANY node in the list, or null) - naive copying breaks because when you copy node A, its random pointer might point to a node you haven't copied yet
- **The trick**: weave the copied nodes into the original list - `A -> A' -> B -> B' -> C -> C' -> ...`
  1. For each original node, create its copy and insert it right after the original
  2. Now `copy.random = original.random.next` (since the copy of any node sits right after it)
  3. Unweave - separate the interleaved list back into original and copy chains
- Avoids needing a HashMap to track original->copy mappings, though a HashMap approach also works and is simpler to reason about (trade a bit of extra space for a much easier mental model)
- KEYWORDS - "clone/copy a linked list", "random pointer"

### LRU Cache (Doubly Linked List + HashMap)
- Need O(1) for BOTH "get a value" and "move most-recently-used to the front" - a plain array/list can't do both in O(1)
- **HashMap**: `key -> node` for O(1) lookup
- **Doubly Linked List**: maintains USAGE ORDER - most-recently-used at one end, least-recently-used at the other. Doubly linked (not singly) because you need to REMOVE a node from the middle in O(1), which requires knowing its `.prev` too
- On `get(key)`: look up via HashMap, then unlink the node and re-insert it at the "most recent" end
- On `put(key, value)`: if at capacity, remove the node at the "least recent" end (and delete it from the HashMap too), then insert the new node at the "most recent" end
- Use 2 DUMMY nodes (head and tail sentinels) so insert/remove logic never needs a null-check for edge positions
- KEYWORDS - "design a cache", "O(1) get and put", "least recently used"

### Sorting a Linked List
- Merge Sort is the natural fit (O(n log n), no random access needed) - Quick Sort/Heap Sort assume O(1) random access to arbitrary indices, which a linked list doesn't have
- Find the middle (fast/slow pointer), split into 2 halves, recursively sort each half, merge them back (same merge mechanic as "merge 2 sorted lists")
- KEYWORDS - "sort a linked list", specifically asking for O(n log n) time and O(1) or O(log n) space

---------

## Practice Questions

### Concept Set 1 (Do in order) - Reversal
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Reverse Linked List | Amazon, Microsoft, Google, Meta | [LeetCode 206](https://leetcode.com/problems/reverse-linked-list/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/linked-list/01_reverse_linked_list.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Reverse Linked List II (Between Positions) | Amazon, Microsoft | [LeetCode 92](https://leetcode.com/problems/reverse-linked-list-ii/) | 🔲 TODO - not built yet (02_reverse_linked_list_ii_between_positions.py) |
| 2 | Reverse Nodes in K-Group | Amazon, Microsoft, Google | [LeetCode 25](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/linked-list/03_reverse_nodes_in_k_group.py) |
| 3 | Swap Nodes in Pairs | Amazon, Microsoft | [LeetCode 24](https://leetcode.com/problems/swap-nodes-in-pairs/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/linked-list/16_swap_nodes_in_pairs.py) |

-------

### Concept Set 2 (Do in order) - Fast & Slow Pointers
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Linked List Cycle (Detect) (Floyd's Algorithm) | Amazon, Microsoft, Google, Meta | [LeetCode 141](https://leetcode.com/problems/linked-list-cycle/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/linked-list/04_detect_cycle_floyds.py) |
| 2 | Linked List Cycle II (Find Start) | Amazon, Microsoft, Google | [LeetCode 142](https://leetcode.com/problems/linked-list-cycle-ii/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/linked-list/05_detect_cycle_ii_find_start.py) |
| 3 | Middle of the Linked List | Amazon, Microsoft | [LeetCode 876](https://leetcode.com/problems/middle-of-the-linked-list/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/linked-list/06_middle_of_linked_list.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Remove Nth Node From End of List | Amazon, Microsoft, Meta | [LeetCode 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/linked-list/09_remove_nth_node_from_end.py) |
| 2 | Palindrome Linked List | Amazon, Microsoft, Google | [LeetCode 234](https://leetcode.com/problems/palindrome-linked-list/) | 🔲 TODO - not built yet (10_palindrome_linked_list.py) |
| 3 | Intersection of Two Linked Lists | Amazon, Microsoft, Google | [LeetCode 160](https://leetcode.com/problems/intersection-of-two-linked-lists/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/linked-list/11_intersection_of_two_linked_lists.py) |
| 4 | Reorder List | Amazon, Google, Meta | [LeetCode 143](https://leetcode.com/problems/reorder-list/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/linked-list/12_reorder_list.py) |

-------

### Concept Set 3 (Do in order) - Merging
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Merge Two Sorted Lists | Amazon, Microsoft, Google, Meta | [LeetCode 21](https://leetcode.com/problems/merge-two-sorted-lists/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/linked-list/07_merge_two_sorted_lists.py) |
| 2 | Merge K Sorted Lists | Amazon, Microsoft, Google | [LeetCode 23](https://leetcode.com/problems/merge-k-sorted-lists/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/linked-list/08_merge_k_sorted_lists.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Sort List | Amazon, Microsoft, Google | [LeetCode 148](https://leetcode.com/problems/sort-list/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/linked-list/18_sort_list.py) |
| 2 | Odd Even Linked List | Amazon, Microsoft | [LeetCode 328](https://leetcode.com/problems/odd-even-linked-list/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/linked-list/13_odd_even_linked_list.py) |
| 3 | Partition List | Amazon, Microsoft | [LeetCode 86](https://leetcode.com/problems/partition-list/) | 🔲 TODO - not built yet (14_partition_list.py) |
| 4 | Rotate List | Amazon, Microsoft | [LeetCode 61](https://leetcode.com/problems/rotate-list/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/linked-list/15_rotate_list.py) |
| 5 | Add Two Numbers | Amazon, Microsoft, Google, Meta | [LeetCode 2](https://leetcode.com/problems/add-two-numbers/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/linked-list/17_add_two_numbers.py) |

-------

### Concept Set 4 (Do in order) - Design & Advanced Manipulation
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | LRU Cache | Amazon, Microsoft, Google, Meta | [LeetCode 146](https://leetcode.com/problems/lru-cache/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/linked-list/19_lru_cache.py) |
| 2 | Copy List with Random Pointer | Amazon, Microsoft, Google, Meta | [LeetCode 138](https://leetcode.com/problems/copy-list-with-random-pointer/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/linked-list/21_copy_list_with_random_pointer.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | LFU Cache | Amazon, Google | [LeetCode 460](https://leetcode.com/problems/lfu-cache/) | 🔲 TODO - not built yet (20_lfu_cache.py) |
| 2 | Flatten a Multilevel Doubly Linked List | Amazon, Microsoft, Google | [LeetCode 430](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/linked-list/22_flatten_multilevel_doubly_linked_list.py) |

---------

## Important Points
- ALWAYS ask (or state your assumption) whether the list is singly or doubly linked, and whether it's circular - changes which tricks are even available
- Draw the pointers out on paper/whiteboard before coding - linked list bugs are almost always an off-by-one in WHEN you save `next` before overwriting it
- Watch for: empty list, single-node list, and (for cycle/reversal problems) the list being fully circular - these are the edge cases interviewers probe
