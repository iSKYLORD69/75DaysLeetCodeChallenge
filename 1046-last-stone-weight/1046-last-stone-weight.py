import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to max heap using negatives
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)  # largest
            x = -heapq.heappop(stones)  # second largest

            if y != x:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0