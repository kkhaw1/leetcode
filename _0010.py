class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = ' ' + s
        p = ' ' + p
        s_len, p_len = len(s), len(p)
        m = [[False for _ in range(0, p_len)] for _ in range(0, s_len)]
        m[0][0] = True
        for i in range(1, p_len):
            if p[i] == '*':
                m[0][i] = m[0][i - 2]

        for j in range(1, s_len):
            for k in range(1, p_len):
                if s[j] == p[k] or p[k] == '.':
                    m[j][k] = m[j - 1][k - 1]
                elif p[k] == '*':
                    m[j][k] = m[j][k - 2]
                    if p[k - 1] == '.' or p[k - 1] == s[j]:
                        m[j][k] = m[j][k] or m[j - 1][k]
                else:
                    m[j][k] = False

        return m[s_len - 1][p_len - 1]


if __name__ == '__main__':
    test_cases = [
        {
            'input': ('abc', 'abc'),
            'expected': True,
        },
        {
            'input': ('abc', 'a'),
            'expected': False,
        },
        {
            'input': ('abc', 'a.c'),
            'expected': True,
        },
        {
            'input': ('abc', 'ab*c'),
            'expected': True,
        },
        {
            'input': ('abbbbbbc', 'ab*c*d*e*'),
            'expected': True,
        },
        {
            'input': ('aa', 'a*'),
            'expected': True,
        },
    ]
    solution = Solution()
    for test_case in test_cases:
        i = test_case['input']
        actual = solution.isMatch(i[0], i[1])
        try:
            assert test_case['expected'] == actual
            print "Test case passed: x=%s res=%s" % (test_case['input'], test_case['expected'])
        except AssertionError as e:
            print('Failed to assert that:\n  x: %s\n  Expected: %s\n  Actual:   %s' % (test_case['input'], test_case['expected'], actual))
