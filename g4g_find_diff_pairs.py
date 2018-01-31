# -*- coding: utf-8; -*-


# Two-pass approach O(n)
def find_pair(nums, diff):
    pair = []
    visited = {}
    for i in nums:
        visited[i] = i + diff

    for i in nums:
        if i in visited and visited[i] in visited:
            pair = [i, visited[i]]
            break

    return pair


# Using `in` O(n^2)
def find_pair_slow(nums, diff):
    pair = []

    for i in nums:
        if i + diff in nums:
            pair = [i, i + diff]
            break
        elif i - diff in nums:
            pair = [i, i - diff]
            break

    return pair


if __name__ == '__main__':
    test_cases = [
        {
            'input': ([1, 2] + range(5, 10**5, 2), 1),
            'output': [1, 2],
        },
        {
            'input': ([5, 20, 3, 2, 50, 80], 78),
            'output': [2, 80],
        },
        {
            'input': ([90, 70, 20, 80, 50], 45),
            'output': [],
        },
        {
            'input': ([1, 8, 30, 40, 100], 60),
            'output': [40, 100],
        },
    ]
    for test_case in test_cases:
        actual = find_pair(test_case['input'][0], test_case['input'][1])
        try:
            assert test_case['output'] == actual
            print "Test case passed: input=%s output=%s, expected:%s" % (test_case['input'], actual, test_case['output'])
        except AssertionError as e:
            print('Failed to assert that:\n  Expected: %s\n  Actual:   %s\n[%s]' % (test_case['output'], actual, test_case['input']))
