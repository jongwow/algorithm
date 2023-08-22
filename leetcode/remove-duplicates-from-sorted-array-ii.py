from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l, r 포인터 존재
        # l 은 진실
        # r 은 순회용
        # r의 순회로 훑으면서 진짜로 넣어도 되는 애들만(최대2개만) l의 자리에 넣어주면서 l을 증가시키기

        # while r 이 끝에 다다를때까지.
        # - nums[r] 가 이전과 다르면 cnt = 1, cur = nums[r]
        # - nums[r] 이 이전과 같으면
        # - - cnt += 1,
        # - - - cnt > 2: r += 1, continue (left는 움직이지 않음. 이게 포인트)
        # (이전과다르면 바로 넣어주고, 이전과같아도 cnt 조건으로 위에서 걸림)
        # nums[r] = nums[l]
        # l += 1, r +=1 함

        if len(nums) == 1:  # Base case
            return 1
        left = 0
        right = 0
        current = None
        cnt = 1
        while right < len(nums):
            if nums[right] != current:
                cnt = 0
                current = nums[right]
            cnt += 1
            if cnt > 2:
                right += 1
                continue
            nums[left] = nums[right]
            left += 1
            right += 1
        return left  # left는 0-index 값, 반환값은 길이라서 +1 필요.


tcs = [
    # [1, 1, 1, 2, 2, 3],  # 5 [1,1,2,2,3,_]
    # [0, 0, 1, 1, 1, 1, 2, 3, 3],  # 7 [0,0,1,1,2,3,3,_,_]
    [1, 1]
]
for tc in tcs:
    sol = Solution().removeDuplicates(tc)
    print(sol)
