import unittest


class Islands():
    def numOfIsland(self, grid):
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        numIsland = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                if grid[i][j] == 1:
                    numIsland += self.dfs(grid, i, j)
        return numIsland

    def dfs(self, grid, i, j):

        if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == 0:
            return 0
        grid[i][j] = 0

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

        return 1


il = Islands()

grid = [[1, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 1]]
print(il.numOfIsland(grid))


class Test(unittest.TestCase):
    def test1(self):
        il = Islands()
        grid = [[1, 0, 0, 1],
                [1, 1, 0, 0],
                [0, 0, 1, 0],
                [1, 0, 1, 1]]
        self.assertEqual(il.numOfIsland(grid), 4)

    def test2(self):
        il = Islands()
        grid = [[1, 0, 0, 1],
                [1, 1, 0, 0],
                [0, 0, 1, 0],
                [1, 0, 0, 1]]
        self.assertEqual(il.numOfIsland(grid), 5)

    def test3(self):
        il = Islands()
        grid = [[1, 0, 0, 1],
                [1, 1, 0, 1],
                [0, 0, 0, 1],
                [0, 0, 0, 1]]
        self.assertEqual(il.numOfIsland(grid), 2)


if __name__ == '__main__':
    unittest.main()
