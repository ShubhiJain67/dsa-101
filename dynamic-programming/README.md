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

## Problem Patterns
1. 0-1 Knapscak
2. Unbounded Knapsack
3. Fibonacci
4. LCS
5. LIS
6. Kadane's Algorithm
7. Matrix Chain Multiplication
8. DP on Trees
9. DP on Grid
10. Others

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
An item cab be choosen multiple times 

### 0-1 KnapSack
- Item CANNOT be choosen fractionally, it is choosen or not
- 1 Item can be choosen at max 1 times
- Matrix usually becomes of n+1 * sum+1
- Type 
  - Subset Sum
  - Equal Sum Partition
  - Count of subset sum
  - Mnimum subset sum difference
  - Target Sum
  - Number of Subset sum with given difference


## Code

### Concept
| # | Problem | Companies | GFG/Leetcode | Solution |
|---|---------|-----------|-----|----------|
| 1 | 0-1 KnapSack | - | [Link](https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/dynamic-programming/01_01_knapsack.py) |


### Questions
| # | Problem | Companies | GFG/Leetcode | Solution |
|---|---------|-----------|-----|----------|
| 1 | Is Subset Sum | Amazon, Microsoft | [Link](https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/dynamic-programming/02_is_subset_sum.py) |
| 2 | Equal Sum Partition Problem | Amazon, Google | [Link](https://www.geeksforgeeks.org/problems/subset-sum-problem2014/1) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/dynamic-programming/03_equal_sum_partition_problem.py) |
| 3 | Perfect Sum Problem | Amazon, Microsoft, Tesco | [Link](https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/dynamic-programming/04_perfect_sum_problem.py) |
| 4 | Minimum Subset Sum Difference | Amazon, Samsung | [Link](https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/dynamic-programming/05_minimum_subset_sum_difference.py) |
| 5 | Count of Subsets with given Difference | NPCI | [Link](https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/dynamic-programming/06_count_of_subsets_with_given_diff.py) |
| 6 | Target Sum Problem | - | [Link](https://leetcode.com/problems/target-sum/description/) | [Python](https://github.com/ShubhiJain67/interview-prepration-101/blob/main/dynamic-programming/07_target_sum.py) |

