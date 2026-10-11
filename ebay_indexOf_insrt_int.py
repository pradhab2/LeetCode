""" Given a sorted List and an integer,
    return the index where it is going to be inserted to keep the array sorted """
import unittest as ut



def searchInsert( nums, target) :
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left

# print(searchInsert([1,3,5,6],2)) # o/p 1

def firstBadVersion(ary):
    left =0
    right= len(ary)-1
    res= -1
    while left <= right:
        mid = left+(right - left)//2  # in python we can use (left+right)//2
        if ary[mid] == 1:
            res = mid
            right = mid - 1  # right -= 1
        else:
            left = mid + 1   # left += 1
    return res

print(firstBadVersion([0,0,0,1,1,1]))

# def leftMostColWithOne(inpList):
#     fin_res = float('inf')
#
#     for rec in inpList:
#         leftMostCol=firstBadVersion(rec)
#         if leftMostCol < fin_res and leftMostCol != -1:
#             fin_res = leftMostCol
#     return fin_res if fin_res != float('inf') else -1
#
#
#

#
# print(leftMostColWithOne([[0,0,0,0,0,0],
#                           [0,0,0,1,1,1],
#                           [0,0,0,0,1,1]]))
#
# def leftMostColWithOne_2(inp_list):
#     rows=len(inp_list)
#     cols=len(inp_list[0])
#
#
#
# # Leetcode 300: Longest Increasing Subsequence using DP
# # j  i
# #[10,9,2,5,3,7,101,18]
#
# # DP : [1,1,1,1,1,1,1,1,]
#
# def lengthOfLIS( nums: [int]) -> int:
#     cnt=0
#     dp = [1 for _ in nums]
#     for i in range(1,len(nums)):
#         for j in range(i):
#             if nums[j] < nums[i]:
#                 if dp[i] <= dp[j]:
#                     dp[i] = dp[j] + 1
#                 # if dp[i] > cnt:
#                 #     cnt = dp[i]
#         print(dp)
#
#     print(dp)
#     return max(dp)#cnt

# print(lengthOfLIS([10,9,2,5,3,7,101,18]))
# print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
#
# print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
#
