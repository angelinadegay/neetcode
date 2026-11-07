class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        for row in range(9):
            hashmap = {}
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in hashmap:
                    print('in hash', board[row][col])
                    return False
                hashmap[board[row][col]] = True
                
        for col in range(9):
            hashmap = {}
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in hashmap:
                    print('in hash', board[row][col])
                    return False
                hashmap[board[row][col]] = True
        for box in range(9):
            hashmap = {}
            box_row = (box // 3) * 3
            box_col = (box % 3) * 3
            for i in range(3):
                for j in range(3):
                    val = board[box_row + i][box_col + j]
                    if val == ".":
                        continue
                    if val in hashmap:
                        return False
                    hashmap[val] = True

        return True
        