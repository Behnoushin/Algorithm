// Robot Return to Origin
// - Check if a sequence of moves returns the robot to (0,0).
// - Valid moves: 'R', 'L', 'U', 'D'

using System;

class Solution
{
    public bool JudgeCircle(string moves)
    {
        int x = 0, y = 0; 

        foreach (char move in moves)
        {
            if (move == 'U') y += 1;
            else if (move == 'D') y -= 1;
            else if (move == 'L') x -= 1;
            else if (move == 'R') x += 1;
        }

        return x == 0 && y == 0; 
    }
}
