# Bit Manipulation

- Operating on the binary representation of numbers directly - AND, OR, XOR, NOT, and shifts - to solve problems in O(1) extra space that would otherwise need a HashSet or extra array
- At SDE3 level, this shows up less as "solve this bit puzzle" and more as an OPTIMIZATION layer inside a bigger problem (bitmask DP, representing a subset as an integer, deduplication without extra memory) - see dynamic-programming/README.md's Bitmask DP section for the biggest real-world application of this

## How to Identify
- "Without using extra space" on a problem that would normally need a HashSet
- "Every element appears twice/three times except one" (classic XOR/bit-counting territory)
- Anything about counting set bits, checking powers of 2, or toggling specific bits
- A "state" that's really just a small fixed set of binary flags -> represent it as an integer bitmask (see dynamic-programming/README.md - Bitmask DP for the full pattern)

---------

## Keyword → Technique Cheat Sheet
| Keywords in Question | Technique |
|---|---|
| Every element appears twice except one | XOR all elements (`a^a=0`, `a^0=a` - pairs cancel out) |
| Every element appears 3 times except one | Bit-counting per position (count set bits at each of the 32 positions, mod 3) |
| Exactly 2 elements appear once, rest appear twice | XOR everything, then use the lowest set bit of the result to split elements into 2 groups |
| Count the number of 1 bits (popcount) | Brian Kernighan's trick: `n & (n-1)` clears the lowest set bit, repeat and count |
| Check if a number is a power of 2 | `n > 0 and (n & (n-1)) == 0` (a power of 2 has exactly 1 set bit) |
| Add 2 numbers without `+`/`-` | Simulate a full adder: `XOR` = sum without carry, `AND` shifted left 1 = the carry, repeat until no carry remains |
| Represent a subset of items as a single number | Bitmasking (see dynamic-programming/README.md - Bitmask DP) |
| Missing number in a range | XOR trick (XOR all indices AND all values, duplicates cancel, only the missing one survives) - alternative to Cyclic Sort in arrays-two-pointers/README.md |

---------

## Core Concepts

### XOR Fundamentals
- **Properties**: `a ^ a = 0`, `a ^ 0 = a`, commutative and associative (order doesn't matter) - these 3 facts alone solve a surprising number of problems
- **Single Number (every element appears twice except one)**: XOR every element together - all the pairs cancel out to 0, leaving only the unpaired number
- **Missing Number**: XOR all array values together AND all indices `0..n` together in the same pass - every value that exists cancels with its matching index, leaving only the missing number
- **2 unique numbers (everything else appears twice)**: XOR everything first - the result is `unique1 ^ unique2` (nonzero, since they differ). Find any SET BIT in that result (a position where the 2 unique numbers differ) - use it to split ALL numbers into 2 groups (bit set / bit not set), then XOR within each group separately to isolate each unique number
- KEYWORDS - "appears twice except one", "missing number", "exactly 2 numbers appear once"

### Bit Counting & Checks
- **Brian Kernighan's Algorithm (count set bits)**: `n & (n - 1)` clears the LOWEST set bit of `n` (subtracting 1 flips all trailing zeros to 1s and the lowest set bit to 0, and ANDing with the original clears exactly that bit) - repeat until `n` becomes 0, counting iterations
  ```
  def count_set_bits(n):
      count = 0
      while n:
          n &= (n - 1)   # clears the lowest set bit
          count += 1
      return count
  ```
- **Power of Two check**: a power of 2 has EXACTLY 1 set bit, so `n & (n-1) == 0` (clearing its only set bit gives 0) - combined with `n > 0` to exclude 0 itself
- **Counting Bits for every number 0..n (DP + bit trick combo)**: `dp[i] = dp[i >> 1] + (i & 1)` - the count of set bits in `i` equals the count in `i` with the last bit removed, plus whether that last bit was itself set. This turns an O(n log n) "count bits for each number independently" into O(n) by reusing previous results
- **Every element appears 3 times except one**: for each of the 32 bit positions, sum up how many numbers have that bit set - if the total isn't divisible by 3, the unique number has that bit set. Reconstruct the answer bit by bit
- KEYWORDS - "count set bits", "power of two/four", "counting bits for every number up to n", "every element appears 3 times except one"

### Advanced Bit Tricks
- **Sum of Two Integers without `+`/`-`**: simulate binary addition manually - `XOR` gives the sum ignoring carries, `AND` (then shifted left by 1) gives where a carry would be generated. Repeat: `a, b = a^b, (a&b)<<1` until `b` (the carry) becomes 0 - at that point `a` holds the final sum
- **Reverse Bits**: build the result bit by bit - shift the result left, OR in the lowest bit of the input, shift the input right - repeat 32 times
- **Bitwise AND of Numbers Range [m, n]**: the answer is the common PREFIX of `m` and `n`'s binary representations (any bit that differs between them will be 0 in at least one number somewhere in the range, so it gets zeroed out) - repeatedly right-shift both `m` and `n` until they're equal, then shift the common value back left by the same amount
- **Subsets via Bitmask**: represent a subset of `n` items as an `n`-bit integer, iterate `mask` from `0` to `2^n - 1`, and check `mask & (1 << i)` to see if item `i` is included - this is the SAME representation used in Bitmask DP (dynamic-programming/README.md) and the bitmask-based Hamiltonian/TSP approach (graphs/README.md), just without the DP layer on top
- KEYWORDS - "add without +/-", "reverse bits", "bitwise AND of a range", "generate all subsets using bits"
- To get the right most bit from "num" -> `num & -num`

---------

## Practice Questions

### Concept Set 1 (Do in order) - XOR Fundamentals
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Single Number | Amazon, Microsoft, Google, Meta | [LeetCode 136](https://leetcode.com/problems/single-number/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/bit-manipulation/01_single_number.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Single Number II | Amazon, Microsoft | [LeetCode 137](https://leetcode.com/problems/single-number-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/bit-manipulation/02_single_number_ii.py) |
| 2 | Single Number III | Amazon, Microsoft, Google | [LeetCode 260](https://leetcode.com/problems/single-number-iii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/bit-manipulation/03_single_number_iii.py) |
| 3 | Missing Number (XOR Approach) | Amazon, Microsoft | [LeetCode 268](https://leetcode.com/problems/missing-number/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/bit-manipulation/04_missing_number_xor.py) |

-------

### Concept Set 2 (Do in order) - Bit Counting & Checks
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Number of 1 Bits | Amazon, Microsoft, Google | [LeetCode 191](https://leetcode.com/problems/number-of-1-bits/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/bit-manipulation/05_number_of_1_bits.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Counting Bits | Amazon, Microsoft, Google | [LeetCode 338](https://leetcode.com/problems/counting-bits/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/bit-manipulation/06_counting_bits.py) |
| 2 | Power of Two | Amazon, Microsoft | [LeetCode 231](https://leetcode.com/problems/power-of-two/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/bit-manipulation/07_power_of_two.py) |
| 3 | Power of Four | Amazon, Microsoft | [LeetCode 342](https://leetcode.com/problems/power-of-four/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/bit-manipulation/08_power_of_four.py) |

-------

### Concept Set 3 (Do in order) - Advanced Bit Tricks
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Sum of Two Integers (Without +/-) | Amazon, Microsoft, Google | [LeetCode 371](https://leetcode.com/problems/sum-of-two-integers/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/bit-manipulation/09_sum_of_two_integers.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Reverse Bits | Amazon, Microsoft | [LeetCode 190](https://leetcode.com/problems/reverse-bits/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/bit-manipulation/10_reverse_bits.py) |
| 2 | Bitwise AND of Numbers Range | Amazon, Microsoft | [LeetCode 201](https://leetcode.com/problems/bitwise-and-of-numbers-range/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/bit-manipulation/11_bitwise_and_of_numbers_range.py) |

-------

### Concept Set 4 (Do in order) - Trie-Based Bit Tricks
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Maximum XOR of Two Numbers in an Array | Amazon, Google, Microsoft | [LeetCode 421](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | 🔲 TODO - not built yet (12_maximum_xor_of_two_numbers.py) |

---------

## Important Points
- Python integers don't have a fixed bit-width like other languages - watch out for negative numbers and left/right shifts behaving differently than in Java/C++ if you ever translate a bit-manipulation solution between languages
- Bit tricks are rarely the WHOLE solution at SDE3 level - they're more often a space/time optimization layered onto a bigger problem (bitmask DP, subset representation, deduplication) - know them well enough to reach for them as a tool, not just as standalone puzzles
- If you're about to write a HashSet purely to check "have I seen this before" and the values are small/bounded, ask whether a bitmask could replace it entirely in O(1) space
