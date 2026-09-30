class Solution:
    def hasDuplicate(self, a: List[str]) -> bool:
        c = Counter(a)
        for key, val in c.items():
            if key != "." and val > 1:
                return True

        return False
            


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_arr = [None] * 9
        cube_arr = [None] * 9

        for i, a in enumerate(board):
            if self.hasDuplicate(a):
                return False

            cube_arr[i] = [a[s:s+3] for s in range(0, len(a), 3)]
            col_arr[i] = [board[j][i] for j in range(9)]

        for a in col_arr:
            if self.hasDuplicate(a):
                return False

        for i in (0, 3, 6):
            for j in (0, 1, 2):
                a = (
                    cube_arr[i][j]
                    + cube_arr[i+1][j]
                    + cube_arr[i+2][j]
                )

                if self.hasDuplicate(a):
                    return False

        return True
            


