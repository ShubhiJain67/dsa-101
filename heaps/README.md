# Heaps (Priority Queue)

- A complete binary tree stored in an ARRAY (no actual node/pointer objects needed) where every parent is smaller (min-heap) or larger (max-heap) than its children
- Gives O(log n) insert/remove of the min (or max) and O(1) peek - the go-to structure whenever you repeatedly need "the smallest/largest remaining item," not just once

## How to Identify a Heap Question
- "Kth largest/smallest", "top K", "closest K"
- "Median of a stream" (data arriving continuously, need a running median)
- "Merge K sorted ___"
- "Schedule with priority/cooldown"
- Any time you'd otherwise re-sort the whole collection every time the "next best" item changes

---------

## Keyword → Technique Cheat Sheet
| Keywords in Question | Technique |
|---|---|
| Kth largest element | Min-heap of size K (keep only the K largest seen so far, root = the answer) |
| Kth smallest element | Max-heap of size K (keep only the K smallest seen so far, root = the answer) |
| Top K frequent elements | HashMap for frequency + heap of size K on frequency |
| K closest points/elements | Max-heap of size K on distance |
| Median of a data stream | Two Heaps (max-heap for lower half, min-heap for upper half) |
| Merge K sorted lists/arrays | Min-heap holding the current head of each list/array |
| Schedule tasks with a cooldown | Max-heap (most frequent task next) + a cooldown queue |
| Meeting rooms / interval overlap count | Min-heap of end times |
| Smallest range covering elements from K lists | Min-heap across all K lists + track the current max |

---------

## Core Concepts

### Heap Mechanics (Array-Based Representation)
- Stored in a plain array - for a node at index `i`: parent = `(i-1)//2`, left child = `2*i+1`, right child = `2*i+2`
- **Insert**: append to the end of the array, then "sift UP" - swap with parent while the heap property is violated
- **Extract min/max (root)**: swap the root with the LAST element, remove the last element (was the root), then "sift DOWN" the new root - swap with the smaller (min-heap) or larger (max-heap) child while violated
- **Build a heap from an array in O(n)** (not O(n log n)) - sift-down starting from the LAST non-leaf node backward to the root (leaf nodes are already valid heaps of size 1, so skip them)
- **Heap Sort**: build a max-heap, repeatedly swap root with the last unsorted element and sift-down - O(n log n), in-place, but NOT stable
- Most languages give you this via a library (Python's `heapq` is a MIN-heap only - negate values for a max-heap)
- KEYWORDS - implementing a heap from scratch is rare in interviews, but knowing sift-up/sift-down cold matters for reasoning about complexity

### Top-K Pattern (the most common heap use case)
- **"K largest" -> use a MIN-heap of size K**: push each element, if the heap exceeds size K, pop the smallest - whatever survives at the end are the K largest, and the ROOT is specifically the Kth largest
- **"K smallest" -> use a MAX-heap of size K** (mirror logic)
- The counterintuitive part: for "K LARGEST" you use a MIN-heap, not a max-heap - the min-heap lets you cheaply evict the smallest of your current top-K candidates whenever a bigger one shows up
- TC - O(n log K), better than sorting the whole array (O(n log n)) when K is much smaller than n
- KEYWORDS - "kth largest/smallest", "top K", "K closest"

### Two-Heap Technique (Running Median)
- Maintain 2 heaps: a MAX-heap for the LOWER half of numbers seen so far, a MIN-heap for the UPPER half
- **Balancing rule**: keep the sizes equal, or the max-heap (lower half) exactly 1 larger - this keeps the median always accessible in O(1) (either the max-heap's root, or the average of both roots)
- On inserting a new number: push it to the appropriate heap based on comparison with the max-heap's root, then REBALANCE if sizes drift more than 1 apart (pop from the bigger heap, push to the smaller one)
  ```
  # maxHeap = lower half (negate values in Python since heapq is min-only)
  # minHeap = upper half
  def add_num(num):
      if not maxHeap or num <= -maxHeap[0]:
          heappush(maxHeap, -num)
      else:
          heappush(minHeap, num)
      # rebalance - sizes can differ by at most 1
      if len(maxHeap) > len(minHeap) + 1:
          heappush(minHeap, -heappop(maxHeap))
      elif len(minHeap) > len(maxHeap):
          heappush(maxHeap, -heappop(minHeap))

  def find_median():
      if len(maxHeap) > len(minHeap):
          return -maxHeap[0]
      return (-maxHeap[0] + minHeap[0]) / 2
  ```
- KEYWORDS - "median of a stream", "running median", "median so far"

### Merging with a Heap
- When merging K sorted sources (lists, arrays, streams), DON'T merge them pairwise in a loop (that revisits elements too many times)
- Push the FIRST element of each of the K sources into a min-heap (tagged with which source it came from), repeatedly pop the smallest, push the NEXT element from that same source
- TC - O(N log K) where N = total elements, vastly better than O(N*K) naive merging
- KEYWORDS - "merge K sorted lists/arrays/streams"

### Heap vs Monotonic Deque (know the difference)
- Sliding Window Maximum LOOKS like a heap problem ("max in a window") but a heap can't efficiently REMOVE an element that's slid out of the window (you'd need to know its position, heaps don't support arbitrary removal in O(log n) without extra bookkeeping)
- A MONOTONIC DEQUE (see stacks/README.md) solves this in true O(n) instead - keep it in mind as the better tool for "max/min in a sliding window" specifically
- KEYWORDS - "maximum/minimum in every window of size K" -> reach for monotonic deque, NOT a heap, despite the "max" keyword

---------

## Practice Questions

### Concept Set 1 (Do in order) - Top-K Pattern
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Kth Largest Element in an Array | Amazon, Microsoft, Google, Meta | [LeetCode 215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/01_kth_largest_element_in_array.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Kth Largest Element in a Stream | Amazon, Microsoft | [LeetCode 703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/02_kth_largest_element_in_a_stream.py) |
| 2 | Top K Frequent Elements | Amazon, Microsoft, Google, Meta | [LeetCode 347](https://leetcode.com/problems/top-k-frequent-elements/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/03_top_k_frequent_elements.py) |
| 3 | K Closest Points to Origin | Amazon, Microsoft, Google, Meta | [LeetCode 973](https://leetcode.com/problems/k-closest-points-to-origin/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/04_k_closest_points_to_origin.py) |
| 4 | Kth Smallest Element in a Sorted Matrix | Amazon, Google | [LeetCode 378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/10_kth_smallest_element_in_sorted_matrix.py) |

-------

### Concept Set 2 (Do in order) - Two-Heap Technique
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Find Median from Data Stream | Amazon, Microsoft, Google | [LeetCode 295](https://leetcode.com/problems/find-median-from-data-stream/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/05_find_median_from_data_stream.py) |

-------

### Concept Set 3 (Do in order) - Merging & Scheduling
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Merge K Sorted Lists | Amazon, Microsoft, Google | [LeetCode 23](https://leetcode.com/problems/merge-k-sorted-lists/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/06_merge_k_sorted_lists_heap.py) |
| 2 | Task Scheduler | Amazon, Meta, Google | [LeetCode 621](https://leetcode.com/problems/task-scheduler/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/07_task_scheduler.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Reorganize String | Amazon, Google | [LeetCode 767](https://leetcode.com/problems/reorganize-string/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/08_reorganize_string.py) |
| 2 | Ugly Number II | Amazon, Microsoft | [LeetCode 264](https://leetcode.com/problems/ugly-number-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/09_ugly_number_ii.py) |
| 3 | Meeting Rooms II | Amazon, Microsoft, Google, Meta | [LeetCode 253](https://leetcode.com/problems/meeting-rooms-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/11_meeting_rooms_ii.py) |
| 4 | Smallest Range Covering Elements from K Lists | Google, Amazon | [LeetCode 632](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/12_smallest_range_covering_elements_from_k_lists.py) |
| 5 | Sliding Window Maximum (Monotonic Deque, contrast with heap) | Amazon, Google, Meta | [LeetCode 239](https://leetcode.com/problems/sliding-window-maximum/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/13_sliding_window_maximum_deque.py) |

---------

## Important Points
- Python's `heapq` is MIN-heap only - for a max-heap, push negated values and negate again on pop (easy to forget mid-interview, say it out loud)
- "Top K" almost always means O(n log K), not O(n log n) - if you're sorting the whole array for a top-K question, you're leaving an easy optimization on the table
- Heaps give you the min/max fast, but NOT fast arbitrary search/removal of a middle element - if a problem needs that, a heap alone isn't enough (often paired with a HashMap for lazy deletion, or a different structure entirely)
