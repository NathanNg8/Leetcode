class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        count = 0 
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                index = i 
                count = 0  
                for j in range(len(needle)):
                    if i + j >= len(haystack) or haystack[i + j] != needle[j]:
                        break
                    count += 1
                if count == len(needle):
                    return index

        return -1