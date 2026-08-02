from functools import lru_cache

class Solution:
    def stoneGame(self, piles):

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return piles[i]

            return max(
                piles[i] - dp(i + 1, j),
                piles[j] - dp(i, j - 1)
            )

        return dp(0, len(piles) - 1) > 0