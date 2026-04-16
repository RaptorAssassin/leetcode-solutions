# [Two Sum](https://leetcode.com/problems/two-sum/)

## Intuition

My first idea was to use the brute force method, **looping** over every element in the array and checking if there is another element which then adds up to `target`. That approach would result in a **time complexity of $O(n^2)$**, 
which is too slow to be considered for huge amounts of data. To optimize the time complexity, I used a **hash map** to store values I have already seen to be able to access them quickly.

## Approach

- **Hash Map**: The hash map `prev_map` is used to store all the values that have already been seen. The key is the number and the value its index.
- **One-Pass Search**: The algorithm iterates over the array and calculates `complement = target - current` every time to check if it exists in the `prev_map`.
- **Check & Return**: When `complement` exists in the `prev_map`, both the current index and the the value of `prev_map[complement]` get returned.

## Complexity

- **Time Complexity**: $O(n)$
  - We traverse the list only once, with each lookup in the hash map taking only $O(1)$ time.
- **Space Complexity**: $O(n)$
  - In the worst case, we need to store all `n` values in the hash table.
 
## Key Takeaways
- I learned that checking if a key in a hash map exists is way faster than searching an array, taking $O(1)$ instead of $O(n)$ time.
