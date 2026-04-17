# [Same Tree](https://leetcode.com/problems/same-tree)

## Intuition

My idea how to solve this problem is using a **DFS** (here with the recursive implementation) to recursively compare each possible node from the first tree with the equivalent one from the other tree. This way, we know the trees are not the same and return `False` once we reach a node that does not have the same value on both trees.

## Approach

**DFS (Recursive):** At each step, we compare a node `p` from the first tree with the corresponding node `q` from the second tree.
1. **Base Case:** If both `p` and `q` are None, the subtrees are identical.
2. **Value Mismatch:** If `p` does not equal `q`, we return False.
3. **Recursive Step:** We move a step deeper and compare `p.left` with `q.left` and `p.right` with `q.right`. 
  
## Complexity

- **Time Complexity**: $O(n)$
  - The algorithm visits every node in the two trees once.
- **Space Complexity**: $O(h)$, where $h$ is the height of the tree
  - For every layer of the tree, we do one more recursive function call taking space in the Call Stack.
 
## Key Takeaways
- For traversing two trees or graphs at the same time, pass both nodes as arguments to be able to use both of them for comparison etc in one recursion level
