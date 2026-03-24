class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def add_binary_builtin(a, b):
            decimal_sum = int(a, 2) + int(b, 2)
            binary_sum = bin(decimal_sum)
            return binary_sum[2:]
        
        return add_binary_builtin(a, b)