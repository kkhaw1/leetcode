
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        num = 0
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        start, end = 0, len(s)
        valid_ints = [str(i) for i in range(0, 10)]

        if s[0] == '-':
            sign, start = -1, 1
        elif s[0] == '+':
            sign, start = 1, 1
        for i in range(start, end):
            chr = s[i]
            if chr in valid_ints:
                num = num*10 + int(chr)
            else:
                break
        num = sign * num
        return min(max((-0x7fffffff - 1), num), 0x7fffffff)


if __name__ == '__main__':
    test_cases = [
        {
            'input': ('',),
            'output': (0,),
        },
        {
            'input': (' 42',),
            'output': (42,),
        },
        {
            'input': (' +42',),
            'output': (42,),
        },
        {
            'input': (' -42',),
            'output': (-42,),
        },
        {
            'input': ('abc123def',),
            'output': (0,),
        },
        {
            'input': ('abc-123def',),
            'output': (0,),
        },
        {
            'input': (' -123def',),
            'output': (-123,),
        },
        {
            'input': ('2147483648',),
            'output': (2147483647,),
        },
        {
            'input': ('-2147483649',),
            'output': (-2147483648,),
        },
    ]
    solution = Solution()
    for test_case in test_cases:
        actual = solution.myAtoi(test_case['input'][0])
        try:
            assert test_case['output'][0] == actual
            print "Test case passed: input=%s output=%s, expected:%s" % (test_case['input'][0], actual, test_case['output'][0])
        except AssertionError as e:
            print('Failed to assert that:\n  Expected: %s\n  Actual:   %s\n[%s]' % (test_case['output'][0], actual, test_case['input'][0]))

