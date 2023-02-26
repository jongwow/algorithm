from typing import List


def quickSort(arr):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)

        sort(low, mid-1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
        return low
    return sort(0, len(arr)-1)


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # 오름차순 정렬
        quickSort(arr)
        arr[0] = 1
        # 순회하면서
        for i in range(1, len(arr)):
            prevV = arr[i-1]
            v = arr[i]
            # - 이전값과 현재값을 비교해서
            if abs(prevV - v) <= 1:
                continue
            else:  # 예외의 경우엔 이전의 값 + 1
                arr[i] = prevV + 1
        return arr[len(arr)-1]


if __name__ == "__main__":
    cases = [
        [2, 2, 1, 2, 1],  # 2
        [100, 1, 1000],  # 3
        [73, 98, 9],  # 3
        [1, 2, 3, 4, 5],  # 5
        [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],  # 5
        [11111],  # 1
    ]
    for ca in cases:
        output = Solution().maximumElementAfterDecrementingAndRearranging(ca)
        print(output)
