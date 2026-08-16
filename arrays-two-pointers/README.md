# Arrays & Two Pointers

## How to Identify
- Sorted (or sortable) array + "find a pair/triplet/quadruplet that..." -> Two Pointers
- "Subarray" + "sum equals/at most/at least K" -> Prefix Sum or Sliding Window (see sliding-window/README.md for the window version)
- Array of `1..n` range values, "find missing/duplicate" -> Cyclic Sort
- "In-place", "O(1) extra space" -> almost always a two-pointer or index-manipulation trick

---------

## Keyword → Technique Cheat Sheet
| Keywords in Question | Technique |
|---|---|
| Sorted array, find a pair summing to target | Two Pointers (opposite ends) |
| Find a triplet/quadruplet summing to target | Sort + Two Pointers (fix 1-2 elements, two-pointer the rest) |
| Container/area maximization between 2 lines | Two Pointers (move the shorter side) |
| Remove/overwrite elements in-place, keep relative order | Two Pointers (slow write index, fast read index) |
| 3-way partition (0s, 1s, 2s / low, mid, high) | Dutch National Flag (3 pointers) |
| Subarray sum equals K (NOT contiguous constraint on window growth) | Prefix Sum + HashMap |
| Product/sum of array except self | Prefix + Suffix pass (no division needed) |
| Array contains `1..n`, find missing/duplicate in O(n)/O(1) | Cyclic Sort (place each number at its "home" index) |
| Repeated rectangular region sum queries on a 2D grid | 2D Prefix Sum (precompute once, O(1) per query) |
| Next lexicographic permutation | Next Permutation algorithm (suffix + swap + reverse) |
| Merge/overlap of ranges | see greedy/README.md (sort by start, merge greedily) |
| Max subarray sum (contiguous) | see dynamic-programming/README.md - Kadane's Algorithm |
| Find duplicate using pointer-chasing, not extra space | see linked-list/README.md - Floyd's Cycle Detection (array-as-implicit-linked-list trick) |

---------

## Core Concepts

### Two Pointers - Opposite Ends (Sorted Array)
- Start 1 pointer at index 0, the other at the last index, move them TOWARD each other based on a comparison with the target
- **2Sum on a sorted array**: if `arr[left] + arr[right] > target`, move `right` left (need a smaller sum); if `< target`, move `left` right; if equal, found it
- **3Sum**: fix 1 element with a loop, then run the 2-pointer technique on the rest of the array for the remaining 2 - sort first (O(n log n)), then O(n) two-pointer per fixed element = O(n^2) total. SKIP DUPLICATES at both the outer loop and the inner two-pointer to avoid duplicate triplets in the output
- **4Sum**: same idea, fix 2 elements with nested loops, two-pointer the remaining 2 - O(n^3)
- **Container With Most Water**: 2 pointers at both ends, area is bounded by the SHORTER wall - always move the pointer at the shorter wall inward (moving the taller one can only shrink width without ever helping height, so it's provably never useful)
- KEYWORDS - "pair/triplet/quadruplet summing to target", "maximize area/volume between 2 boundaries"

### Two Pointers - Same Direction (In-Place Array Manipulation)
- A SLOW pointer marks "the next valid write position," a FAST pointer scans ahead
- **Remove Duplicates from Sorted Array**: fast pointer scans for new values, slow pointer only advances (and writes) when a genuinely new value is found
- **Move Zeroes**: slow pointer tracks where the next non-zero should go, fast pointer scans - swap when fast finds a non-zero
- **Dutch National Flag (Sort Colors)**: 3 pointers - `low` (boundary for 0s), `mid` (current element), `high` (boundary for 2s). Swap and advance pointers based on whether `arr[mid]` is 0, 1, or 2 - single pass, O(1) space, no counting needed
  ```
  low, mid, high = 0, 0, len(arr) - 1
  while mid <= high:
      if arr[mid] == 0:
          arr[low], arr[mid] = arr[mid], arr[low]
          low += 1; mid += 1
      elif arr[mid] == 1:
          mid += 1
      else:  # arr[mid] == 2
          arr[mid], arr[high] = arr[high], arr[mid]
          high -= 1   # do NOT increment mid here - the swapped-in value from high is unchecked
  ```
- **Next Permutation (genuinely non-obvious, SDE3-level expectation)**: find the rearrangement that is the NEXT one in lexicographic order, in-place, O(1) space
  1. Scan from the right, find the first index `i` where `arr[i] < arr[i+1]` (the first "descent" from the right - if none exists, the array is the last permutation, reverse the whole thing)
  2. Scan from the right again, find the first index `j > i` where `arr[j] > arr[i]`
  3. Swap `arr[i]` and `arr[j]`
  4. Reverse everything after index `i` (the suffix was in descending order, reversing makes it the smallest possible arrangement)
- KEYWORDS - "remove/modify array in-place", "sort an array of 3 distinct values in one pass", "next lexicographic permutation"

### Prefix Sum
- Precompute `prefix[i]` = sum of `arr[0..i-1]`, so any range sum `[L, R]` = `prefix[R+1] - prefix[L]` in O(1) after O(n) preprocessing
- **Subarray Sum Equals K**: as you build the running prefix sum left to right, check a HashMap for `(running_sum - K)` - if it exists, you've found a subarray ending here that sums to K. Store `prefix_sum -> count of times seen` as you go (this is the array-domain twin of Path Sum III in trees/README.md)
- **Product of Array Except Self**: do 1 pass accumulating a running PREFIX product, then a second pass (often right-to-left) accumulating a running SUFFIX product, multiplying into the result array - avoids division entirely (important since division breaks if any element is 0)
- KEYWORDS - "subarray sum equals K", "product/sum of array except self", "range sum query on an immutable array"

### 2D Prefix Sum
- Extends the 1D idea to a grid: `prefix[r][c]` = sum of EVERYTHING in the rectangle from `(0,0)` to `(r-1,c-1)`
- Build it with **inclusion-exclusion** (the part people get wrong): `prefix[r][c] = matrix[r-1][c-1] + prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1]` - you add the row-above and column-left sums, but the top-left corner got counted in BOTH of those, so subtract it back out once
  ```
  rows, cols = len(matrix), len(matrix[0])
  prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
  for r in range(1, rows + 1):
      for c in range(1, cols + 1):
          prefix[r][c] = (matrix[r-1][c-1]
                           + prefix[r-1][c]
                           + prefix[r][c-1]
                           - prefix[r-1][c-1])
  ```
- **Query any rectangle `(r1,c1)` to `(r2,c2)`, inclusive, in O(1)** - same inclusion-exclusion idea in reverse: take the full rectangle from the origin, then subtract the strip above and the strip to the left, then add back the corner you subtracted twice
  ```
  def region_sum(r1, c1, r2, c2):
      return (prefix[r2+1][c2+1]
              - prefix[r1][c2+1]
              - prefix[r2+1][c1]
              + prefix[r1][c1])
  ```
- Using a `(rows+1) x (cols+1)` grid (1-indexed, with a padding row/column of zeros) avoids special-casing r=0 or c=0 in every query - worth doing by default rather than fighting boundary conditions inline
- **Number of Submatrices That Sum to Target / Max Sum of Rectangle No Larger Than K (hard variants)**: fix a pair of ROW boundaries, collapse everything between them into a 1D array of column sums (using the 2D prefix sum for O(1) collapsing), then run the exact 1D "subarray sum equals K" technique (HashMap of prefix sums) on that collapsed row - this is the single most common "hard" 2D prefix sum trick: reduce 2D to repeated 1D
- KEYWORDS - "sum of a submatrix/rectangle", "repeated range queries on a 2D grid", "immutable matrix, many region sum queries"

### Cyclic Sort
- Used specifically when array values are constrained to a known range like `1..n` or `0..n-1` - each value has a "home index" it belongs at
- Walk the array, and whenever `arr[i]` isn't at its home index (`arr[i] != i` or `arr[i]-1`, depending on indexing), SWAP it to its home index and re-check the same position (don't advance `i` yet) - repeat until `arr[i]` is in place, then move on
- After 1 pass, any index `i` where `arr[i] != i+1` reveals a missing or duplicate number in O(n) time, O(1) extra space
- **First Missing Positive (the hardest common variant)**: same cyclic sort idea, but ignore/skip values outside `[1, n]` range (negatives, zeros, values > n can never be "the answer" so don't bother placing them) - after sorting what's placeable, the first index where `arr[i] != i+1` is the answer; if all match, the answer is `n+1`
- KEYWORDS - "array contains values 1 to n", "find the missing/duplicate number in O(n) time O(1) space"

---------

## Practice Questions

### Concept Set 1 (Do in order) - Two Pointers (Opposite Ends)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Two Sum II - Input Array Is Sorted | Amazon, Microsoft, Google | [LeetCode 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/01_two_sum_ii_sorted.py) |
| 2 | Container With Most Water | Amazon, Microsoft, Google, Meta | [LeetCode 11](https://leetcode.com/problems/container-with-most-water/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/02_container_with_most_water.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | 3Sum | Amazon, Microsoft, Google, Meta | [LeetCode 15](https://leetcode.com/problems/3sum/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/tree/main/arrays-two-pointers) |
| 2 | 3Sum Closest | Amazon, Microsoft | [LeetCode 16](https://leetcode.com/problems/3sum-closest/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/04_3sum_closest.py) |
| 3 | 4Sum | Amazon, Microsoft | [LeetCode 18](https://leetcode.com/problems/4sum/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/05_4sum.py) |
| 4 | Trapping Rain Water (Two-Pointer Approach) | Amazon, Microsoft, Google, Meta | [LeetCode 42](https://leetcode.com/problems/trapping-rain-water/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/06_trapping_rain_water_two_pointer.py) |
| 5 | Valid Palindrome | Amazon, Microsoft, Meta | [LeetCode 125](https://leetcode.com/problems/valid-palindrome/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/07_valid_palindrome.py) |

-------

### Concept Set 2 (Do in order) - In-Place Manipulation
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Remove Duplicates from Sorted Array | Amazon, Microsoft | [LeetCode 26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/08_remove_duplicates_from_sorted_array.py) |
| 2 | Sort Colors (Dutch National Flag) | Amazon, Microsoft, Google, Meta | [LeetCode 75](https://leetcode.com/problems/sort-colors/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/10_sort_colors_dutch_flag.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Move Zeroes | Amazon, Microsoft, Google, Meta | [LeetCode 283](https://leetcode.com/problems/move-zeroes/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/09_move_zeroes.py) |
| 2 | Next Permutation | Amazon, Microsoft, Google, Meta | [LeetCode 31](https://leetcode.com/problems/next-permutation/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/11_next_permutation.py) |

-------

### Concept Set 3 (Do in order) - Prefix Sum
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | 1-D prefix sum | Amazon, Microsoft, Google, Meta | [GFG](https://www.geeksforgeeks.org/problems/1-d-prefix-sum/1) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/21_1d_prefix_sum.py) |
| 2 | 2D Submatrix Sum Queries | Amazon, Microsoft, Google, Meta | [GFG](https://www.geeksforgeeks.org/problems/2d-submatrix-sum-queries/1) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/22_2d_matrix_sum_queries.py) |
| 3 | Range Sum Query 2D - Immutable | Amazon, Microsoft, Google, Meta | [LeetCode 304](https://leetcode.com/problems/range-sum-query-2d-immutable/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/23_range_sum_query_2d_immutable.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Subarray Sum Equals K | Amazon, Microsoft, Google, Meta | [LeetCode 560](https://leetcode.com/problems/subarray-sum-equals-k/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/12_subarray_sum_equals_k.py) |
| 2 | Product of Array Except Self | Amazon, Microsoft, Google, Meta | [LeetCode 238](https://leetcode.com/problems/product-of-array-except-self/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/13_product_of_array_except_self.py) |
| 3 | Continuous Subarray Sum | Amazon, Google | [LeetCode 523](https://leetcode.com/problems/continuous-subarray-sum/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/14_continuous_subarray_sum.py) |
| 4 | Range Sum Query - Immutable | Amazon, Microsoft | [LeetCode 303](https://leetcode.com/problems/range-sum-query-immutable/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/15_range_sum_query_immutable.py) |
| 5 | Matrix Block Sum | Amazon, Google | [LeetCode 1314](https://leetcode.com/problems/matrix-block-sum/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/24_matrix_block_sum.py) |
| 6 | Number of Submatrices That Sum to Target | Amazon, Google | [LeetCode 1074](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/25_number_of_submatrices_that_sum_to_target.py) |
| 7 | Max Sum of Rectangle No Larger Than K | Amazon, Google | [LeetCode 363](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/) | 🔲 TODO - not built yet (26_max_sum_of_rectangle_no_larger_than_k.py) |

-------

### Concept Set 4 (Do in order) - Cyclic Sort
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Cyclic Sort | Amazon, Microsoft, Google | [GFG](https://www.geeksforgeeks.org/dsa/cycle-sort/) | 🔲 TODO - not built yet (20_cycle_sort.py) |


### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Find the Duplicate Number | Amazon, Microsoft, Google | [LeetCode 287](https://leetcode.com/problems/find-the-duplicate-number/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/arrays-two-pointers/16_find_the_duplicate_number.py) |
| 2 | Missing Number | Amazon, Microsoft | [LeetCode 268](https://leetcode.com/problems/missing-number/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/arrays-two-pointers/18_missing_number.py) |
| 3 | Find All Duplicates in an Array | Amazon, Microsoft | [LeetCode 442](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/arrays-two-pointers/19_find_all_duplicates_in_an_array.py) |
| 4 | First Missing Positive | Amazon, Microsoft, Google, Meta | [LeetCode 41](https://leetcode.com/problems/first-missing-positive/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/arrays-two-pointers/17_first_missing_positive.py) |


---------

## Important Points
- Sort FIRST is the unlock for most two-pointer problems on unsorted input - if a problem seems to need nested loops, ask whether sorting first turns it into a two-pointer sweep instead (O(n log n) vs O(n^2)/O(n^3) naive)
- Watch for duplicate handling in 3Sum/4Sum - skipping duplicates correctly (both in the outer fixed-element loop AND inside the two-pointer sweep) is where most bugs live
- "O(1) extra space" in the problem statement is a strong signal you're expected to mutate the input array itself (two-pointer swaps, cyclic sort) rather than build a new structure
