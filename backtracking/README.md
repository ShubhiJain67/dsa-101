# Backtracking

- Systematic brute force - try a choice, recurse, UNDO the choice ("backtrack") if it doesn't lead anywhere, try the next choice
- At SDE3 level, the correctness of the template is the easy part - the actual bar is PRUNING: cutting off invalid branches as early as possible so it doesn't time out on the given constraints. Anyone can write a working-but-slow backtracking solution; the signal is whether you add pruning unprompted

## How to Identify
- "Generate all possible ___" (subsets, permutations, combinations, arrangements)
- "Find all valid ways to place/arrange ___ satisfying constraints" (N-Queens, Sudoku)
- Constraints that only matter INCREMENTALLY as you build a partial solution (you can tell a placement is invalid before the whole solution is built - that's what makes pruning possible)
- Contrast with DP: if the problem asks for a COUNT or an OPTIMAL VALUE only (not the actual arrangements), it might be solvable with DP instead, often faster - see dynamic-programming/README.md. If it explicitly wants ALL solutions or ANY ONE valid solution enumerated, that's backtracking

---------

## Keyword → Technique Cheat Sheet
| Keywords in Question | Technique |
|---|---|
| Generate all subsets/power set | Backtracking (include/exclude each element) |
| Generate all permutations/arrangements | Backtracking (swap-based or visited-array based) |
| Generate all combinations of size K | Backtracking (choose with an increasing start index, no reuse) |
| Combination Sum (reuse elements allowed) | Backtracking (don't advance the start index when reusing) - contrast with the DP COUNTING version in dynamic-programming/README.md |
| N-Queens / Sudoku / constraint grids | Backtracking + constraint checking before each placement |
| Word Search on a grid | Backtracking (DFS in 4 directions + mark visited + unmark on backtrack) |
| Word Search II (multiple target words) | see trees/README.md - Trie + Backtracking (prune using the Trie structure itself) |
| Generate all valid parenthesis combinations | Backtracking (track open/close count, prune invalid partial strings early) |
| Partition a string into all valid substrings | Backtracking (try every prefix, recurse on the rest) - contrast with the DP MIN-CUT version in dynamic-programming/README.md |

---------

## Core Concepts

### The Core Template
- Every backtracking problem follows the same shape: CHOOSE an option, EXPLORE (recurse) with that choice made, UN-CHOOSE (undo it) before trying the next option
  ```
  def backtrack(path, choices):
      if is_complete(path):
          results.append(path.copy())   # copy! path is mutated in place
          return
      for choice in choices:
          if not is_valid(choice, path):
              continue   # PRUNE - skip invalid choices before recursing at all
          path.append(choice)
          backtrack(path, remaining_choices(choices, choice))
          path.pop()   # undo - this IS the "backtrack" step
  ```
- The `path.pop()` after the recursive call is the entire mechanic - forgetting it means every branch shares corrupted state with every other branch
- **Pruning** (the SDE3-level differentiator): check `is_valid` BEFORE recursing, not after - the earlier you can rule out an invalid branch, the more of the search tree you skip entirely. Sorting the input first often unlocks pruning (lets you `break` out of a loop early once remaining choices can't possibly work, instead of just `continue`-ing past each one)
- KEYWORDS - the template applies to virtually every problem below, the differences are all in what counts as "valid" and what the "choices" are at each step

### Subsets, Permutations, Combinations
- **Subsets (Power Set)**: at each element, branch into 2 choices - include it, or don't. `2^n` total subsets, matches the recursion tree exactly
- **Permutations**: at each position, try every UNUSED element (track via a `visited` set or by swapping used elements to the front and recursing on the rest)
- **Combinations of size K**: like subsets, but track a START INDEX so you never reconsider earlier elements (this is what prevents `[1,2]` and `[2,1]` from both appearing as separate combinations)
- **With duplicates in the input (Subsets II / Permutations II)**: sort first, then skip a candidate if it equals the previous candidate AND the previous one hasn't been used at this same recursion depth - this is the standard dedup pattern, worth memorizing exactly since it's easy to get subtly wrong
- **Combination Sum (elements reusable)**: same as combinations, but when you choose an element, recurse WITHOUT advancing the start index (since it can be reused) - contrast with plain Combination Sum where each element is used once (advance the start index)
- KEYWORDS - "all subsets", "all permutations", "all combinations", "combination sum"

### Constraint Satisfaction (N-Queens, Sudoku)
- The "choices" at each step are constrained by BOARD STATE, not just "used vs unused" - need a fast `is_valid` check (e.g. for N-Queens: no other queen shares this row, column, or either diagonal)
- **N-Queens**: place 1 queen per row, try each column in that row, check column/diagonal conflicts against ALREADY PLACED queens before recursing to the next row - track used columns/diagonals in sets for O(1) validity checks instead of re-scanning the board
- **Sudoku Solver**: for each empty cell, try digits 1-9, check row/column/3x3-box validity before placing, backtrack if no digit works and the cell can't be filled
- The performance difference between a naive and a well-pruned constraint-satisfaction backtracking solution can be orders of magnitude - this is where "does it just work" vs "does it work well" is most visible to an interviewer
- KEYWORDS - "N-Queens", "Sudoku", any grid with row/column/region constraints

### Grid & String Backtracking
- **Word Search**: DFS from every starting cell, at each step check the next character matches, mark the current cell VISITED before recursing, UNMARK it after (so other paths can reuse the cell) - this mark/unmark is the backtracking step applied to a grid instead of a list
- **Palindrome Partitioning (enumerate ALL valid partitions)**: try every possible "first piece" (as a prefix), check if it's a palindrome, if so recurse on the remainder - contrast with the DP version (Palindrome Partitioning II in dynamic-programming/README.md) which only wants the MINIMUM number of cuts, not every partition
- **Generate Parentheses**: track counts of open and close brackets used so far, only add a `(` if you haven't used all `n`, only add a `)` if it wouldn't exceed the number of `(` used - this constraint IS the pruning, an unconstrained approach would generate and then filter invalid strings, which is much slower
- **Restore IP Addresses**: try every valid-length segment (1-3 digits, no leading zero unless the segment is exactly "0", value <= 255) at each step, recurse on the remainder, backtrack when a segment can't be valid
- KEYWORDS - "word search on a grid", "all palindrome partitions", "generate valid parentheses", "restore IP addresses"

---------

## Practice Questions

### Concept Set 1 (Do in order) - Subsets, Permutations, Combinations
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Subsets | Amazon, Microsoft, Google, Meta | [LeetCode 78](https://leetcode.com/problems/subsets/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/backtracking/01_subsets.py) |
| 2 | Permutations | Amazon, Microsoft, Google, Meta | [LeetCode 46](https://leetcode.com/problems/permutations/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/backtracking/03_permutations.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Subsets II (With Duplicates) | Amazon, Microsoft | [LeetCode 90](https://leetcode.com/problems/subsets-ii/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/backtracking/02_subsets_ii_with_duplicates.py) |
| 2 | Permutations II (With Duplicates) | Amazon, Microsoft | [LeetCode 47](https://leetcode.com/problems/permutations-ii/) | 🔲 TODO - not built yet (04_permutations_ii_with_duplicates.py) |
| 3 | Combinations | Amazon, Microsoft | [LeetCode 77](https://leetcode.com/problems/combinations/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/backtracking/05_combinations.py) |
| 4 | Combination Sum | Amazon, Microsoft, Google, Meta | [LeetCode 39](https://leetcode.com/problems/combination-sum/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/backtracking/06_combination_sum.py) |

-------

### Concept Set 2 (Do in order) - Constraint Satisfaction
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | N-Queens | Amazon, Microsoft, Google, Meta | [LeetCode 51](https://leetcode.com/problems/n-queens/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/backtracking/07_n_queens.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | N-Queens II (Count Only) | Amazon, Microsoft | [LeetCode 52](https://leetcode.com/problems/n-queens-ii/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/backtracking/08_n_queens_ii_count.py) |
| 2 | Sudoku Solver | Amazon, Microsoft, Google | [LeetCode 37](https://leetcode.com/problems/sudoku-solver/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/backtracking/09_sudoku_solver.py) |

-------

### Concept Set 3 (Do in order) - Grid & String Backtracking
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Word Search | Amazon, Microsoft, Google, Meta | [LeetCode 79](https://leetcode.com/problems/word-search/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/backtracking/10_word_search.py) |
| 2 | Generate Parentheses | Amazon, Microsoft, Google, Meta | [LeetCode 22](https://leetcode.com/problems/generate-parentheses/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/backtracking/12_generate_parentheses.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Palindrome Partitioning | Amazon, Microsoft, Google, Meta | [LeetCode 131](https://leetcode.com/problems/palindrome-partitioning/) | [Python]((https://github.com/ShubhiJain67/dsa-101/blob/main/backtracking/11_palindrome_partitioning.py)) |
| 2 | Restore IP Addresses | Amazon, Microsoft | [LeetCode 93](https://leetcode.com/problems/restore-ip-addresses/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/backtracking/13_restore_ip_addresses.py) |

---------

## Important Points
- Always ask yourself "does this need EVERY solution, or just a count/optimum" - if it's the latter, check dynamic-programming/README.md first, since a DP solution is usually faster than enumerating everything with backtracking
- Copy the path (`path.copy()` / `path[:]` / `list(path)`) when appending to results - appending the mutable list reference itself is the single most common backtracking bug, and it fails silently (wrong output, no error)
- State your pruning strategy OUT LOUD before coding in an interview - "I'll sort first so I can break early once remaining candidates are too large" is exactly the signal that separates a working solution from a strong one
