class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        down = 1 
        row_index = 0 
        rows = [""] * numRows

        if numRows == 1: 
                return s 

        for letter in s:
            rows[row_index] += letter 

            if row_index == numRows - 1: 
                down = -1
            if row_index == 0: 
                down = 1

            if down == 1: 
                row_index += 1
            elif down == -1: 
                row_index -= 1  

        results = "".join(rows)  
        return results


        

          
        