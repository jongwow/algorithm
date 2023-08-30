from typing import List


def quickSort(arr: List[int], left: int, right: int):
    # 이때 right는 끝 인덱스 값.
    # 유효한지 확인 (left < right)
    # - 파티션함수 호출 (pivot을 반환. arr는 pivot 인덱스를 기준으로 크기 구분되어있을 것)
    # - left ~ pivot -1 까지 파티션 함수 호출
    # - pivot ~ right 까지 파티션 함수 호출
    # print(left, right)
    if left >= right:
        return
    pivot = partition(arr, left, right)
    # print('-: ', pivot)
    quickSort(arr, left, pivot-1)
    quickSort(arr, pivot, right)

    return


def partition(arr: List[int], start: int, end: int) -> int:
    pv = arr[start]
    left = start
    right = end
    while left <= right:
        while arr[left] < pv:
            left += 1
        while arr[right] > pv:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1
    return left


tcs = [
    [1, 7, 4, 8, 2, 6, 5], [1, 5, 3, 2], [1, 7, 4, 8, 10, 5]
    # [1, 7, 4, 8, 2, 6, 5], [5, 2, 3, 1], [3, 7, 4, 8, 10, 1]
]

for tc in tcs:
    # partition(tc, 0, len(tc)-1)
    # print(tc)
    quickSort(tc, 0, len(tc)-1)
    print(tc)
