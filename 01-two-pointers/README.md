# Two Pointers Pattern

## Pattern Overview

The **Two Pointers pattern** uses two indices that move through a data structure (usually an array or string) to solve problems efficiently.

It is commonly used when:

- The array is **sorted**
- You need to find **pairs**
- You need to remove duplicates
- You need to compare elements from both ends

---

## Common Use Cases

- Pair with target sum
- Removing duplicates
- Rearrange array
- Merge array
- Squaring sorted array
- Palindrome checking
- 3Sum / 4Sum problems

---

## Time Complexity

Usually **O(n)**

Much faster than the naive **O(n²)** approach.

---

## Problems in This Pattern

| Problem | Difficulty |
|------|------|
| Two Sum II | Easy |
| Remove Duplicates from Sorted Array | Easy |
| Valid Palindrome | Easy |
| 3Sum | Medium |

---

## Example Template

```python
left = 0
right = len(nums) - 1

while left < right:
    if condition:
        left += 1
    else:
        right -= 1
