from typing import List
from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adjacent = {
            0: [1,3],
            1: [0,2,4],
            2: [1,5],
            3: [0,4],
            4: [1,3,5],
            5: [2,4]
        }

        board_as_string = "".join([str(c) for row in board for c in row])
        q = deque([(board_as_string.index("0"),board_as_string, 0)])
        visited= set([board_as_string])
        while q:
            i,board_as_string, length = q.popleft()

            if board_as_string =="123450":
                return length
            
            board_as_array = list(board_as_string)
            for j in adjacent[i]:
                new_board_arr = board_as_array.copy()
                new_board_arr[i], new_board_arr[j] = board_as_array[j], board_as_array[i]
                new_board="".join(new_board_arr)
                if new_board not in visited:
                    q.append((j, new_board, length+1))
                    visited.add(new_board)
        return -1