
""" --- Length of Longest Increasing Subsequences ----

Here the logic is Iterate through the input with initial result array [].
search the new digit postion in the result array using binary search, if the 
it is == length means it is big number then append to the result.
Else replace the digit in the postion of the BSR postion. """


class LIS():

	def bsr(self,ary, tgt):     # classic binary search
		left=0
		right=len(ary)-1

		while left <= right:
			mid=left + (right - left)/2
			if ary[mid] == tgt:
				return mid
			elif ary[mid] > tgt:
				right= mid -1
			else:
				left=mid+1
		return left


	def lis_max_len(self,inp_list):
		res=[]

		for digit in inp_list:
			pos=self.bsr(res,digit)

			if pos == len(res):
				res.append(digit)
			else:
				res[pos] = digit
		return len(res) #(res)


ls=LIS()
print(ls.lis_max_len([5,3,6,8,7,12]))     # LIS is either 3,6,8,12 or 3,6,7,12 , so the length is 4
assert ls.lis_max_len([5,3,6,8,7,12]) == 4

""" inp : 
5,3,6,8,7,12

5
3
3,6
3,6,8
3,6,7
3,6,7,12 : result .

Here the time complexity is O(nlog(n))
         space complexity in n where n is the number element of the string """



