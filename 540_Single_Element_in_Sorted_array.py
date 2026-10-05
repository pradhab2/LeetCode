class Solution:
    def singleNonDuplicate(self, nums):

        # for i in range(0, len(nums)-1, 2):
        #
        #     if nums[i + 1] is None: return nums[i]
        #
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]
        # return nums[-1]

        start, end = 0, len(nums) - 1
        while start < end:
            mid = 2 * ((start + end) // 4)
            if nums[mid] != nums[mid + 1]:
                end = mid
            else:
                start = mid + 2

        return nums[start]


a = Solution()
print(a.singleNonDuplicate([1, 1, 2,3,3]))
