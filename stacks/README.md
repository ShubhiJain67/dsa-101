# Stacks

- LIFO (Last In, First Out) - the last element pushed is the first one popped
- Recursion itself uses an implicit call stack - anywhere you'd reach for recursion, you can also simulate it with an explicit stack (useful when recursion would blow the call stack on deep input)

## How to Identify a Stack Question
- "Matching pairs" (parentheses, brackets, tags)
- "Next greater/smaller element", "previous greater/smaller"
- "Undo" behavior, or needing to know what came "just before" in a nested structure
- Expression evaluation (calculators, nested encoded strings)
- Anything phrased as "process left to right, but the answer for element i depends on some earlier unresolved element"

---------

## Keyword → Technique Cheat Sheet
| Keywords in Question | Technique |
|---|---|
| Valid/balanced parentheses or brackets | Stack matching (push opening, pop-and-check on closing) |
| Next greater/smaller element (to the right) | Monotonic Stack |
| Previous greater/smaller element (to the left) | Monotonic Stack (same idea, scan direction flips) |
| Largest rectangle in histogram | Monotonic Stack (index-based, track bar heights) |
| Trapping rain water | Monotonic Stack (alternative to two-pointer approach) |
| Get min/max from a stack in O(1) | Auxiliary min/max stack alongside the main stack |
| Evaluate an expression / calculator | Stack for operands + operators (or a stack of signs for nested parens) |
| Nested encoded string (e.g. `3[a2[c]]`) | Stack of (count, partial-string) pairs |
| Simplify a Unix-style file path | Stack of path tokens (push folder names, pop on `..`) |
| Undo/redo, browser back button | Stack (or 2 stacks for undo + redo) |
| Implement a queue using only stacks | 2-stack technique (1 for enqueue, 1 for dequeue) |

---------

## Core Concepts

### Stack Matching (Valid Parentheses)
- Push every OPENING bracket. On a CLOSING bracket, pop and check it matches the corresponding opening type - mismatch or empty-stack-on-pop means invalid
- String is valid overall only if the stack is EMPTY at the end (no unclosed opens remain)
- KEYWORDS - "valid parentheses", "balanced brackets", matching tag problems (like valid HTML)

### Monotonic Stack (the core stack pattern for interviews)
- A stack that's kept either strictly INCREASING or strictly DECREASING from bottom to top - maintained by popping elements that violate the order BEFORE pushing the new one
- **Next Greater Element (to the right)**: use a DECREASING stack. For each new number, pop everything smaller than it (those popped elements just found their "next greater" - the current number), then push the current number
  ```
  def next_greater_elements(arr):
      n = len(arr)
      result = [-1] * n
      stack = []   # stores INDICES, kept decreasing by value
      for i in range(n):
          while stack and arr[stack[-1]] < arr[i]:
              j = stack.pop()
              result[j] = arr[i]   # arr[i] is the next greater element for index j
          stack.append(i)
      return result
  ```
- **Next Smaller** -> flip the comparison (increasing stack instead)
- **Previous Greater/Smaller** -> scan right-to-left instead of left-to-right (or keep the stack of "not yet resolved" indices and read the answer as you go left-to-right, using the stack top as the nearest unresolved candidate)
- **Largest Rectangle in Histogram**: for each bar, you need the nearest smaller bar to the left AND right (those bound how wide a rectangle CAN be at that height) - a single monotonic-increasing stack pass gets both, popping a bar means you've just found its right boundary, and whatever's left on the stack below it is the left boundary
- **Daily Temperatures / Stock Span**: literally "next greater element," just phrased as "how many days until" instead of "what is"
- KEYWORDS - "next/previous greater or smaller element", "largest rectangle", "daily temperatures", "stock span"

### Min Stack (O(1) Min/Max Retrieval)
- A normal stack can't tell you the min in O(1) without scanning - fix: maintain a SECOND stack that tracks the min-so-far at each level
- On push: push the value to the main stack, and push `min(value, current_min_stack_top)` to the min-stack
- On pop: pop from BOTH stacks together (keeps them in sync)
- `get_min()` = just peek the min-stack's top - always O(1)
- Alternative (saves space): only push to the min-stack when a NEW minimum is found, and only pop from it when the popped main-stack value equals the current min
- KEYWORDS - "design a stack with O(1) getMin/getMax"

### Expression Evaluation
- **Basic Calculator (with `+`, `-`, parentheses)**: maintain a running `result`, a running `sign`, and a STACK OF SIGNS to handle nested parentheses - when you hit `(`, push the current sign context; when you hit `)`, pop it back
- **Basic Calculator II (with `+`, `-`, `*`, `/`, no parens)**: push numbers onto a stack, but for `*`/`/` immediately combine with the PREVIOUS stack value instead of pushing (since multiplication/division bind tighter than addition) - at the end, sum everything left on the stack
- **Infix to Postfix / Postfix Evaluation**: operator stack tracks precedence, operand stack (or the same stack) evaluates as you go
- KEYWORDS - "calculator", "evaluate expression", "reverse polish notation"

### Nested Encoded Strings (Decode String)
- Pattern like `3[a2[c]]` -> `"accaccacc"` - use a stack to remember "what was I building before I went 1 level deeper," push `(current_string, current_count)` when you hit `[`, pop and combine when you hit `]`
- KEYWORDS - "decode a nested/encoded string"

### Path Simplification
- Split a Unix-style path on `/`, push real folder names onto a stack, pop on `..` (go up a directory), ignore `.` (current directory) and empty segments
- Final path = join whatever remains on the stack with `/`
- KEYWORDS - "simplify a file path"

### Queue Using Stacks (and vice versa)
- **Queue from 2 stacks**: an "in" stack for enqueue, an "out" stack for dequeue - when the "out" stack is empty, dump the ENTIRE "in" stack into it (reverses the order back to FIFO), then pop from "out". Each element moves between stacks at most once, so it's still amortized O(1) per operation
- **Stack from queues**: mirror idea, but generally needs re-rotating the queue on every push to keep the newest element at the front
- KEYWORDS - "implement a queue using stacks", "implement a stack using queues"

---------

## Practice Questions

### Concept Set 1 (Do in order) - Stack Matching & Min Stack
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Valid Parentheses | Amazon, Microsoft, Google, Meta | [LeetCode 20](https://leetcode.com/problems/valid-parentheses/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/01_valid_parentheses.py) |
| 2 | Min Stack | Amazon, Microsoft, Google, Meta | [LeetCode 155](https://leetcode.com/problems/min-stack/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/02_min_stack.py) |

-------

### Concept Set 2 (Do in order) - Monotonic Stack
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Next Greater Element I | Amazon, Microsoft, Google | [LeetCode 496](https://leetcode.com/problems/next-greater-element-i/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/03_next_greater_element_i.py) |
| 2 | Next Greater Element II (Circular) | Amazon, Microsoft | [LeetCode 503](https://leetcode.com/problems/next-greater-element-ii/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/04_next_greater_element_ii_circular.py) |
| 3 | Largest Rectangle in Histogram | Amazon, Microsoft, Google, Meta | [LeetCode 84](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/06_largest_rectangle_in_histogram.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Daily Temperatures | Amazon, Microsoft, Google, Meta | [LeetCode 739](https://leetcode.com/problems/daily-temperatures/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/05_daily_temperatures.py) |
| 2 | Trapping Rain Water (Stack Approach) | Amazon, Microsoft, Google, Meta | [LeetCode 42](https://leetcode.com/problems/trapping-rain-water/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/07_trapping_rain_water_stack.py) |
| 3 | Stock Span Problem | Amazon, Microsoft | [GFG](https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/08_stock_span_problem.py) |
| 4 | Remove K Digits | Amazon, Google | [LeetCode 402](https://leetcode.com/problems/remove-k-digits/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/14_remove_k_digits.py) |
| 5 | Remove Duplicate Letters | Amazon, Google, Microsoft | [LeetCode 316](https://leetcode.com/problems/remove-duplicate-letters/) | 🔲 TODO - not built yet (15_remove_duplicate_letters.py) |
| 6 | Asteroid Collision | Amazon, Google | [LeetCode 735](https://leetcode.com/problems/asteroid-collision/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/13_asteroid_collision.py) |

-------

### Concept Set 3 (Do in order) - Expression Evaluation
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Basic Calculator | Amazon, Microsoft, Google | [LeetCode 224](https://leetcode.com/problems/basic-calculator/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/09_basic_calculator_i.py) |
| 2 | Basic Calculator II | Amazon, Microsoft, Google | [LeetCode 227](https://leetcode.com/problems/basic-calculator-ii/) | 🔲 TODO - not built yet (10_basic_calculator_ii.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Evaluate Reverse Polish Notation | Amazon, Microsoft, Google | [LeetCode 150](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/18_evaluate_reverse_polish_notation.py) |
| 2 | Decode String | Amazon, Microsoft, Google, Meta | [LeetCode 394](https://leetcode.com/problems/decode-string/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/11_decode_string.py) |

-------

### Concept Set 4 (Do in order) - Design & Path Manipulation
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Simplify Path | Amazon, Microsoft, Google | [LeetCode 71](https://leetcode.com/problems/simplify-path/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/12_simplify_path.py) |
| 2 | Implement Queue using Stacks | Amazon, Microsoft | [LeetCode 232](https://leetcode.com/problems/implement-queue-using-stacks/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/16_implement_queue_using_stacks.py) |

### Questions
| # | Problem | Companies | Question | Solution |
|---|---------|-----------|-----|----------|
| 1 | Implement Stack using Queues | Amazon, Microsoft | [LeetCode 225](https://leetcode.com/problems/implement-stack-using-queues/) | [Python](https://github.com/ShubhiJain67/dsa-101/blob/main/stacks/17_implement_stack_using_queues.py) |

---------

## Important Points
- If you find yourself asking "what was the most recent unresolved X" while scanning left to right, that's a monotonic stack, even if the problem doesn't mention "stack" anywhere in the description
- Monotonic stack problems are easy to get backwards - before coding, explicitly state: am I keeping this INCREASING or DECREASING, and does a pop happen on `<` or `>`? Write that down first, then code
- A stack of INDICES (not values) is usually more useful than a stack of values - you often need to know the position/distance, not just the value itself (e.g. Daily Temperatures needs "how many days," which is an index difference)
