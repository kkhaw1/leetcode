class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x > 0 and x % 10 == 0:
            return False
        num = 0
        while num < x:
            num = num * 10 + x % 10
            x = x / 10
        return num == x or (num/10 == x)


if __name__ == '__main__':
    test_cases = [
        {
            'input': (0,),
            'output': (True,),
        },
        {
            'input': (42,),
            'output': (False,),
        },
        {
            'input': (1221,),
            'output': (True,),
        },
        {
            'input': (121,),
            'output': (True,),
        },
        {
            'input': (-2147447412,),
            'output': (False,),
        },
    ]
    solution = Solution()
    for test_case in test_cases:
        actual = solution.isPalindrome(test_case['input'][0])
        try:
            assert test_case['output'][0] == actual
            print "Test case passed: input=%s output=%s, expected:%s" % (test_case['input'][0], actual, test_case['output'][0])
        except AssertionError as e:
            print('Failed to assert that:\n  Expected: %s\n  Actual:   %s\n[%s]' % (test_case['output'][0], actual, test_case['input'][0]))
