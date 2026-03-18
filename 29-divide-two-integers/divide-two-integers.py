class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        
        while dividend >= divisor:
            i = 0
            while (divisor << i) <= dividend:
                i += 1
            i -= 1
            dividend -= (divisor << i)
            count += (1 << i)
        
        if negative:
            count = -count
        
        return count
                
        

        