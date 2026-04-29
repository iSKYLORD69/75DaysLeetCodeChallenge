from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue

                if (val, r) in seen or (c, val) in seen or (r//3, c//3, val) in seen:
                    return False

                seen.add((val, r))            # row
                seen.add((c, val))            # column
                seen.add((r//3, c//3, val))   # box

        return True