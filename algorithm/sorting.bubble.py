def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(i, len(nums)):
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
    return nums


given = [5, 7, 8, 1, 4, 6, 9]
expected = [1, 4, 5, 6, 7, 8, 9]

output = bubbleSort(given)
assert output == expected
