from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (start_index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                area = height * (i - index)
                max_area = max(max_area, area)

                start = index

            stack.append((start, h))

        # Remaining bars
        for index, height in stack:
            area = height * (len(heights) - index)
            max_area = max(max_area, area)

        return max_area