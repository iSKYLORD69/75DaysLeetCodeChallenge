from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]

        if original == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            # Out of bounds or different color
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if image[r][c] != original:
                return

            # Fill color
            image[r][c] = color

            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image