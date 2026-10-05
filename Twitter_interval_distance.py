""" Given a list of intervals in the format [[l_1,r_1],[l_2,r_2],[l_3,r_3].....[l_n,r_n]].
where l_1 and r_1 are the left and right bounds of the interval. Find the distance covered by these intervals.
Example:
    [[1,5],[7,10],[8,12],[2,6]] covers 10 units

Visualization:
  ______
 |     |    ______
 |  ___|__ |   __|____
 | |   | | |  |  |   |
---------------------------
 1 2   5 6 7 8  10  12

 [1,5]  => 5-1 = 4
 [2,6]  => 6-5 = 1
 [7,10] => 10-7 = 3
 [8,12] => 12-10= 2
 So total distance is 4+1+3+2
"""

class Distance():
    def find_distiance(self,intervals:[[int,int]])-> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[0])   # [[1, 5], [2, 6], [7, 10], [8, 12]]  O(n(logn))
        last_left, last_right = intervals[0]
        dist = last_right - last_left
        for left,right in intervals[1:]:
            if left < last_right:
                dist += max(right,last_right) - last_right   # Current right amy be smaller then last right
            elif left > last_right:
                dist += right - left
            last_right = max(last_right, right)

        return dist

ds=Distance()
print(ds.find_distiance([[1,5],[7,10],[8,12],[2,6]]))
assert ds.find_distiance([]) == 0
assert ds.find_distiance([[1,5],[7,10],[8,12],[2,6]]) == 10



