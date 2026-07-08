class Solution:
    def nextGreaterElement(self, nums1, nums2):

        ans = []

        for num in nums1:

            index = nums2.index(num)

            found = -1

            for j in range(index + 1, len(nums2)):

                if nums2[j] > num:
                    found = nums2[j]
                    break

            ans.append(found)

        return ans