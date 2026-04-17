# [Same Tree](https://leetcode.com/problems/same-tree)

## Intuition

My idea how to solve this problem is using a **DFS** (here with the recursive implementation) to recursively compare each possible node from the first tree with the equivalent one from the other tree. This way, we know the trees are not the same and return `False` once we reach a node that does not have the same value on both trees.

## Approach

**DFS (Recursive):** At each step, we compare a node `p` from the first tree with the corresponding node `q` from the second tree.
1. **Base Case:**
  
## Complexity

- **Time Complexity**: $O(n)$
  - Explanation why the solution has this time complexity
- **Space Complexity**: $O(h)$, where $h$ is the height of the tree
  - Explanation why the solution has this space complexity
 
## Key Takeaways
- What I learned from this problem
