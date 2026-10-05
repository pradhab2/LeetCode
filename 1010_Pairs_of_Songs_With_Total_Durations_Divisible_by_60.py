from typing import List
class Solution:
    # songs=[30,20,150,100,40], duration :60  o/p: 3
    # find the number of pairs of song that make the duration of the 60 or multiple of 60
    # here the expected op is 3 as [30,150], [20,40] and [20,100] make the total duration 60 or multiple of 60
    # songs=[60, 60, 60], duration :60  o/p: 2
    def numPairsDivisibleBy60(self, songs:List[int])-> int:
        remainder_counts=[0]*60
        pair_count = 0
        for song in songs:
            rem = song % 60
            target = (60 - rem) % 60
            pair_count += remainder_counts[target]
            remainder_counts[rem] += 1

        return pair_count

sl = Solution()
# print(sl.numPairsDivisibleBy60([30,20,150,100,40]))
print(sl.numPairsDivisibleBy60([60, 60, 60]))





