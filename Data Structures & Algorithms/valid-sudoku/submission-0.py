class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                current_val = board[r][c]
                if(current_val == "."):
                    continue
                if(current_val in rows[r] or current_val in cols[c] 
                or current_val in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(current_val)
                cols[c].add(current_val)
                squares[(r // 3, c // 3)].add(current_val)
        return True
        