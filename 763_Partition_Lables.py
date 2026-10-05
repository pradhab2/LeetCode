""" 763: Partition labels
inp_str: "ababcbaca defegde hijhklij"
op : [9, 7, 8]
Partition the string such that no repeating characters present in other partition ,
 put the length of each partition to the result
"""
class PL(object):
    def partition_lables(self,inp_str):
        dct={}
        res=[]
        for i,c in enumerate(inp_str):
            dct[c]=i
        # print(dct)
        left=0
        right=0
        for i,c in enumerate(inp_str):
            right=max(right,dct[c])
            if i==right:
                res.append(right-left+1)
                left=i+1
        return res

pl=PL()
print(pl.partition_lables("ababcbacadefegdehijhklij"))
assert pl.partition_lables("ababcbacadefegdehijhklij") == [9,7,8]

