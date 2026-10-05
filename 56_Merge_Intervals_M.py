class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        if not intervals:
            return []
        stack = []
        intervals.sort(key=lambda x: x[0])
        stack.append(intervals[0])
        # last_right = intervals[0][1]
        for left, right in intervals[1:]:
            last_left, last_right = stack[-1]       # [[1, 6], [8, 10], [15, 18]]
            if left <= last_right:
                stack.pop()
                stack.append([last_left, max(last_right, right)])    # stack=[[1,10]]  in case of merge
            else:
                stack.append([left, right])      # in case of non overlapping interval

        return stack

sl=Solution()
print(sl.merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1, 6], [8, 10], [15, 18]]

assert sl.merge([[1,4],[4,5]]) == [[1,5]]
assert sl.merge([[1,4],[0,4]]) == [[0,4]]