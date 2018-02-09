# -*- coding: utf-8; -*-


class Solution(object):
    def search(self, haystack, needle):
        found = False
        left, right = 0, len(haystack) - 1

        while not found and left <= right:
            mid = (left + right) / 2
            if haystack[mid] == needle:
                found = True
            elif haystack[mid] < needle:
                # continue search on the right half
                left = mid + 1
            elif haystack[mid] > needle:
                # continue search on the left half
                right = mid - 1

        return found

    def search_recursive_main(self, haystack, needle):
        left, right = 0, len(haystack) - 1
        return left <= right and self.search_recursive(haystack, needle, 0, len(haystack) - 1)

    def search_recursive(self, haystack, needle, left, right):
        found = False
        mid = (left + right) / 2
        if haystack[mid] == needle:
            found = True
        elif haystack[mid] < needle:
            # continue search on the right half
            left = mid + 1
        elif haystack[mid] > needle:
            # continue search on the left half
            right = mid - 1
        return found or (left <= right and self.search_recursive(haystack, needle, left, right))


if __name__ == '__main__':
    test_cases = [
        {
            'input': ([], 1),
            'output': False,
        },
        {
            'input': ([1], 1),
            'output': True,
        },
        {
            'input': ([1], 2),
            'output': False,
        },
        {
            'input': ([1, 2, 3, 4, 5], 2),
            'output': True,
        },
        {
            'input': (range(0, 1000000), 1),
            'output': True,
        },
    ]
    solution = Solution()

    print "Testing Binary Search:"
    for test_case in test_cases:
        i, o = (test_case['input'], test_case['output'])
        ret_val = solution.search(i[0], i[1])
        try:
            assert o == ret_val
            print "Test case passed: input=%s output=%s" % ((i[0] if len(i[0]) < 10 else len(i[0]), i[1]), o)
        except AssertionError as e:
            print('Failed to assert that:\n  x: %s\n  Expected: %s\n  Actual:   %s' % (i, o, ret_val))

    print "Testing Binary Search Recursive:"
    for test_case in test_cases:
        i, o = (test_case['input'], test_case['output'])
        ret_val = solution.search_recursive_main(i[0], i[1])
        try:
            assert o == ret_val
            print "Test case passed: input=%s output=%s" % ((i[0] if len(i[0]) < 10 else len(i[0]), i[1]), o)
        except AssertionError as e:
            print('Failed to assert that:\n  x: %s\n  Expected: %s\n  Actual:   %s' % (i, o, ret_val))

