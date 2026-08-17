# Sliding Window

- A specialized two-pointer technique for CONTIGUOUS subarray/substring problems - instead of recomputing from scratch for every window position, you INCREMENTALLY update as the window slides, turning an O(n^2) or O(n^3) brute force into O(n)
- At SDE3 level, the bar is recognizing when a problem is a sliding window in disguise (it often won't say "window" or "substring" directly) and handling the shrink condition correctly on the first attempt

## How to Identify
- "Longest/shortest/max/min ... SUBSTRING or SUBARRAY ..." (contiguous - if it's a subsequence instead, that's DP or two-pointer on a different axis, not sliding window)
- A CONDITION on the window contents (at most K distinct characters, sum <= target, contains all characters of another string)
- Brute force would be "try every substring/subarray" (O(n^2)) - sliding window gets it to O(n) because the window only ever expands or shrinks, never restarts

---------

## Keyword → Technique Cheat Sheet
| Keywords in Question | Technique |
|---|---|
| Fixed window size K, max/min/average of each window | Fixed-Size Sliding Window |
| Longest substring/subarray satisfying a condition | Variable-Size Window (expand right, shrink left when condition breaks) |
| Shortest substring/subarray satisfying a condition | Variable-Size Window (expand right until valid, then shrink left as much as possible) |
| At most/exactly K distinct characters | Variable window + frequency HashMap |
| Contains all characters of another string (anagram/permutation check) | Variable window + frequency HashMap match-count |
| Maximum/minimum value in every window of size K | see heaps/README.md and stacks/README.md - Monotonic Deque (NOT plain sliding window, needs a deque) |
| Median in every window of size K | see heaps/README.md - Two Heaps with lazy deletion |

---------

## Core Concepts

### Fixed-Size Window
- Compute the result for the FIRST window directly, then slide by 1: subtract the element leaving the window, add the element entering it - O(1) update per step instead of O(K) recomputation
- **Maximum Sum Subarray of Size K**: classic - `window_sum += arr[right] - arr[left]` as the window slides
- **Permutation in String / Anagram check with fixed window**: maintain a frequency count of the window, compare against the target's frequency count (or track a "matches" counter to avoid comparing the whole frequency map every step)
- KEYWORDS - "subarray of exactly size K", "every window of size K"

### Variable-Size Window (the more common interview pattern)
- 2 pointers, `left` and `right`, both starting at 0
- Expand `right` to grow the window. When the window VIOLATES the condition (or, for "shortest" problems, as soon as it SATISFIES the condition), shrink from `left` until it's valid again
- **Longest Substring Without Repeating Characters**: expand right, if the new character is already in the window, shrink left past its previous occurrence
  ```
  def longest_unique_substring(s):
      seen = {}   # char -> last index seen
      left = 0
      best = 0
      for right, ch in enumerate(s):
          if ch in seen and seen[ch] >= left:
              left = seen[ch] + 1   # jump left PAST the duplicate, don't just increment
          seen[ch] = right
          best = max(best, right - left + 1)
      return best
  ```
- **Longest Repeating Character Replacement**: window is valid as long as `(window_length - count_of_most_frequent_char_in_window) <= K` (i.e. you can afford to replace the "wrong" characters within your budget K) - shrink left when this breaks
- **Minimum Size Subarray Sum**: this is a "shortest" variant - expand right until the sum meets the target, then GREEDILY shrink left as far as possible while still valid, recording the minimum length along the way
- KEYWORDS - "longest substring/subarray with condition X", "at most/exactly K distinct", "minimum window/subarray meeting condition"

### Hard Variable Window (SDE3-Level Variants)
- **Minimum Window Substring**: the window must contain ALL characters of a target string (with correct multiplicities) - maintain a frequency map of what's still NEEDED, and a `matched` counter tracking how many distinct required characters are currently fully satisfied in the window. Expand right until `matched == required`, then shrink left greedily while still valid, tracking the minimum window seen
- **Substring with Concatenation of All Words**: window size is FIXED at `(number of words * word length)`, but instead of character-by-character sliding, you slide WORD-by-word and match a frequency map of words instead of characters - the "fixed window" idea generalizes beyond single characters
- Both of these combine sliding window with a HashMap-based frequency/count-matching mechanism - that combination (not window mechanics alone) is what makes them hard
- KEYWORDS - "minimum window containing all characters/words of another string", "concatenation of all words"

---------

## Practice Questions

### Concept Set 1 (Do in order) - Fixed-Size Window
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Maximum Average Subarray I | Amazon, Microsoft | [LeetCode 643](https://leetcode.com/problems/maximum-average-subarray-i/) | [Python](https://github.com/ShubhiJain67/dsa-101/tree/main/sliding-window) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Permutation in String | Amazon, Microsoft, Google | [LeetCode 567](https://leetcode.com/problems/permutation-in-string/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/sliding-window/02_permutation_in_string.py) |
| 2 | Find All Anagrams in a String | Amazon, Microsoft, Google, Meta | [LeetCode 438](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/sliding-window/03_find_all_anagrams_in_a_string.py) |

-------

### Concept Set 2 (Do in order) - Variable-Size Window
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Longest Substring Without Repeating Characters | Amazon, Microsoft, Google, Meta | [LeetCode 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/sliding-window/04_longest_substring_without_repeating_characters.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Longest Repeating Character Replacement | Amazon, Microsoft, Google | [LeetCode 424](https://leetcode.com/problems/longest-repeating-character-replacement/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/sliding-window/05_longest_repeating_character_replacement.py) |
| 2 | Fruit Into Baskets | Amazon, Google | [LeetCode 904](https://leetcode.com/problems/fruit-into-baskets/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/sliding-window/06_fruit_into_baskets.py) |
| 3 | Longest Substring with At Most K Distinct Characters | Amazon, Google, Meta | [LeetCode 340](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/sliding-window/07_longest_substring_at_most_k_distinct.py) |
| 4 | Minimum Size Subarray Sum | Amazon, Microsoft, Google | [LeetCode 209](https://leetcode.com/problems/minimum-size-subarray-sum/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/sliding-window/08_minimum_size_subarray_sum.py) |

-------

### Concept Set 3 (Do in order) - Hard Variants (SDE3-Level)
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Minimum Window Substring | Amazon, Microsoft, Google, Meta | [LeetCode 76](https://leetcode.com/problems/minimum-window-substring/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/sliding-window/09_minimum_window_substring.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Substring with Concatenation of All Words | Amazon, Microsoft, Google | [LeetCode 30](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/sliding-window/10_substring_concatenation_of_all_words.py) |
| 2 | Sliding Window Maximum (cross-ref: Monotonic Deque, not pure window) | Amazon, Google, Meta | [LeetCode 239](https://leetcode.com/problems/sliding-window-maximum/) | see heaps/README.md and stacks/README.md |
| 3 | Sliding Window Median (cross-ref: Two Heaps) | Google, Amazon | [LeetCode 480](https://leetcode.com/problems/sliding-window-median/) | see heaps/README.md |

---------

## Important Points
- The single most common bug: shrinking the window with `left += 1` but forgetting to UNDO that element's contribution to your running state (frequency count, sum, matched-counter) - the shrink step needs to mirror the expand step exactly, just in reverse
- "Longest" problems usually shrink only when the condition is VIOLATED; "shortest/minimum" problems usually shrink greedily as soon as the condition is SATISFIED - mixing these up is the second most common bug
- If the window needs the MAX or MIN of its contents (not just a sum/count/frequency), plain sliding window isn't enough - that's what pushes you to a monotonic deque (see stacks/README.md) or a heap (see heaps/README.md) instead
