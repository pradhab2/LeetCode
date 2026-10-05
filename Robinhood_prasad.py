from collections import defaultdict

import heapq
class Solution(object):
    """
    Your function will be called with a list/array of strings of the format "userId,stockSymbol" -
    for example, ["123,AAPL", "456629,GOOG"].

    It should calculate a leaderboard of stock picks - that is, the stocks that users picked most, with the number of users
     that picked them - and return this leaderboard as an ordered list/array of strings in the form "stockSymbol,numberOfPicks"
     - for example, ["AAPL,54", "GOOG,31", "MMM,4", ...].

    Implementation notes:

    The output should be in descending order, based on the number of picks.
    If a user has more than one pick, you should select only their first pick (the one with the lowest index),
    and ignore later picks (don't raise an error).
    We don't mind too much about having perfect runtime efficiency
    - it's OK to have a non-optimal solution as long as it's not exponential time.

    Extra Bits (Tests 5 - 6)

    Extend your solution to handle two more requirements:

    Test 5: Have your program ignore any extra whitespace around either the user ID or the stock symbol (e.g. interpret 24231, TWLO as the user ID 24231 and the stock TWLO)

    Test 6: Only output the top 5 picks in the leaderboard, not all of them. (If there are less than 5 picks, output just that many; don't pad to length 5)
    """
    def get_pick_count(self, inp: [str]) :
        usr_stk_map = defaultdict(str)
        int_res = defaultdict(int)

        res = []
        for rec in inp:
            usr, stok = rec.split(",")
            if usr_stk_map[usr.strip()] != stok.strip():
                int_res[stok.strip()] += 1
                usr_stk_map[usr.strip()] = stok.strip()

        ary=[]

        print(int_res)
        for k, v in int_res.items():
            ary.append((-v,k))
        heapq.heapify(ary)

        res1 = [heapq.heappop(ary) for _ in range(2)]

        for v,k in res1:
            res.append(""+k+","+str(-v)+"")
        return res


sl = Solution()

print(sl.get_pick_count(["123,  AAPL", "234,GOGL", "456,MSFT","214,GOGL","143,AAPL","734,GOGL"]))
