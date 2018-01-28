"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.


Example:

Input: "cbbd"

Output: "bb"

"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_p = ''
        str_len = len(s)
        for i in range(0, str_len):
            start, end = i, i
            while 0 <= start <= end < str_len:
                even_s = s[start:end+2]
                odd_s = s[start:end+1]
                palindrome = ''

                if self.isPalindrome(even_s):
                    palindrome = even_s
                elif self.isPalindrome(odd_s):
                    palindrome = odd_s

                if palindrome:
                    max_p = palindrome if len(palindrome) > len(max_p) else max_p
                    start = start - 1
                    end = end + 1
                else:
                    break

        return max_p

    def isPalindrome(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    test_cases = [
        {
            'input': 'babad',
            'expected': 'bab',
        },
        {
            'input': '',
            'expected': '',
        },
        {
            'input': 'a',
            'expected': 'a',
        },
        {
            'input': 'ab',
            'expected': 'a',
        },
        {
            'input': 'aba',
            'expected': 'aba',
        },
        {
            'input': 'abbc',
            'expected': 'bb',
        },
    ]
    solution = Solution()
    for test_case in test_cases:
        actual = solution.longestPalindrome(test_case['input'])
        try:
            assert test_case['expected'] == actual
            print "Test case passed: s=%s longest=%s" % (test_case['input'], test_case['expected'])
        except AssertionError as e:
            print('Failed to assert that:\n  s: %s\n  Expected: %s\n  Actual:   %s' % (test_case['input'], test_case['expected'], actual))
