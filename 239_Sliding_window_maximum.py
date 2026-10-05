
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums,k) :
    # def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        d = deque()
        output = []

        for i in range(len(nums)):
            if d and d[0] == i - k:  # if index is more than window ignore the left items from deque
                d.popleft()
            while d and nums[d[-1]] <= nums[i]: # if the incoming number is greater or equal to the last(left most)
                # number of the deque, keep on popping
                d.pop()

            d.append(i)
            if i >= k-1 :
                output.append(nums[d[0]])

        return output

sl=Solution()
print(sl.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
# ans : [3, 3, 5, 5, 6, 7]
print(sl.maxSlidingWindow([1,-1],1))