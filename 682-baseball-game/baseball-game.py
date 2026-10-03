class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        results = []
         
        for i in operations: 
            if i == '+':
                results.append(results[-1] + results[-2])
            elif i == 'D':
                results.append(results[-1] * 2)
            elif i == 'C':
                results.pop()
            else: 
                results.append(int(i))
                
        return sum(results)
