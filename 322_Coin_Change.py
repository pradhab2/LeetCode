"""You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1

"""
from collections import deque

class Solution:
    # DFS Approach
    def coin_change1(self, amount: int, coins: [int]) -> int:
        q=deque([(0,0)])     # first 0 is amount collected so far and the second zero
                             # is the total number of coins so far
        visited=set()

        while q:
            prev_amt,num_coins=q.popleft()
            num_coins+=1
            for coin in coins:
                curr_amt = prev_amt + coin
                if curr_amt == amount:
                    return num_coins
                if curr_amt < amount and curr_amt not in visited:
                    q.append((curr_amt,num_coins))
                    visited.add(curr_amt)
        return -1

    def coin_change1_aprch2(self,amount,coins):
        dp=[float('inf') for i in range(amount+1)]
        dp[0]=0
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],1+dp[i-coin])
                print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1

    def coin_change1_aprch3(self,amount,coins):
        dp=[float('inf') for i in range(amount+1)]
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i],1+dp[i-coin])
                    print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1

sl=Solution()
print(sl.coin_change1_aprch2(11,[1,2,5]))

import unittest

class Unittest(unittest.TestCase):
    def test_scen1(self):
        sl=Solution()
        self.assertEqual(sl.coin_change1(11,[1,2,5]),3)

    def test_scen2(self):
        sl = Solution()
        self.assertEqual(sl.coin_change1(5, [1, 2, 3]), 2)
    def test_scen3(self):
        sl = Solution()
        self.assertEqual(sl.coin_change1(2, [3]), -1)


# if __name__ == '__main__':
#     unittest.main()