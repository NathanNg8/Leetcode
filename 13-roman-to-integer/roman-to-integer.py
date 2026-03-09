class Solution(object):
    def romanToInt(self, s):
        total = 0 
        n = len(s)
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        } 
        
        for i in range(n): 
            if i < n - 1 and values[s[i]] < values[s[i+1]]:
                total -=  values[s[i]]
            else:
                total += values[s[i]]

        return total