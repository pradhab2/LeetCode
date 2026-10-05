""" Medium
There is an integer array nums sorted in ascending order (with distinct values).
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return mid
            # check left is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            # check right is sorted
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1


sl=Solution()
print(sl.search([4,5,6,7,0,1,2,3],3)) # 7
print(sl.search([4,5,6,7,0,1,2,3],0)) # 4