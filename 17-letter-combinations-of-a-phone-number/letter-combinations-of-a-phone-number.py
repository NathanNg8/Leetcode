class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        result = [""]

        for digit in digits:
            temp = []
            for combo in result:
                for letter in phone[digit]:
                    temp.append(combo + letter)
            result = temp

        return result

