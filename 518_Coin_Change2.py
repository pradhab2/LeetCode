"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
]The answer is guaranteed to fit into a signed 32-bit integer.
Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
DP array:
   0  1  2  3  4  5
0 [1, 0, 0, 0, 0, 0]
1 [1, 0, 0, 0, 0, 0],
2 [1, 0, 0, 0, 0, 0],
5 [1, 0, 0, 0, 0, 0]

     0  1  2  3  4  5   <- j(amount)
0  [[1, 0, 0, 0, 0, 0],
1   [1, 1, 1, 1, 1, 1],
2   [1, 1, 2, 2, 3, 3],
5   [1, 1, 2, 2, 3, 4]]
^
i(coins)
"""
import unittest


class Solution:
    def coin_change2(self, amount: int, coins: [int]) -> int:
        ln_coins = len(coins)
        # first column should be 1
        dp = [[1 if j == 0 else 0 for j in range(amount + 1)] for i in range(ln_coins+1)]

        for i in range(1,ln_coins+1):
            for j in range(1,amount+1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i-1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)
        return dp[ln_coins][amount]

    def coin_change2_aprch_2(self, amount: int, coins: [int]) -> int:
        dp = [1 if i == 0 else 0 for i in range(amount + 1)]
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] += dp[i-coin]
                print(dp)
        return dp[amount]


obj=Solution()
# print(obj.coin_change2_aprch_2(5,[5,2,1]))
# print(obj.coin_change2(5,[1,2,5]))
print(obj.coin_change2(5,[1,2,3]))

#
# class Unittest(unittest.TestCase):
#     def test1(self):
#         obj=Solution()
#         self.assertEqual(obj.coin_change2(5,[1,2,5]),4)
#
# if __name__ == '__main__':
#     unittest.main()
