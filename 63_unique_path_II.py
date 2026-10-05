import unittest

""" 
The robot can only move either down or right at any point in time.
Find the number of ways a robot can reach to the * from the beginning with hurdles
0 means pass, 1 means hurdle
                        R
   Input obstacleGrid:[[0,0,0],
                       [0,0,0],
                       [0,1,0],
                       [0,0,0]]   Expected Output : 4
                            *
-----------------------------------------------------------
                        R
   Input obstacleGrid:[[0,0,0],
                       [0,1,0],
                       [0,0,0]]   Expected Output : 3
                            *                          """


class Solution():
    # def uniquePathWithObstacles(self, obstacleGrid):
    #     if obstacleGrid[0][0] == 1:
    #         return 0
    #     r, c = len(obstacleGrid), len(obstacleGrid[0])
    #     dp = [[0 for _ in range(c)] for _ in range(r)]    
    #     for i in range(r):                 # Each row column 1
    #         if obstacleGrid[i][0] == 0:
    #             dp[i][0] = 1
    #         else:
    #             break
    #     for i in range(c):                 # Each column row 1
    #         if obstacleGrid[0][i] == 0:
    #             dp[0][i] = 1
    #         else:
    #             break
    #     for i in range(1, r):
    #         for j in range(1, c):
    #             if obstacleGrid[i][j] == 0:
    #                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    #
    #     return dp[-1][-1]
    def uniquePathWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(c)]
        # dp = [0] * c
        dp[0] = 1
        for row in obstacleGrid:
            for j in range(c):
                if row[j] == 1:
                    dp[j] = 0
                elif (j > 0):
                    dp[j] = dp[j] + dp[j - 1]
                    # print(dp)
        return dp[c - 1]


class UnitTest(unittest.TestCase):
    def test_1(self):
        sl = Solution()
        obstacleGrid = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 1, 0],
                        [0, 0, 0]]

        # print(sl.uniquePathWithObstacles(obstacleGrid))
        self.assertEqual(sl.uniquePathWithObstacles(obstacleGrid), 4)

    def test_2(self):
        sl = Solution()
        obstacleGrid = [[0, 0, 0],
                        [0, 1, 0],
                        [0, 0, 0]]

        # print(sl.uniquePathWithObstacles(obstacleGrid))
        self.assertEqual(sl.uniquePathWithObstacles(obstacleGrid), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
