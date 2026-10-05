def maxSubArray(nums):

    max_sum = total_sum = nums[0]

    for i in nums[1:]:
        total_sum = max(i,total_sum +i)
        max_sum = max(total_sum,max_sum)

    return max_sum



print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# Ans: 6




