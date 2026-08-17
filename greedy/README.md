# Greedy Algorithms

- Make the LOCALLY optimal choice at each step, trusting it leads to the globally optimal solution - no backtracking, no reconsidering past choices
- The SDE3-level bar isn't applying a greedy rule - it's PROVING (at least informally, out loud) that the greedy choice is safe. Greedy algorithms are notoriously easy to get subtly wrong because a locally-obvious rule can fail on an edge case that only shows up with adversarial input - stating your justification is what shows you actually checked, not just pattern-matched

## How to Identify
- "Minimum number of ___" or "maximum number of ___" where a straightforward local rule (earliest deadline, smallest/largest first) seems to work
- Sorting the input FIRST makes the rest of the problem trivial or near-trivial
- Contrast with DP: if the "obviously correct" local choice can be proven WRONG by a counterexample, it's not actually greedy - it's DP (you need to consider multiple options and let the recurrence figure out which was best, since local optimality doesn't guarantee global optimality)

---------

## Keyword → Technique Cheat Sheet
| Keywords in Question | Technique |
|---|---|
| Merge overlapping intervals | Sort by start time, merge greedily left to right |
| Maximum number of non-overlapping intervals | Sort by END time, greedily pick the interval that finishes earliest |
| Minimum intervals to remove for no overlaps | Same as above - count what's LEFT OUT of the greedy max non-overlapping selection |
| Can you reach the end (array of max jump lengths) | Track the FARTHEST reachable index greedily as you scan left to right |
| Minimum jumps to reach the end | Greedy BFS-like "level" tracking (current window's farthest reach) |
| Circular route, enough fuel to complete a loop | Greedy - if total fuel >= total cost, a valid start always exists; track running tank to find it |
| Assign items to people to maximize/minimize satisfaction | Sort both sides, greedily match smallest-to-smallest or largest-to-largest |
| Partition/reorganize so no 2 adjacent are the same | Greedy + Heap (always place the most frequent remaining item) - see heaps/README.md - Task Scheduler |

---------

## Core Concepts

### What Makes a Greedy Solution Valid
- 2 properties must hold: **Greedy Choice Property** (a locally optimal choice is part of SOME globally optimal solution) and **Optimal Substructure** (the optimal solution to the whole problem contains optimal solutions to subproblems)
- The informal way to justify it in an interview: an EXCHANGE ARGUMENT - "suppose an optimal solution didn't make this greedy choice - show you can swap it in without making the solution worse, therefore the greedy choice is always at least as good"
- If you can construct a counterexample where the "obvious" local rule fails, it's not greedy - reach for DP instead (see dynamic-programming/README.md)
- KEYWORDS - this is reasoning to have ready, not a coding pattern - interviewers specifically probe "why does that work" on greedy solutions more than on any other category

### Interval Scheduling
- **Merge Intervals**: sort by START time, then scan left to right - merge the current interval into the last one in your result if they overlap, otherwise start a new entry
- **Maximum Non-Overlapping Intervals (Activity Selection)**: sort by END time (not start!) - greedily pick the interval that finishes EARLIEST among remaining options, since finishing early leaves the most room for future picks. This is the single most classic greedy proof (exchange argument: any optimal solution can be modified to include the earliest-finishing interval without losing optimality)
- **Minimum Removals to Eliminate Overlaps**: solve via the same earliest-end-time greedy selection - whatever ISN'T selected in the maximum non-overlapping set is what needs removing
- **Insert Interval**: since intervals are pre-sorted and non-overlapping, walk through - copy intervals ending before the new one starts, merge all overlapping intervals into the new one, then copy the rest
- KEYWORDS - "merge intervals", "maximum non-overlapping intervals", "minimum removals for no overlap", "insert an interval"

### Reachability & Jump Greedy
- **Jump Game (can you reach the end?)**: scan left to right, maintain `farthest_reachable` - if at any index `i`, `i > farthest_reachable`, you're stuck (return False). Otherwise keep updating `farthest_reachable = max(farthest_reachable, i + arr[i])`
- **Jump Game II (minimum jumps)**: treat it like a BFS by levels without an explicit queue - track the current jump's boundary and the farthest reachable within the NEXT jump; when you reach the current boundary, that's forced a new jump, and the boundary becomes whatever was the farthest reachable so far
- **Gas Station**: if `sum(gas) < sum(cost)`, no valid start exists at all. Otherwise, track a running tank total as you scan - whenever the tank goes negative, the current start point (and everything before it up to the last reset) can't work, so reset the candidate start to the NEXT index and the tank to 0. The final candidate start (after 1 full scan) is guaranteed valid given the total-sum check passed
- KEYWORDS - "can you reach the last index", "minimum jumps to reach the end", "circular gas station route"

### Sorting-Based Greedy
- **Assign Cookies**: sort both children's greed factors and cookie sizes, greedily match the smallest available cookie that satisfies the smallest unsatisfied child - a classic 2-pointer + greedy combo
- **Candy**: 2 passes - left-to-right ensuring each child with a higher rating than their LEFT neighbor gets more candy, then right-to-left doing the same check against the RIGHT neighbor (taking the max of both passes per child) - a single pass can't satisfy both neighbor constraints at once
- **Partition Labels**: for each character, precompute its LAST occurrence index. Scan left to right, extending the current partition's end to `max(current_end, last_occurrence[char])` - close the partition once you reach that end
- **Task Scheduler / Reorganize String**: these are greedy IN COMBINATION with a heap (always place the currently-most-frequent remaining item first) - see heaps/README.md for the full mechanic, listed here as a cross-reference since the core idea ("greedily use up the most constrained resource first") is a greedy principle even though the implementation needs a heap
- KEYWORDS - "assign/match to minimize/maximize satisfaction", "candy distribution by rating", "partition into as many parts as possible"

### Deadline Scheduling
- Different from Interval Scheduling above - here each job has a PROFIT and a DEADLINE (not a start/end time), and the goal is to pick the subset of jobs that maximizes total profit while respecting deadlines, at most 1 job per time slot
- **Job Sequencing**: sort jobs by profit DESCENDING (greedily prefer the most valuable jobs first), then for each job try to place it in the LATEST available free slot at or before its deadline (scanning from `deadline` down to 1) - placing late keeps earlier slots open for jobs with tighter deadlines. A DSU over slots (with path compression) speeds up "find latest free slot" to near O(1) instead of a linear scan
- KEYWORDS - "jobs with profit and deadline", "maximize profit, 1 job per time slot", "schedule to maximize total value"

---------

## Practice Questions

### Concept Set 1 (Do in order) - Interval Scheduling
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Merge Intervals | Amazon, Microsoft, Google, Meta | [LeetCode 56](https://leetcode.com/problems/merge-intervals/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/greedy/01_merge_intervals.py) |
| 2 | Non-overlapping Intervals | Amazon, Microsoft, Google | [LeetCode 435](https://leetcode.com/problems/non-overlapping-intervals/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/greedy/03_non_overlapping_intervals.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Insert Interval | Amazon, Microsoft, Google, Meta | [LeetCode 57](https://leetcode.com/problems/insert-interval/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/greedy/02_insert_interval.py) |
| 2 | Meeting Rooms (Can Attend All) | Amazon, Microsoft, Meta | [LeetCode 252](https://leetcode.com/problems/meeting-rooms/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/greedy/04_meeting_rooms.py) |
| 3 | Minimum Number of Platforms Required | Amazon, Microsoft, Ola | [GFG](https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/greedy/11_minimum_platforms.py) |

-------

### Concept Set 2 (Do in order) - Reachability & Jump Greedy
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Jump Game | Amazon, Microsoft, Google, Meta | [LeetCode 55](https://leetcode.com/problems/jump-game/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/greedy/05_jump_game.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Jump Game II | Amazon, Microsoft, Google, Meta | [LeetCode 45](https://leetcode.com/problems/jump-game-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/greedy/06_jump_game_ii.py) |
| 2 | Gas Station | Amazon, Microsoft, Google | [LeetCode 134](https://leetcode.com/problems/gas-station/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/greedy/07_gas_station.py) |

-------

### Concept Set 3 (Do in order) - Sorting-Based Greedy
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Assign Cookies | Amazon, Microsoft | [LeetCode 455](https://leetcode.com/problems/assign-cookies/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/greedy/08_assign_cookies.py) |
| 2 | Partition Labels | Amazon, Microsoft, Google | [LeetCode 763](https://leetcode.com/problems/partition-labels/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/greedy/10_partition_labels.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Candy | Amazon, Microsoft, Google | [LeetCode 135](https://leetcode.com/problems/candy/) | 🔲 TODO - not built yet (09_candy.py) |
| 2 | Task Scheduler (cross-ref: Greedy + Heap) | Amazon, Meta, Google | [LeetCode 621](https://leetcode.com/problems/task-scheduler/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/heaps/07_task_scheduler.py) |

-------

### Concept Set 4 (Do in order) - Deadline Scheduling
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Job Sequencing Problem | Amazon, Microsoft, Google | [GFG](https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1) | 🔲 TODO - not built yet (12_job_sequencing.py) |

---------

## Important Points
- Sort by the RIGHT key - interval problems sorting by start vs end time produce completely different (and often wrong) results depending on what the problem actually asks; get this decision right before writing any code
- If you can't articulate WHY the greedy choice is safe in 1-2 sentences, don't trust it yet - try to construct a counterexample first, and if you can't, that failed attempt IS your informal proof
- Greedy + Sorting is usually O(n log n) - if a "greedy-looking" problem seems to need O(n^2) or worse, you likely haven't found the right greedy rule yet, or the problem isn't actually greedy (check dynamic-programming/README.md)
