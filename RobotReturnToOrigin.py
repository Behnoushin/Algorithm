# Robot Return to Origin
# - Given a string `moves` representing a sequence of moves by a robot on a 2D plane.  
# - Valid moves: 'R' (right), 'L' (left), 'U' (up), 'D' (down).  
# - Return `True` if the robot returns to the origin (0,0) after all moves, otherwise `False`.  

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        return x == 0 and y == 0