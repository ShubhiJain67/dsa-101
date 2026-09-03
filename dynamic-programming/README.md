# Dynamic Programming

- It is an "Enhanced Recursion"
- Optimising Recurssion calls
- ### RECURSION + STORAGE

## How to Identify Dynamic Programming?
- There will be a choice (recursion)
- Same Recursion made multiple times
- Will be asking an OPTIMAL ANSWER (maximum value, minimum cost)

------
## CORRECT FLOW - Recursion -> Memorise -> Top Down
------

## General DP Methodology (How to Derive ANY DP Solution)
- **Step 1 - RECURSION**: define the STATE (what changes between calls) + the TRANSITION (the choices) + the BASE CASE
- **Step 2 - MEMOIZE**: add a cache keyed by the state (dict or array) - check the cache before recursing, store the result after
- **Step 3 - TABULATE (bottom-up)**: convert the memo into an array, fill it in an order where dependencies are already computed (usually smallest subproblem first)
- **Step 4 (optional) - SPACE OPTIMIZE**: if `dp[i]` only depends on `dp[i-1]` (or a few previous rows), collapse the array to O(1) or O(k) space
  ```
  # Step 1: Recursion
  def solve(state):
      if base_case: return base_value
      return best(solve(next_state_1), solve(next_state_2), ...)

  # Step 2: Memoization
  memo = {}
  def solve(state):
      if state in memo: return memo[state]
      if base_case: return base_value
      memo[state] = best(solve(next_state_1), solve(next_state_2), ...)
      return memo[state]

  # Step 3: Tabulation
  dp = [base_value] * (n + 1)
  for state in range(1, n + 1):
      dp[state] = best(dp[state - 1], dp[state - 2], ...)
  ```
- This is the METHOD, not a pattern - apply it to identify ANY new DP shape you haven't seen before, not just the named patterns below

## Keyword → Pattern Cheat Sheet
| Keywords in Question | DP Pattern |
|---|---|
| Choose items with weight/value constraint, each item at most once | 0-1 Knapsack |
| Choose items with weight/value constraint, unlimited quantity | Unbounded Knapsack |
| Coin change / rod cutting / combinations with repetition allowed | Unbounded Knapsack |
| 2 strings, common subsequence/substring, convert A to B | LCS Family |
| "Ways to reach step N", "climb stairs", depends only on the last 1-2 states | Linear DP (Fibonacci pattern) |
| Cannot pick 2 ADJACENT elements | Linear DP (House Robber variant) |
| Maximum/minimum sum of a CONTIGUOUS subarray | Kadane's Algorithm |
| Longest increasing/bitonic subsequence (not necessarily contiguous) | LIS |
| Grid traversal, min/max path sum, unique paths, robot moving | DP on Grid |
| "Min cost to merge/partition a range", matrix multiplication order, parenthesization | Interval DP / Matrix Chain Multiplication |
| Tree, cannot pick a node AND its parent/child together, max path sum in a tree | DP on Trees |
| n <= ~20, assign/select a SUBSET of items, "visit all" | Bitmask DP |
| Count/sum numbers in a range with a digit-based property | Digit DP |
| Buy/sell stock, K transactions, cooldown, transaction fee | DP on Stocks (State Machine DP) |
| Pattern matching with wildcards (`*`, `?`) or regex | String Matching DP |
| "Can this string be segmented into dictionary words" | Word Break |
| Minimize worst-case number of trials/attempts | Search Space DP (Egg Drop style) |

------

## Knapsack Problems
```
Input - Items where each item has a value and a Target Value
Choice of selection of Item
```

### Fractional Knapsack -> Greedy Problem
Item can be choosen fractionally
1 Item can be choosen at max 1 times

### Unboaunded Knapsack
- An item can be choosen multiple times 
- Knapsack with duplicate items
- Item is Marked as processed ONLY when decoded to not take it

### 0-1 KnapSack
- Item CANNOT be choosen fractionally, it is choosen or not
- 1 Item can be choosen at max 1 times
- Matrix usually becomes of n+1 * sum+1
- Item is marked processed if we take it or no take it
- Type 
  - Subset Sum
  - Equal Sum Partition
  - Count of subset sum
  - Mnimum subset sum difference
  - Target Sum
  - Number of Subset sum with given difference

------

## LCS Family (Longest Common Subsequence / Substring)
```
Input - 2 strings/arrays
Choice - for each pair of indices (i, j), does s1[i] match s2[j] or not
```
- **State**: `dp[i][j]` = answer considering the first i characters of s1 and first j characters of s2
- **LCS transition**: if `s1[i-1] == s2[j-1]` -> `dp[i][j] = 1 + dp[i-1][j-1]` (character matches, extend the subsequence), else `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` (skip 1 character from either string)
- **Longest Common SUBSTRING transition** (must be CONTIGUOUS, different from subsequence): if match -> `dp[i][j] = 1 + dp[i-1][j-1]`, else `dp[i][j] = 0` (a mismatch breaks the substring entirely, no "skip and continue" like subsequence)
- Base case: `dp[0][j] = dp[i][0] = 0` (empty string has 0 common length with anything)
- Answer for LCS = `dp[n][m]`, answer for substring = `max(dp[i][j])` over ALL i, j (best substring might not end at the last index)
- Type
  - Print LCS (backtrack through the dp table instead of just reading the length)
  - Shortest Common Supersequence
  - Min Insertions/Deletions to convert A to B
  - Longest Repeating Subsequence (LCS of a string with itself, with the constraint i != j)
  - Longest Palindromic Subsequence (LCS of the string with its own reverse)
  - Edit Distance style problems

## Linear DP (Fibonacci / "Depends on Last K States")
- **State**: `dp[i]` = answer considering the first i elements/steps
- Transition looks back at a FIXED small window (`dp[i-1]`, `dp[i-2]`, ...) - not the whole array like Knapsack
- Classic shape: Climbing Stairs, House Robber (cannot pick 2 adjacent), Decode Ways, Tiling problems
- Almost always space-optimizable to O(1) since only the last 1-2 states matter
- KEYWORDS - "ways to reach step N", "cannot pick 2 adjacent elements", "ways to decode/tile"

## Kadane's Algorithm (Maximum Subarray Sum)
- Finds the max sum of a CONTIGUOUS subarray in O(n)
- `dp[i]` = max subarray sum ENDING at index i = `max(arr[i], dp[i-1] + arr[i])`
- If `dp[i-1]` is negative, it only hurts you - start fresh from `arr[i]` instead
- Answer = `max(dp[i])` over ALL i, NOT `dp[n-1]` (the best subarray might not end at the last index)
- Extends to: MAX PRODUCT subarray (track both running max AND running min, since a negative * negative can flip into the new max), CIRCULAR subarray (`total sum - min subarray`, watch the all-negative edge case)
- KEYWORDS - "maximum sum contiguous subarray", "maximum subarray"

## Longest Increasing Subsequence (LIS)
- `dp[i]` = length of the LIS ENDING at index i
- O(n^2): `dp[i] = max(dp[j] + 1) for all j < i where arr[j] < arr[i]`
- **O(n log n) - Patience Sorting / Binary Search trick (the non-obvious part)**:
  - Maintain a `tails[]` array - `tails[k]` = smallest possible tail value of an increasing subsequence of length k+1
  - For each number, binary search `tails[]` for the first element >= number and replace it (or append if none found)
  - Final `len(tails)` = LIS length (`tails` is NOT the actual subsequence, just a proxy for lengths)
  ```
  tails = []
  for num in arr:
      idx = bisect_left(tails, num)
      if idx == len(tails): tails.append(num)
      else: tails[idx] = num
  answer = len(tails)
  ```
- KEYWORDS - "longest increasing subsequence", "longest bitonic/decreasing subsequence", envelope/box-stacking-style problems (LIS in disguise, usually after sorting)

## DP on Grid
- `dp[r][c]` = answer considering the grid up to cell (r, c)
- Transition usually comes from `dp[r-1][c]` and `dp[r][c-1]` (came from above or left)
- Watch boundaries (row 0 / column 0 have only 1 incoming direction) and obstacles (set `dp[r][c] = 0`/blocked or skip)
- KEYWORDS - "unique paths", "minimum path sum", "grid", "robot moving right/down"

## Interval DP / Matrix Chain Multiplication
- `dp[i][j]` = answer for the SUBARRAY/RANGE from i to j
- Transition: try every possible SPLIT POINT k between i and j, combine the 2 halves - `dp[i][j] = min/max over k of (dp[i][k] + dp[k+1][j] + cost_to_merge)`
- Iterate by INCREASING RANGE LENGTH (small ranges first - bigger ranges depend on smaller ranges inside them)
- KEYWORDS - "matrix chain multiplication", "minimum cost to merge/partition a range", "min cuts for palindrome partition", "burst balloons", parenthesization problems

## DP on Trees
- `dp[node]` = answer for the SUBTREE rooted at node, usually as a pair: `(answer if node IS included, answer if node is NOT included)`
- Compute children FIRST (post-order DFS), then combine at the parent
- Classic shape: House Robber III (can't rob a node + its direct child), max path sum in a binary tree
- Tree Diameter is also this pattern (see graphs/README.md - Tree-on-Graph Techniques - same DP idea, cross-listed there since it's tree-specific)
- KEYWORDS - "tree", "cannot pick a node and its parent/child together", "maximum path sum in a tree"

## Bitmask DP
- Used when N is SMALL (usually <= ~20) and you need to track a SUBSET of items as state
- State: `dp[mask]` where `mask` is an N-bit number, bit `i` = 1 means item i is already used/visited
- Transition: for each unset bit in mask, try setting it and recurse into `dp[mask | (1 << i)]`
- `2^N` total masks - that's why N must stay small (TC often `O(2^N * N)` or `O(2^N * N^2)`)
- Same idea as Hamiltonian Path/TSP bitmask DP in graphs/README.md - the state representation is identical, only the transition differs
- KEYWORDS - "n <= 20", "assign/partition items", "visit all", TSP-style problems

## Digit DP
- Used to count/sum numbers in a range `[0, N]` that satisfy a DIGIT-based property (digit sum, no repeated digits, etc.)
- Build the number DIGIT BY DIGIT (as a string), state: `dp[pos][tight][...extra state like running sum/count]`
- **`tight`** = are we still bound by N's digits so far, or free to place ANY digit 0-9 - this is the part people forget
  - If `tight = True` at position `pos`, you can only place digits up to N's digit at that position (else you'd exceed N)
  - The moment you place a digit SMALLER than N's digit, `tight` becomes `False` for all following positions (now free to place 0-9)
- Compute `f(N)` = count from 0 to N, then for a range `[L, R]` the answer = `f(R) - f(L-1)`
- KEYWORDS - "count numbers between L and R with property X", digit sum/digit constraint problems

## DP on Stocks (State Machine DP)
- State: `dp[day][transactions_left][holding_or_not]` - track the day, how many buy/sell transactions remain, and whether you currently hold a stock
- Each day - 2 choices: do nothing, OR act (buy if not holding / sell if holding)
- Variants differ only in which extra state dimension gets added: unlimited transactions (drop `transactions_left`), at most K transactions (add that dimension), cooldown after selling (add a cooldown flag), transaction fee (subtract fee on sell)
- KEYWORDS - "buy and sell stock", "at most K transactions", "cooldown", "transaction fee"

## String Matching DP (Wildcard / Regex)
- `dp[i][j]` = does `s[0:i]` match pattern `p[0:j]`
- Normal character match -> `dp[i][j] = dp[i-1][j-1]` if `s[i-1] == p[j-1]`
- `*` in WILDCARD matching (matches ANY sequence, including empty) -> `dp[i][j] = dp[i-1][j] OR dp[i][j-1]` (either `*` consumes 1 char of s, or `*` matches nothing)
- `*` in REGEX matching (means "zero or more of the PRECEDING character") -> different handling, look 1 pattern character back before deciding
- KEYWORDS - "wildcard matching", "regular expression matching", pattern with `*` / `?`

## Word Break
- `dp[i]` = can the string `s[0:i]` be fully segmented into dictionary words
- `dp[i] = True` if ANY `j < i` exists where `dp[j] = True` AND `s[j:i]` is in the dictionary
- Base case: `dp[0] = True` (empty prefix is trivially "segmented")
- KEYWORDS - "can string be segmented", "break into dictionary words"

## Search Space DP (Egg Drop style)
- State isn't "index in array" - it's a SEARCH PARAMETER, e.g. `dp[eggs][floors]` = minimum trials needed
- Transition tries every possible "test floor" `x` and takes the WORST case (egg breaks vs egg survives), then MINIMIZES over all choices of x
- `dp[eggs][floors] = min over x of (1 + max(dp[eggs-1][x-1], dp[eggs][floors-x]))` - egg breaks -> 1 fewer egg, search below x; egg survives -> same eggs, search above x
- KEYWORDS - "minimize worst case number of trials", egg drop, binary-search-flavored DP

------

## Code

### Concept
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | 0-1 KnapSack | - | [Link](https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/01_01_knapsack.py) |


### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Is Subset Sum | Amazon, Microsoft | [Link](https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/02_is_subset_sum.py) |
| 2 | Equal Sum Partition Problem | Amazon, Google | [Link](https://www.geeksforgeeks.org/problems/subset-sum-problem2014/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/03_equal_sum_partition_problem.py) |
| 3 | Perfect Sum Problem | Amazon, Microsoft, Tesco | [Link](https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/04_perfect_sum_problem.py) |
| 4 | Minimum Subset Sum Difference | Amazon, Samsung | [Link](https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/05_minimum_subset_sum_difference.py) |
| 5 | Count of Subsets with given Difference | NPCI | [Link](https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/06_count_of_subsets_with_given_diff.py) |
| 6 | Target Sum Problem | - | [Link](https://leetcode.com/problems/target-sum/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/07_target_sum.py) |

-------

### Concept
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Unbounded KnapSack | - | [Link](https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/08_unbounded_knapsack.py) |


### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Rod Cutting Problem | - | [Link](https://www.geeksforgeeks.org/problems/rod-cutting0840/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/09_rod_cutting_problem.py) |
| 2 | Coin Change - Number of Ways | - | [Link](https://leetcode.com/problems/coin-change-ii/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/10_coin_change_number_of_ways.py) |
| 3 | Coin Change - Using Minimum Number of Coins | - | [Link](https://leetcode.com/problems/coin-change/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/11_coin_change_minimum_number_of_coins.py) |
| 4 | Combination Sum | Generate All Combinations (Backtracking + Unbounded Choice) | [Link](https://leetcode.com/problems/combination-sum/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/12_combination_sum.py) |
| 5 | Combination Sum IV | Count Permutations (Order Matters) | [Link](https://leetcode.com/problems/combination-sum-iv/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/13_combination_sum_iv.py) |
| 6 | Form Largest Integer With Digits That Add up to Target | Lexicographical Optimization + Reconstruction | [Link](https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/14_form_largest_integer_with_digits_that_add_up_to_target.py) |


-------

### Concept
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Longest Common Subsequence | Amazon, Microsoft, Google | [GFG](https://www.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/15_longest_common_subsequence.py) |
| 2 | Longest Common Substring | Amazon, Microsoft | [GFG](https://www.geeksforgeeks.org/problems/longest-common-substring1452/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/16_longest_common_substring.py) |



### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|--------------|----------|
| 1 | Print Longest Common Subsequence | Amazon | [Naukri](https://www.naukri.com/code360/problems/print-longest-common-subsequence_8416383) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/17_print_longest_common_subsequence.py) |
| 2 | Shortest Common Supersequence | Amazon, Google | [LeetCode 1092](https://leetcode.com/problems/shortest-common-supersequence/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/18_shortest_common_supersequence.py) |
| 3 | Minimum Insertions & Deletions to Convert String A to B | Amazon | [GFG](https://www.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/19_min_insertions_deletions_to_convert_string.py) |
| 4 | Longest Repeating Subsequence | Microsoft | [GFG](https://www.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/20_longest_repeating_subsequence.py) |
| 5 | Sequence Pattern Matching | Amazon | [Leetcode](https://leetcode.com/problems/substring-matching-pattern/description/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/21_sequence_pattern_matching.py) |
| 6 | Distinct Subsequences | Google, Meta | [LeetCode 115](https://leetcode.com/problems/distinct-subsequences/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/22_distinct_subsequences.py) |
| 7 | Longest Palindromic Subsequence | Amazon, Microsoft | [LeetCode 516](https://leetcode.com/problems/longest-palindromic-subsequence/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/23_longest_palindromic_subsequence.py) |
| 8 | Longest Palindromic Substring | Amazon, Microsoft | [LeetCode 5](https://leetcode.com/problems/longest-palindromic-substring/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/24_longest_palindromic_substring.py) |
| 9 | Count Palindromic Substrings | Amazon | [LeetCode 647](https://leetcode.com/problems/palindromic-substrings/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/25_count_palindromic_substrings.py) |
| 10 | Minimum Deletions to Make a String Palindrome | Microsoft | [GFG](https://www.geeksforgeeks.org/problems/minimum-deletitions1648/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/26_min_deletions_to_make_palindrome.py) |
| 11 | Minimum Insertions to Make a String Palindrome | Google | [LeetCode 1312](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/27_min_insertions_to_make_palindrome.py) |

-------

### Concept (Linear DP / Fibonacci Pattern)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Climbing Stairs | Amazon, Adobe | [LeetCode 70](https://leetcode.com/problems/climbing-stairs/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/28_climbing_stairs.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | House Robber | Amazon, Google, Microsoft | [LeetCode 198](https://leetcode.com/problems/house-robber/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/29_house_robber.py) |
| 2 | House Robber II (Circular) | Amazon, Google | [LeetCode 213](https://leetcode.com/problems/house-robber-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/30_house_robber_ii_circular.py) |
| 3 | Decode Ways | Meta, Amazon | [LeetCode 91](https://leetcode.com/problems/decode-ways/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/31_decode_ways.py) |
| 4 | Min Cost Climbing Stairs | Amazon | [LeetCode 746](https://leetcode.com/problems/min-cost-climbing-stairs/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/32_min_cost_climbing_stairs.py) |

-------

### Concept (LIS)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Longest Increasing Subsequence (O(n^2) DP) | Amazon, Microsoft, Google | [LeetCode 300](https://leetcode.com/problems/longest-increasing-subsequence/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/33_longest_increasing_subsequence.py) |
| 2 | Longest Increasing Subsequence (O(n log n) Binary Search) | Amazon, Microsoft, Google | [LeetCode 300](https://leetcode.com/problems/longest-increasing-subsequence/) | 🔲 TODO - not built yet (34_longest_increasing_subsequence_binary_search.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Longest Bitonic Subsequence | Amazon, Microsoft | [GFG](https://www.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/35_longest_bitonic_subsequence.py) |
| 2 | Maximum Sum Increasing Subsequence | Amazon | [GFG](https://www.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/36_maximum_sum_increasing_subsequence.py) |
| 3 | Russian Doll Envelopes | Google, Amazon | [LeetCode 354](https://leetcode.com/problems/russian-doll-envelopes/) | 🔲 TODO - not built yet (37_russian_doll_envelopes.py) |

-------

### Concept (Kadane's Algorithm)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Maximum Subarray (Kadane's) | Amazon, Microsoft, Google, Meta | [LeetCode 53](https://leetcode.com/problems/maximum-subarray/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/38_kadanes_algorithm_max_subarray_sum.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Maximum Product Subarray | Amazon, Microsoft | [LeetCode 152](https://leetcode.com/problems/maximum-product-subarray/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/39_maximum_product_subarray.py) |
| 2 | Maximum Sum Circular Subarray | Google, Amazon | [LeetCode 918](https://leetcode.com/problems/maximum-sum-circular-subarray/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/40_maximum_sum_circular_subarray.py) |

-------

### Concept (Interval DP / Matrix Chain Multiplication / Partition DP)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Matrix Chain Multiplication | Amazon, Microsoft | [GFG](https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/41_matrix_chain_multiplication.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Palindrome Partitioning II (Min Cuts) | Amazon, Google | [LeetCode 132](https://leetcode.com/problems/palindrome-partitioning-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/42_palindrome_partitioning_ii_min_cuts.py) |
| 2 | Burst Balloons | Google, Amazon | [LeetCode 312](https://leetcode.com/problems/burst-balloons/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/43_burst_balloons.py) |
| 3 | Boolean Parenthesization | Amazon, Microsoft | [GFG](https://www.geeksforgeeks.org/problems/boolean-parenthesization5610/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/44_boolean_parenthesization.py) |

-------

### Concept (DP on Trees)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | House Robber III (Tree) | Amazon, Microsoft, Google | [LeetCode 337](https://leetcode.com/problems/house-robber-iii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/46_house_robber_iii_tree.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Binary Tree Maximum Path Sum | Amazon, Microsoft, Meta | [LeetCode 124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/47_binary_tree_maximum_path_sum.py) |

-------

### Concept (DP on Grid)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Unique Paths | Amazon, Microsoft, Google | [LeetCode 62](https://leetcode.com/problems/unique-paths/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/48_unique_path.py) |
| 2 | Minimum Path Sum | Amazon, Microsoft | [LeetCode 64](https://leetcode.com/problems/minimum-path-sum/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/49_min_path_sum.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Unique Paths II (With Obstacles) | Amazon, Microsoft | [LeetCode 63](https://leetcode.com/problems/unique-paths-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/50_unique_paths_ii_with_obstacles.py) |
| 2 | Triangle (Min Path Sum) | Amazon, Microsoft | [LeetCode 120](https://leetcode.com/problems/triangle/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/51_triangle_min_path_sum.py) |
| 3 | Cherry Pickup | Google | [LeetCode 741](https://leetcode.com/problems/cherry-pickup/) | 🔲 TODO - not built yet (52_cherry_pickup.py) |
| 4 | Dungeon Game | Microsoft, Amazon | [LeetCode 174](https://leetcode.com/problems/dungeon-game/) | 🔲 TODO - not built yet (53_dungeon_game.py) |

-------

### Concept (Bitmask DP)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Partition to K Equal Sum Subsets | Amazon, Google | [LeetCode 698](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | 🔲 TODO - not built yet (54_partition_to_k_equal_sum_subsets_bitmask.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Assignment Problem (Bitmask) | Amazon, Google | [GFG](https://www.geeksforgeeks.org/problems/assignment-problem5028/1) | 🔲 TODO - not built yet (55_assignment_problem_bitmask.py) |

-------

### Concept (Digit DP)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Count Numbers With Given Digit Sum (Digit DP) | Google, Amazon | [GFG](https://www.geeksforgeeks.org/dsa/digit-dp-introduction/) | 🔲 TODO - not built yet (56_count_numbers_with_digit_sum_digit_dp.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Numbers At Most N Given Digit Set | Google | [LeetCode 902](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) | 🔲 TODO - not built yet (57_numbers_at_most_n_given_digit_set.py) |

-------

### Concept (DP on Stocks - State Machine DP)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Best Time to Buy and Sell Stock I | Amazon, Microsoft, Meta | [LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/58_best_time_to_buy_sell_stock_i.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Best Time to Buy and Sell Stock II (Unlimited Transactions) | Amazon, Microsoft | [LeetCode 122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/59_best_time_to_buy_sell_stock_ii.py) |
| 2 | Best Time to Buy and Sell Stock III (At Most 2 Transactions) | Amazon, Google | [LeetCode 123](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/60_best_time_to_buy_sell_stock_iii.py) |
| 3 | Best Time to Buy and Sell Stock IV (At Most K Transactions) | Google, Amazon | [LeetCode 188](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/61_best_time_to_buy_sell_stock_iv.py) |
| 4 | Best Time to Buy and Sell Stock With Cooldown | Amazon, Google | [LeetCode 309](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/62_best_time_to_buy_sell_stock_with_cooldown.py) |
| 5 | Best Time to Buy and Sell Stock With Transaction Fee | Amazon, Microsoft | [LeetCode 714](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/63_best_time_to_buy_sell_stock_with_fee.py) |

-------

### Concept (String Matching DP)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Wildcard Matching | Amazon, Google, Microsoft | [LeetCode 44](https://leetcode.com/problems/wildcard-matching/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/64_wildcard_matching.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Regular Expression Matching | Amazon, Google, Microsoft | [LeetCode 10](https://leetcode.com/problems/regular-expression-matching/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/65_regular_expression_matching.py) |

-------

### Concept (Word Break)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Word Break | Amazon, Google, Meta | [LeetCode 139](https://leetcode.com/problems/word-break/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/66_word_break.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Word Break II | Amazon, Google | [LeetCode 140](https://leetcode.com/problems/word-break-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/dynamic-programming/67_word_break_ii.py) |

-------

### Concept (Search Space DP - Optional / Lower Priority)
- Lower interview frequency than everything above - only worth doing once the rest are solid
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Egg Dropping Puzzle | Amazon, Google | [GFG](https://www.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1) | 🔲 TODO - not built yet (68_egg_dropping_puzzle.py) |





