from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                # Update closest
                if abs(current - target) < abs(closest - target):
                    closest = current

                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return current  # exact match

        return closest