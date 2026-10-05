class Solution():
    """
    inp                k=3 (rotate the inp array  3 times
    [1,2,3,4,5,6,7]
    7,1,2,3,4,5,6
    6,7,1,2,3,4,5
    5,6,7,1,2,3,4  o/p

    j = (i+k)%len(inp_aray)

    """

    def rotate_arry_k_times(self,inp_aray,k):

        l=len(inp_aray)
        res = [''] * l
        for i in range(l):
            j = (i+k) % l
            res[j]=inp_aray[i]
        return res


if __name__=='__main__':
    sl=Solution()
    print(sl.rotate_arry_k_times( [1,2,3,4,5,6,7],3))


