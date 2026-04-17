# [Rotate Array](https://leetcode.com/problems/rotate-array)

## Intuition

My idea was to use modulo to calculate the new index of the elements. Then we would place them at their new index, taking the old values from a copy of the original Array.

## Approach

- **Modulo/Remainder Operator %**: The new indices of the items are calculated with the formula `new_index = (old_index + k) % len(nums)`. The new index is taken modulo the length of the `nums` array to make sure overflowing items are added at the beginning of the array.
- **Original Array:** The old values of `nums` are saved into an array called `original`, where the new values for `nums` are taken from later.
  
## Complexity

- **Time Complexity**: $O(n)$
  - Loop over every element in `nums` once
- **Space Complexity**: $O(n)$
  - We need to save a copy of each element in an array.
 
## Key Takeaways
- None
