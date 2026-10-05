import heapq
from collections import defaultdict

class leaderBoard():
    def topLeaders(self, inpList, topN):
        usr_dct = defaultdict(set)
        hp = []
        res = defaultdict()

        for sticker, qty, usr in inpList:
            if sticker not in usr_dct[usr]:
                usr_dct[usr].add((sticker))
                if sticker not in res:
                    res[sticker] = qty
                else:
                    res[sticker] += qty

        print(res)
        # di = [(-v,v,k) for k,v in res.items()]

        return heapq.heapify(list(res.items()))

        # return heapq.nlargest(topN,res,key = res.get )
        # return heapq.nlargest(topN,res.items(),key = lambda x: x[1] )

    # return sorted(res.items(), key = lambda x:x[1],reverse=True)
#
#
lb = leaderBoard()

inpList = [

    ("HOOD", 7, "uid1"),
    ("V", 25, "uid1"),
    ("MSFT", 95, "uid1"),
    ("TSLA", 10, "uid1"),
    ("AAPL", 25, "uid1"),
    ("AAPL", 65, "uid2"),
    ("TSLA", 5, "uid2"),
    ("AAPL", 5, "uid3"),
    ("TSLA", 80, "uid3"),
    ("AAPL", 5, "uid1")]

res=lb.topLeaders(inpList,3)



    # def topLeaders(self, inpList, topN):
    #     usr_dct = defaultdict(set)
    #     res = {}
    #
    #     for rec in inpList:
    #         sticker=rec.split(",")[0].strip()
    #         usr=rec.split(",")[1].strip()
    #         if sticker not in usr_dct[usr]:
    #             usr_dct[usr].add((sticker))
    #             if sticker not in res:
    #                 res[sticker] = 1
    #             else:
    #                 res[sticker] += 1
    #
    #     int_res=heapq.nsmallest(len(res), res.items(), key=lambda x: (-x[1],x[0]))
    #     final_res=[]
    #     for item in int_res:
    #         final_res.append(item[0]+','+str(item[1]))
    #
    #
    #     return final_res


# return sorted(res.items(), key = lambda x:x[1],reverse=True)


# lb = leaderBoard()
#
# inpList = [
#
#     ("    HOOD,    uid1"),
#     ("  V   ,   uid1"),
#     ("MSFT,uid1"),
#     ("TSLA,uid1"),
#     ("AAPL,uid1"),
#     ("AAPL,uid2"),
#     ("TSLA,uid2"),
#     ("AAPL,uid3"),
#     ("TSLA,uid1"),
#     ("AAPL,uid1")]
#
# res = lb.topLeaders(inpList, 3)
# print(res)



"""

Question:
Your function will be called with a list/array of strings of the format "userId,stockSymbol" - for example, ["123,AAPL", "456629,GOOG"].

It should calculate a leaderboard of stock picks - that is, the stocks that users picked most, with the number of users that picked them - and return this leaderboard as an ordered list/array of strings in the form "stockSymbol,numberOfPicks" - for example, ["AAPL,54", "GOOG,31", "MMM,4", ...].

Implementation notes:

The output should be in descending order, based on the number of picks.
If a user has more than one pick, you should select only their first pick (the one with the lowest index), and ignore later picks (don't raise an error).
We don't mind too much about having perfect runtime efficiency - it's OK to have a non-optimal solution as long as it's not exponential time.
CodeSignal will call your function with a fixed input array/list each time and check the output against our tests.

You can run all tests with the "Run Tests" button at the bottom right, or a single test by clicking the "play" button on that test in the bottom pane.

Extra Bits (Tests 5 - 6)

Extend your solution to handle two more requirements:

Test 5: Have your program ignore any extra whitespace around either the user ID or the stock symbol (e.g. interpret 24231, TWLO as the user ID 24231 and the stock TWLO)

Test 6: Only output the top 5 picks in the leaderboard, not all of them. (If there are less than 5 picks, output just that many; don't pad to length 5)

"""

