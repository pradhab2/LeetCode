class Solution():
    def ph_num_comb(self,digits):
        res=[]
        d={"2":"abc","3":'def',"4":'ghi'}
        start=list(d[digits[0]])

        for digit in digits[1:]:
            start = [i+j for i in start for j in d[digit]]

        return start



sl = Solution()
print(sl.ph_num_comb("234"))