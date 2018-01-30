def find_max(nums):
    curr_max = 0

    if len(nums) == 2:
        return max(nums[0], nums[1])

    start = 0
    end = len(nums) - 1
    pivot = (start + end) / 2

    while start <= pivot <= end:
        # print (start, end, pivot, nums[start:end + 1])
        curr_max = max(curr_max, nums[pivot])

        if pivot - 1 < start or pivot + 1 > end:
            break
        prev_val = nums[pivot - 1]
        next_val = nums[pivot + 1]
        if prev_val > nums[pivot]:
            # move to the left
            end = pivot
            pivot = pivot - ((pivot - start) / 2)
        elif next_val > nums[pivot]:
            # move to the right
            start = pivot
            pivot = pivot + ((end - pivot) / 2)
        else:
            break

    return curr_max


if __name__ == '__main__':
    test_cases = [
        {
            'input': [1, 2, 3],
            'output': 2,
        },
        {
            'input': [3, 2, 1],
            'output': 2,
        },
        {
            'input': [1, 3, 5, 4, 2],
            'output': 5,
        },
        {
            'input': [1, 3, 5, 4],
            'output': 5,
        },
        {
            'input': [1, 2, 4, 5, 7, 3, 1],
            'output': 7,
        },
        {
            'input': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            'output': 100,
        },
        {
            'input': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100, 9, 8, 7, 6, 5, 4, 3, 2, 0],
            'output': 100,
        },
        {
            'input': [],
            'output': 0,
        },
        {
            'input': [1, 2],
            'output': 2,
        },
        {
            'input': [2, 1],
            'output': 2,
        },
    ]
    for test_case in test_cases:
        actual = find_max(test_case['input'])
        try:
            assert test_case['output'] == actual
            print "Test case passed: input=%s output=%s, expected:%s" % (test_case['input'], actual, test_case['output'])
        except AssertionError as e:
            print('Failed to assert that:\n  Expected: %s\n  Actual:   %s\n[%s]' % (test_case['output'], actual, test_case['input']))
