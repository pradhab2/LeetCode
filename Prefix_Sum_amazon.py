""" Given an array of integers , determine the number of ways the enrire array be split
    into two non empty subarrays , left and right, such that the sum of elements in the
    left subarray is greater than the sum of elements in the right sub array

    i) arr: [10,4,-8,7]   o/p: 2 i.e there are 2 ways possible
         [10],[4,-8,7]
         [10,4],[-8,7]
                            This combi is not valid [10,4,-8] [7]
    ii) arr: [10,-5,6]   o/p: 1 way
         [10][-5,6]
    iii) arr : [-3,-2,10,20,-30]    o/p 2 ways
         [-3,-2,10][20,-30]
         [-3,-2,10,20][-30]
 This question is related to prefix sum.
 1. Find the left prefix sum
 2. Find the right prefix sum
 3. Find the number of elements where left > right ignoring the rightmost and leftmost element.
               [10,4,-8,7]
 left prefix : 10,14,6,13
 right prefix: 13,3,-1,7

 14 > 3 , 6> -1 so the ans is 2 (ignore the first and last as it yield empty subarray to left/right)


         """

def pfxsum(arr):
    # leftPfxSum=[]
    # sum=0
    # for num in arr:
    #     sum += num
    #     leftPfxSum.append(sum)
    # return leftPfxSum

    # ln=len(arr)
    # lftprfxsm= [sum(arr[:i+1]) for i in range(ln)]
    # rtprfxsm =[sum(arr[i:]) for i in range(ln)]
    # res=0
    # for i in range(1,ln-1):
    #     if lftprfxsm[i] > rtprfxsm[i]:
    #         res += 1
    # return res
    res=0
    leftPrefixSum=[]
    cuml_sum=0
    for num in arr:
        cuml_sum += num
        leftPrefixSum.append(cuml_sum)
    print(leftPrefixSum)
    rightPrifixSum=[cuml_sum]
    for num in arr[:-1]:
        cuml_sum -= num
        rightPrifixSum.append(cuml_sum)
    print(rightPrifixSum)

    for i in range(1,len(arr)-1):
        if leftPrefixSum[i] > rightPrifixSum[i]:
            res += 1
    return res



# print(pfxsum( [10,4,-8,7]))
print(pfxsum( [3,4,5,6]))
# assert pfxsum([10,4,-8,7]) == 2
# assert pfxsum([10,-5,6]) == 1
# assert pfxsum([-3,-2,10,20,-30]) == 2




