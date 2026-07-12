class Solution:
    def arrayRankTransform(self, arr):

        rank = {}

        for num in sorted(arr):

            if num not in rank:
                rank[num] = len(rank) + 1

        return [rank[num] for num in arr]