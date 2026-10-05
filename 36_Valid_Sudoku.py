
# from collections import list
class Solution(object):
    def isValidSudoku(self, board) :
        rows, cols, block = set(), set(), set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rkey = (i, board[i][j])
                    ckey = (j, board[i][j])
                    blkkey = (i // 3, j // 3, board[i][j])

                    if rkey in rows or ckey in cols or blkkey in block:
                        return False
                    else:
                        rows.add(rkey)
                        cols.add(ckey)
                        block.add(blkkey)
        return True


sl=Solution()
print(sl.isValidSudoku(
[["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]
))


