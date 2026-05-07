# [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

## Intuition

When seeing the problem, I wondered how to keep track which node to pick from all the linked lists. This led me to using a **min heap** to always have access to the node that currently has the smallest value. My idea was to loop through all list nodes, traversing all the `k` linked lists and always pick the currently smallest value until all have been used and the new, merged linked list, is done.

## Approach

The problem is solved using a min heap and traversing all the linked lists, picking the node with the smallest value every time. 
- **Min Heap**: Stores a tuple built from `(value of the node, index of the node in the linked list, current ListNode)`. The heap sorts based on element `[0]` of the tuple, which is the value. At `[1]` there is the index of the node in its list to prevent collisions, and last we got the corresponding `ListNode` object wich is used to traverse the list further.
- **Loops**: Loops are used to traverse all the linked lists. In the start, the first values are added to the heap. Then the smallest value is popped from the heap and added to the result list and if existing, the current `ListNode.next` is added to the heap. This is repeated until all linked lists got fully merged into the result list.
- **Linked List Traversal**: Two pointers, `curr` and `dummy` are used to build the new, merged, linked list. The `curr` pointer assembles the new list and stays at the the end of the list. `dummy` stays at the start and is used to prevent some edge cases like having no nodes in the linked list. 
  
## Complexity

**Time Complexity**: $O(n \cdot \log{k})$
  - **n**: We loop through all *n* elements once.
  - **log k**: We need to build a heap that contains at most k elements, taking *log k* time.

**Space Complexity**: $O(k)$
  - We store the nodes in a heap that is at most of size *k*.
 
## Key Takeaways
- When looking for a minimum value, a heap is almost always the solution.
- I Learned how to optimize memory usage by limiting the heap to a specific size.
