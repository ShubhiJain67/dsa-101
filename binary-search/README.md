# Binary Search

- Not just "search a sorted array" - the real SDE3-level skill is recognizing binary search on a SEARCH SPACE that isn't even an array (a range of possible answers), which almost never looks like a binary search problem on first read
- Works whenever the search space has a MONOTONIC PREDICATE - a yes/no condition that flips exactly once as you move across the space (all "no" then all "yes", or vice versa)

## How to Identify
- Sorted array + "find X" / "find first/last occurrence" -> classic binary search
- Sorted array that's been ROTATED -> modified binary search
- "Minimize the maximum" / "maximize the minimum" / "find the smallest value such that condition X holds" -> Binary Search on Answer (the search space is a RANGE OF POSSIBLE ANSWERS, not the input array itself)
- Brute force would be "try every possible answer from low to high and check" -> if checking 1 answer is fast and the checks are monotonic (once it works, everything bigger/smaller also works), binary search the answer instead of trying them all

---------

## Keyword → Technique Cheat Sheet
| Keywords in Question | Technique |
|---|---|
| Find exact target in sorted array | Classic Binary Search |
| Find first/last occurrence of a target | Boundary Binary Search (lower_bound / upper_bound) |
| Sorted array, but ROTATED at some pivot | Modified Binary Search (figure out which half is sorted) |
| Find the peak / local maximum in an array | Binary Search on slope direction |
| "Minimum capacity/speed/time such that task completes within limit" | Binary Search on Answer |
| "Split into groups minimizing the maximum group value" | Binary Search on Answer |
| Find the median of 2 sorted arrays without merging | Binary Search on Partition Point (hard) |
| Search in a 2D sorted matrix | Treat as a flattened 1D array (if fully sorted) or eliminate a row/column per step |

---------

## Core Concepts

### Classic Binary Search & Boundary Search
- Standard binary search: `while low <= high`, check `arr[mid]` against target, move `low` or `high` accordingly
- **First/Last Occurrence (the genuinely useful variant)**: when you find a match, DON'T stop - if searching for the first occurrence, keep searching the LEFT half (`high = mid - 1`) and remember this match as your best-so-far; mirror logic for last occurrence (search the right half instead)
  ```
  def find_first(arr, target):
      low, high, result = 0, len(arr) - 1, -1
      while low <= high:
          mid = (low + high) // 2
          if arr[mid] == target:
              result = mid
              high = mid - 1   # keep searching LEFT for an earlier occurrence
          elif arr[mid] < target:
              low = mid + 1
          else:
              high = mid - 1
      return result
  ```
- KEYWORDS - "find target", "first/last position of element in sorted array"

### Search in a Rotated Sorted Array
- The array is sorted but rotated at an unknown pivot - a plain binary search breaks because `arr[mid]` comparisons no longer cleanly say "go left or right"
- **The key insight**: at least ONE half (left of mid, or right of mid) is ALWAYS properly sorted, even in a rotated array. Figure out which half is sorted first (compare `arr[low]` to `arr[mid]`), then check if the target falls within that sorted half's range - if yes, recurse into it, if no, recurse into the other half
- With DUPLICATES (harder variant): when `arr[low] == arr[mid] == arr[high]`, you can't tell which half is sorted - shrink the search space by 1 from both ends (`low += 1; high -= 1`) and try again, degrading worst-case to O(n) but still correct
- KEYWORDS - "rotated sorted array", "search in rotated array"

### Binary Search on Answer (the signature SDE3-level pattern)
- The search space is NOT the input array - it's the RANGE OF POSSIBLE ANSWERS (e.g. "minimum speed" could range from 1 to max(pile sizes))
- Define a `can_achieve(x)` predicate: "is `x` a valid/sufficient answer?" - this predicate MUST be monotonic (if `x` works, everything bigger also works, or vice versa) for binary search to apply at all
- Binary search over the answer range, using `can_achieve(mid)` to decide which half to keep - converges to the smallest (or largest) valid answer
  ```
  def min_valid_answer(low, high, can_achieve):
      while low < high:
          mid = (low + high) // 2
          if can_achieve(mid):
              high = mid       # mid might BE the answer, keep it in range
          else:
              low = mid + 1    # mid doesn't work, answer must be bigger
      return low
  ```
- **Koko Eating Bananas**: search space = possible eating speeds (1 to max pile size), predicate = "can Koko finish all piles at this speed within H hours?"
- **Capacity to Ship Packages Within D Days**: search space = possible ship capacities, predicate = "can all packages ship within D days at this capacity?"
- **Split Array Largest Sum**: search space = possible "largest subarray sum" values, predicate = "can we split the array into <= K parts where no part exceeds this sum?"
- The hard part is never the binary search loop itself - it's correctly writing the `can_achieve` predicate and confirming it's actually monotonic
- KEYWORDS - "minimize the maximum", "maximize the minimum", "smallest/largest value such that condition holds", "within D days/H hours/K groups"

### Median of Two Sorted Arrays (Hard - Partition-Based Binary Search)
- Goal: find the median of the COMBINED array without actually merging (O(log(min(m,n))) required, not O(m+n))
- Binary search on the PARTITION POINT of the smaller array - for a given partition of array A, the corresponding partition of array B is determined (must total `(m+n+1)//2` elements on the left side combined)
- A partition is correct when `max(left side of A) <= min(right side of B)` AND `max(left side of B) <= min(right side of A)` - binary search the partition point of A until this holds
- Genuinely one of the harder standard interview problems - worth doing once carefully rather than memorizing, since the index bookkeeping (odd vs even total length) is where bugs live
- KEYWORDS - "median of two sorted arrays", explicitly asking for better than O(m+n)

### Binary Search on a 2D Matrix
- If the matrix is FULLY sorted (last element of row i < first element of row i+1), treat it as a flattened 1D array and binary search with `mid -> (mid // cols, mid % cols)` conversion
- If only ROW-sorted and COLUMN-sorted independently (not fully sorted overall), start from the top-right (or bottom-left) corner and eliminate a full row or column per comparison - O(rows + cols), not a true binary search but the same "eliminate half the possibilities" spirit
- KEYWORDS - "search a 2D matrix", "sorted matrix"

---------

## Practice Questions

### Concept Set 1 (Do in order) - Classic & Boundary Search
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Binary Search | Amazon, Microsoft, Google | [LeetCode 704](https://leetcode.com/problems/binary-search/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/binary-search/01_binary_search.py) |
| 2 | Find First and Last Position of Element in Sorted Array | Amazon, Microsoft, Google, Meta | [LeetCode 34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/binary-search/02_find_first_last_position.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Search Insert Position | Amazon, Microsoft | [LeetCode 35](https://leetcode.com/problems/search-insert-position/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/binary-search/03_search_insert_position.py) |
| 2 | Search a 2D Matrix | Amazon, Microsoft, Google | [LeetCode 74](https://leetcode.com/problems/search-a-2d-matrix/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/binary-search/04_search_a_2d_matrix.py) |

-------

### Concept Set 2 (Do in order) - Rotated Array
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Search in Rotated Sorted Array | Amazon, Microsoft, Google, Meta | [LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/binary-search/05_search_in_rotated_sorted_array.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Search in Rotated Sorted Array II (With Duplicates) | Amazon, Microsoft | [LeetCode 81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | [Pyhton](https://github.com/ShubhiJain67/dsa-101/blob/main/binary-search/06_search_in_rotated_sorted_array_ii.py) |
| 2 | Find Minimum in Rotated Sorted Array | Amazon, Microsoft, Google | [LeetCode 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Python](https://github.com/ShubhiJain67/dsa-101/tree/main/binary-search) |
| 3 | Find Peak Element | Amazon, Microsoft, Google | [LeetCode 162](https://leetcode.com/problems/find-peak-element/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/binary-search/08_find_peak_element.py) |

-------

### Concept Set 3 (Do in order) - Binary Search on Answer (SDE3 Signature Pattern)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Koko Eating Bananas | Amazon, Microsoft, Google | [LeetCode 875](https://leetcode.com/problems/koko-eating-bananas/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/binary-search/09_koko_eating_bananas.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Capacity To Ship Packages Within D Days | Amazon, Microsoft, Google | [LeetCode 1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/binary-search/10_capacity_to_ship_packages.py) |
| 2 | Split Array Largest Sum | Amazon, Google | [LeetCode 410](https://leetcode.com/problems/split-array-largest-sum/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/binary-search/11_split_array_largest_sum.py) |
| 3 | Minimum Number of Days to Make m Bouquets | Amazon, Google | [LeetCode 1482](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/binary-search/12_minimum_days_to_make_bouquets.py) |
| 4 | Median of Two Sorted Arrays (Hard) | Amazon, Microsoft, Google, Meta | [LeetCode 4](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔲 TODO - not built yet (13_median_of_two_sorted_arrays.py) |

---------

## Important Points
- Watch the loop boundary convention (`low <= high` vs `low < high`) and whether you use `mid` or `mid +/- 1` when narrowing - pick ONE convention and use it consistently, mixing conventions mid-problem is the #1 source of infinite loops and off-by-one bugs
- For "Binary Search on Answer" problems, always verify the predicate is genuinely MONOTONIC before coding - if it isn't, binary search silently gives a wrong answer with no error
- `mid = low + (high - low) // 2` instead of `(low + high) // 2` avoids integer overflow in languages with fixed-width integers - habit worth having even in Python where it doesn't matter, since it signals awareness
