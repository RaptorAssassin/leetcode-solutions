# [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array)

## Intuition

When reading "largest Element", a **heap** came into my mind instantly. originally i used a self-implemented version, filling the min heap with `n * -1` to have a self-created max heap. But after doing some research i switched to the internally optimized function `heapq.nlargest()`, which runs faster.

## Approach

- **(Max) Heap**: explanation what it does
  
## Complexity

- **Time Complexity**: $O(n \cdot \log{k})$
  
- The `heapq.nlargest()` is optimized internally:
1. A min heap of size $k$ is initialized.
2. All remaining $n - k$ elements are compared with the root and if smaller pushed or popped into/ the heap, taking $\log{k}$ for a heap of the size $k$. If $k$ is small, the time complexity is nearly $O(n)$.
   
- **Space Complexity**: $O(k)$
  - The size of the heap is limited to $k$, so we don't keep track of unnecessary values.
 
## Key Takeaways
- When you want to keep track of a smallest or biggest value, you use a **Min/Max Heap**.
