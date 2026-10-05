
""" inp "12" : ["AB","L"] o/p 2 
    inp "226": ["BZ","BBF",VF] 
    """

def decodeWays(nums):

	if not nums or nums[0]=='0':
		return 0
	if len(nums) == 1:
		return 1

	l=len(nums)
	cnt1,cnt2= 1,1
	res=0

	for i in range(1,l):
		count = 0
		d=ord(nums[i]) - ord('0')
		dd=(ord(nums[i-1]) - ord('0')) * 10 +d

		if d > 0:
			count += cnt2
			# print(count)
		if 10 <= dd <= 26:
			count += cnt1
			# print(d)


		cnt1 = cnt2
		cnt2 = count

	return cnt2

print(decodeWays('240'))
assert decodeWays('296')== 1
assert decodeWays('246')== 2
assert decodeWays('2469')== 2
assert decodeWays('2416')== 4
# assert decodeWays('240')== 0

""" Decode ways using DP solution as above """
def decwaysDP(nums):
	l=len(nums)

	dp= [0 for _ in range(l+1)]

	dp[0]=1
	dp[1]=1

	for i in range(2,l+1):
		singleDgtNum= int(nums[i-1:i])
		dublDgtNum  = int(nums[i-2:i])

		if singleDgtNum > 0:
			dp[i] = dp[i-1]
		if 10<= dublDgtNum <= 26:
			dp[i] += dp[i-2]

	print(dp)
	return dp[-1]

# print(decwaysDP('2'))


