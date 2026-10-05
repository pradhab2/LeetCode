"""
# Definition for an Interval. """
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: [[Interval]]) -> [Interval]:
        flattened_sch=[item for sch in schedule for item in sch]
        flattened_sch_sorted=sorted(flattened_sch,key=lambda x:x.start)
        last_end=flattened_sch_sorted[0].end
        res=[]
        for item in flattened_sch_sorted[1:]:
            start = item.start
            end = item.end

            if start > last_end:
                res.append(Interval(last_end,start))
            last_end=max(last_end,end)

        return res

#schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
schedule=[[Interval(1,2),Interval(5,6)],[Interval(1,3)],[Interval(4,10)]]   # Expected result [[3,4]]
sl=Solution()
res=[]
for item in sl.employeeFreeTime(schedule):
    res.append([item.start,item.end])
print(res)

#schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]

schedule=[[Interval(1,3),Interval(6,7)],[Interval(2,4)],[Interval(2,5),Interval(9,12)]]  # Output: [[5,6],[7,9]]

res=[]
for item in sl.employeeFreeTime(schedule):
    res.append([item.start,item.end])
print(res)

