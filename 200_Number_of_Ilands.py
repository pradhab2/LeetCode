class Solution():
    def num_of_ilands(self, grid: [[str]]) -> int:
        if not grid:
            return 0
        num_of_ilands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_of_ilands += self.dfs(grid, i, j)
        return num_of_ilands

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0" :
            return 0
        grid[i][j] = "0"
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)


        return 1


class Solution2:
    def numIslands_union_find(self, grid: [[str]]) -> int:

        if len(grid) == 0: return 0
        row = len(grid);
        col = len(grid[0])
        self.count = sum(grid[i][j] == '1' for i in range(row) for j in range(col))
        parent = [i for i in range(row * col)]

        def find(x):
            if parent[x] != x:
                x = find(parent[x])
            return parent[x]

        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot: return
            parent[xroot] = yroot
            self.count -= 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i * col + j

                if i < row - 1 and grid[i + 1][j] == '1':
                    union(index, index + col)
                if j < col - 1 and grid[i][j + 1] == '1':
                    union(index, index + 1)
        return self.count


import unittest
class test(unittest.TestCase):
    def test_1(self):
        grid = [["1", "1", "1", "0", "1"],
                ["1", "1", "0", "0", "1"],
                ["1", "1", "1", "0", "1"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]]

        sl = Solution()
        # print(sl.num_of_ilands(grid))
        # print(grid)
        self.assertEqual(sl.num_of_ilands(grid), 2)

    def test_2(self):
        grid = [["0", "0", "1", "0", "1"],
                ["0", "1", "0", "0", "1"],
                ["0", "0", "1", "0", "1"],
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]]

        sl = Solution()
        # print(sl.num_of_ilands(grid))
        # print(grid)
        self.assertEqual(sl.num_of_ilands(grid), 4)
    def test_3(self):
        grid = [["1", "1", "1", "0", "1"],
                ["1", "1", "0", "0", "1"],
                ["1", "1", "1", "0", "1"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]]

        sl = Solution2()
        # print(sl.num_of_ilands(grid))
        # print(grid)
        self.assertEqual(sl.numIslands_union_find(grid), 2)

    def test_4(self):
        grid = [["0", "0", "1", "0", "1"],
                ["0", "1", "0", "0", "1"],
                ["0", "0", "1", "0", "1"],
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]]

        sl = Solution2()
        # print(sl.num_of_ilands(grid))
        # print(grid)
        self.assertEqual(sl.numIslands_union_find(grid), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
