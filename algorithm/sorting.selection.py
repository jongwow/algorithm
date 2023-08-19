
def selectionSort(nums):
    for i in range(len(nums)-1):
        minIndex = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums


given = [5, 7, 8, 1, 4, 6, 9]
expected = [1, 4, 5, 6, 7, 8, 9]

output = selectionSort(given)
assert output == expected
