class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 
        for i in reversed(s):
            if i.isspace():
                if count > 0: 
                    break
            else:
                    count += 1
        return count


        