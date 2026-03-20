class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1      
        INT_MIN = -2**31         
        
        i = 0
        
        while i < len(s) and s[i] == " ":
            i += 1
        
        sign = 1
        if i < len(s) and (s[i] == "-" or s[i] == "+"):
            if s[i] == "-":
                sign = -1
            i += 1

        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1
        
        result = sign * result
        
        result = max(INT_MIN, min(INT_MAX, result))
        
        return result