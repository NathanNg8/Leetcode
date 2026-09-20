class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = [[1]]

        if numRows <= 0:
            return []

        for i in range(1, numRows):
            prev_row = dp[-1]
            current_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)] + [1]
            dp.append(current_row)
            
        return dp

