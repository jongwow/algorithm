from typing import List


def binarySearch(numbers: List[int], target: int) -> int:
    # 만약 없다면 len(numbers) 반환
    start = 0
    end = len(numbers)
    while start < end:
        p = (start + end) // 2
        if numbers[p] == target:
            return p
        if numbers[p] < target:
            start = p+1
        else:
            end = p
    pass


def binarySearch2(numbers: List[int], target: int) -> int:
    start = 0
    end = len(numbers) - 1
    while end - start >= 0:
        mid = (start+end)//2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


given = [1, 3, 5, 7, 8, 9]

targets = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]
for target in targets:
    output = binarySearch2(given, target)
    print(output)
expected = 1
