class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        123
        """
        rev = 0
        sign = cmp(x, 0)
        x = abs(x)
        while x != 0:
            tmp = rev*10 + x%10
            if tmp > 0x7fffffff:
                return 0
            rev = tmp
            x = x/10
        return rev * sign
        
