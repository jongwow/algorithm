from typing import List


class Solution:
    def findKthLargest_v2(self, nums: List[int], k: int) -> int:
        self.quickSelect(nums, k, 0, len(nums)-1)
        return nums[-k]

    def findKthLargest_v1(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

    def quickSelect(self, nums: List[int], k: int, left: int, right: int) -> int:
        if left >= right:
            return
        pivot_index = self.partition(
            nums, left, right)  # 왼쪽엔 작은 값들을, 오른쪽엔 큰 값들을
        # 만약 pivot_index가 k보다 작으면?  -> 오른쪽만 살린다.
        # 만약 pivot_index가 k보다 크면? -> 왼쪽만 살린다
        r_k = len(nums) - k
        if r_k < pivot_index:
            self.quickSelect(nums, k, left, pivot_index-1)
        else:
            self.quickSelect(nums, k, pivot_index, right)

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[left]
        while left <= right:
            while nums[left] < pivot:
                left += 1
            while nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left


tcs = [
    [[3, 2, 1, 5, 6, 4], 2],
    [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4],
    [[7, 6, 5, 4, 3, 2, 1], 2]
]

for tc in tcs:
    so = Solution()
    print(so.findKthLargest_v1(tc[0], tc[1]))
    print(so.findKthLargest_v2(tc[0], tc[1]))
