# [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle)

## Intuition

When I saw this problem, I instantly noticed how to do a **recursive** approach, by calculating each value by going one step up in the triangle. But I realized this would lead to way too many redudant calcualations, which got me to use a **Dynamic Programming** approach. We can build the triangle step by step in memory using already calculated values (**Tabulation**) for a $O(n^2)$ **Time Complexity**.

## Approach
The Problem is solved using a **Dynamic Programming (Tabulation)** approach. Instead of calculating each value independantly, the triangle is built using results from previous rows.
1. **Jagged Array initialization:** At first, the entire structure is pre-filled with `1`s. This allows us to focus on the inner values of the triangle only.
2. **Loops:** Two loops are used to iterate over the triangle. The outer loop `i` iterates over the rows, starting from the third one because the first two are always only `1`s. The inner loop `j` goes through the inner indices, starting from index `1` and going up to index `i - 1`.
3. **Result:** After the loops finish, `triangle` contains a fully calculated Pascal's Triangle with `numRows` rows and gets returned.

<details>
  <summary>Visulizations</summary>
    <p align="center">
      <img width="300" alt="Visualization of the loops" src="https://github.com/user-attachments/assets/636bd8ec-4683-4853-b5df-673805f61e28" />
      <img width="300" alt="Representation of the triangle as a jagged array" src="https://github.com/user-attachments/assets/5b82acf2-eeb6-4a4a-9eb7-1012ce904c11" />
    </p>
</details>

  
## Complexity

- **Time Complexity**: $O(n^2)$
  - Calculating every row, we have a time complexity of $\frac{n^2}{2}$ because a triangle half a square, which shortens to just $n^2$.
- **Space Complexity**: $O(n^2)$
  - We are storing the whole triangle. 
 
## Key Takeaways
- Learned how to apply **top-down/tablulation DP** in practice
