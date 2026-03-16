class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        rev = 0
        num = abs(x)
        
        while num != 0:
            digit = num % 10
            num = num // 10
            if rev > INT_MAX // 10:
                return 0
            if rev == INT_MAX // 10 and digit > 7:
                return 0
            
            rev = rev * 10 + digit
        
        rev = rev if x >= 0 else -rev
        
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        
        return rev