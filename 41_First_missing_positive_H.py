"""
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.

Input: nums = [3,4,-1,1]
Output: 2

Input: nums = [1,2,0]
Output: 3

Input: nums = [7,8,9,11,12]
Output: 1
"""

def firstMissingPositive(nums:[int])->int:
    l=len(nums)

    for i in range(l):
        if nums[i]> l or nums[i]<=0:
            nums[i]=l+1

    for i in range(l):
        num=abs(nums[i])
        if num > l:
            continue
        if nums[num-1]>0:
            nums[num - 1] = -1 * nums[num-1]

    for i in range(l):
        if nums[i]> 0:
            return i+1

    return l+1

print(firstMissingPositive([3,4,-1,1]))     #op: 2
print(firstMissingPositive([1,2,0]))        #op: 3
print(firstMissingPositive([7,8,9,11,12]))  #op: 1




