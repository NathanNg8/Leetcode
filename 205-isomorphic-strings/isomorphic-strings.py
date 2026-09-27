class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        reverse_mapping = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in mapping:
                if t[i] != mapping[s[i]]:
                    return False    

            if t[i] in reverse_mapping:
                if s[i] != reverse_mapping[t[i]]:
                    return False 

            mapping[s[i]] = t[i]
            reverse_mapping[t[i]] = s[i]
        return True