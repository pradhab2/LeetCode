""" Input is s="paypalishiring"  o/p required in zigzag manner
op: "p a h n
     aplsiig
     y i r"     which is "pahnaplsiigyir"
"""


def convert(s,n):
	if s is None or len(s)==1:
		return s
	lst=[[] for _ in range(n)]
	row=0
	incr=-1
	for c in s:
		lst[row].append(c)
		if row ==0 or row==n-1:
			incr *= -1

		row += incr

		

	for i in range(n):
		lst[i] = ''.join(lst[i])

	return ''.join(lst)

print(convert("paypalishiring",3))
assert convert("paypalishiring",3)=="pahnaplsiigyir"

