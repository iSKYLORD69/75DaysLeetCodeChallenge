from math import gcd

class Solution:
    def gcdSum(self, nums):

        prefix = []

        currentMax = 0

        for num in nums:

            currentMax = max(currentMax, num)

            prefix.append(gcd(num, currentMax))

        prefix.sort()

        left = 0
        right = len(prefix) - 1

        ans = 0

        while left < right:

            ans += gcd(prefix[left], prefix[right])

            left += 1
            right -= 1

        return ans