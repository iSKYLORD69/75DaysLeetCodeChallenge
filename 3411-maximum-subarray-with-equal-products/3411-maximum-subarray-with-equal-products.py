from math import gcd

class Solution:
    def maxLength(self, nums):
        ans = 0
        n = len(nums)

        for i in range(n):

            product = 1
            g = 0
            l = 1

            for j in range(i, n):

                product *= nums[j]

                g = gcd(g, nums[j])

                l = l * nums[j] // gcd(l, nums[j])

                if product == g * l:
                    ans = max(ans, j - i + 1)

        return ans