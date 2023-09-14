import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Same number cannot appear twice on the same row/column
        # 3 x 3 Grid can also not have repeating numbers

        # Detecting Dupes with a Hash Set
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (row / 3 , col / 3)

        # Iterate through the entire board
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # Check if the current value is in our set
                if board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

                