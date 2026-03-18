class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        #This is prefix part
        pre = 1
        for i in range(n):
            result[i] = pre
            pre *= nums[i]

        #This is suffix part
        suf = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suf
            suf *= nums[i]

        return result
        
