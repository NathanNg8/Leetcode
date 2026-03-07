class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        reversed_num = [0] * len(string)
        num = [0] * len(string)
        count = 0 

        for i in reversed(string):
            reversed_num[count] = i 
            num[count] = string[count] 
            count += 1
        
        if num == reversed_num:
            return True
        else:
            return False