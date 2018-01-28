"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        new_s = ''
        len_s = len(s)
        level = 0
        direction = 1
        if numRows == 1:
            new_s = s
        else:
            strs = ['' for _ in range(0, numRows)]
            for i in range(0, len_s):
                strs[level] += s[i]

                if (level + direction) >= numRows:
                    direction = -1
                elif (level + direction) < 0:
                    direction = 1

                level = level + direction

            for level_str in strs:
                new_s += level_str

        return new_s



if __name__ == '__main__':
    test_cases = [
        {
            'input': ('abcdef', 3),
            'expected': 'aebdfc',
        },
        {
            'input': ('PAYPALISHIRING', 3),
            'expected': 'PAHNAPLSIIGYIR',
        },
        {
            'input': ('ABC', 1),
            'expected': 'ABC',
        },
    ]
    solution = Solution()
    for test_case in test_cases:
        s, numRows = test_case['input']
        actual = solution.convert(s, numRows)
        try:
            assert test_case['expected'] == actual
            print "Test case passed: s=%s longest=%s" % (test_case['input'], test_case['expected'])
        except AssertionError as e:
            print('Failed to assert that:\n  s: %s\n  Expected: %s\n  Actual:   %s' % (test_case['input'], test_case['expected'], actual))
