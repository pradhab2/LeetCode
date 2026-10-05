import heapq
# from collections import defaultdict
# class leaderBoard():
# 	def topLeaders(self,inpList, topN):
# 		usr_dct=defaultdict(list)
# 		hp =[]
# 		res=defaultdict()
		
# 		for sticker,qty,usr in inpList:
# 			if sticker not in usr_dct[usr]: 
# 				usr_dct[usr].append((sticker))
# 				if sticker not in res:
# 					res[sticker] =qty
# 				else:
# 					res[sticker] += qty
				

# 		di =[(v,k) for k,v in res.items()]

# 		# heapq.heapify(di)
# 		# for rec in di:
# 		# 	if len(hp) < topN:
# 		# 		heapq.heappush(hp,rec)
# 		# 	else:
# 		# 		heapq.heappushpop(hp,rec)

# 		# print(hp)
# 		# print([(val,key) for key,val in hp])

# 		# while len(di) >0:
# 		# 	print(heapq.heappop(di))

# 		# return res

# 		res=sorted(di, key = lambda x:x[0],reverse=True)[:topN]

# 		res= [(key,val) for val,key in res]
		
# 		return res

# 		# return sorted(hp, key = lambda x:x[0],reverse=True)


# lb=leaderBoard()

# inpList=[
# ("AAPL",5,"uid1"),
# ("HOOD",7,"uid1"),
# ("V",25,"uid1"),
# ("MSFT",55,"uid1"),
# ("TSLA",10,"uid1"),
# ("AAPL",15,"uid1"),
# ("AAPL",65,"uid2"),
# ("TSLA",5,"uid2"),
# ("AAPL",5,"uid3"),
# ("TSLA",80,"uid3")]

# print(lb.topLeaders(inpList,3))

# res= 	TSLA : 95
# 	 	AAPL : 75
# 	 	MSFT : 55
# 	 	v    : 25
#      	HOOD : 7

# class Node(object):
# 	def __init__(self, name,val):
# 		self.name = name
# 		self.val= val
	
# 	def __lt__(self, other):
# 		return self.name < other.name

# 	def __repr__(self):
# 		return ('Stock order is : %s, %s' %(self.name, self.val))

# heap = [Node('SOFI',2), Node('MSFT',0), Node('TSLA',1), Node('HOOD',4), Node('AAPL',2)]
# heapq.heapify(heap)

# while heap:
# 	res= heapq.heappop(heap)
# 	print(res)
     

        