class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0 , 0
        for letter in moves: 
            if letter == "U":
                y += 1
            elif letter == "D":
                y -= 1
            elif letter == "R":
                x += 1
            elif letter == "L":
                x -= 1

        if x == 0 and y == 0: 
            return True
        else: 
            return False