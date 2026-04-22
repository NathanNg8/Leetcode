class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            temp = 0 
            
            n_string = str(n)  # update each iteration
            for i in n_string:
                temp += int(i) ** 2 
            
            n = temp
        
        return n == 1