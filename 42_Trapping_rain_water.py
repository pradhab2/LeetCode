
"""
Input : [0,1,0,2,1,0,1,3,2,1,2,1] Expected result=6

Given a list oh heights of blocks, need to find the number unit of water it can hold. """

class RainWater():
	def trapRainWater(self,heights):
		leftMax=heights[0]
		rightMax=heights[-1]

		left,right=0,len(heights)-1
		if right < 3:
			return 0
		res=0
		while left <= right:
			if leftMax <= rightMax:
				leftMax =max(leftMax,heights[left])
				res += leftMax - heights[left]
				left += 1
			else:
				rightMax =max(rightMax,heights[right])
				res += rightMax - heights[right]
				right -= 1

		return res


rn=RainWater()

assert (rn.trapRainWater([0,1,0,2,1,0,1,3,2,1,2,1])) == 6
assert (rn.trapRainWater([3,2,4,1,0,2])) == 4
assert (rn.trapRainWater([3,2,1,0,5,4,2])) == 6
