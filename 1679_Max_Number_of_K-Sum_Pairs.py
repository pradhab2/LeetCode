"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 """
from typing import List


class Solution:
    # Brute force It will exceed time limit for a a longht of the array 10^5
    # def maxOperations(self, nums: List[int], k: int) -> int:
    #     tracker=[]
    #     res=0
    #     for num in nums:
    #         complement=k-num
    #         if num in tracker:
    #             res += 1
    #             tracker.remove(num)
    #
    #         else:
    #             tracker.append(complement)
    #     return res

#     We need to use Two pointer. Two pointer needs the array to be sorted, here we do not need extra space

    def maxOperations(self, nums: List[int], k: int) -> int:
        i=0
        j=len(nums)-1
        res=0
        nums.sort()
        while i < j:
            current_sum = nums[i] + nums[j]
            if current_sum == k:
                res += 1
                i += 1
                j -= 1
            elif current_sum < k:
                i += 1
            else:
                j -= 1
        return res

sl= Solution()
# print(sl.maxOperations([1,2,3,4], 5))   # Expected 2
# print(sl.maxOperations([3,1,3,4,3], 6))  # Expected 1
print(sl.maxOperations([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2))  # Expected 2
# [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5]
