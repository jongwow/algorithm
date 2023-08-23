from typing import List
import math


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # print(numbers[sol2[0]-1], numbers[sol2[1]-1])
        # [24, 30]
        return self.twoSumTwoPointer(numbers, target)

    def twoSumTwoPointer(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            cur = numbers[left] + numbers[right]
            if cur == target:
                return [left+1, right+1]
            if cur > target:
                right -= 1  # 조금씩가기위해 더 큰 값
            else:  # cur < target
                left += 1
                continue
        return [-1, -1]

    def twoSumTwoPointerWrong2(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        cnt = 0
        while left < right and cnt < 100:
            cnt += 1
            cur = numbers[left] + numbers[right]
            print('(', left, ',', right, ') = (',
                  numbers[left], numbers[right], ')')
            if cur == target:
                return [left+1, right+1]
            if cur > target:
                if left-1 < 0:
                    print('case3')
                    right -= 1
                    continue
                case1 = numbers[left-1] + numbers[right]
                case3 = numbers[left] + numbers[right-1]
                # case1 < case3 < target < cur: case1 선택 <- 이경우가 있을까? 없을 것 같다. 배제한다.
                # case3 < case1 < target < cur: case3 선택 <- 이경우가 있을까? 없을 것 같다. 배제한다.

                # case1 < target < case3 < cur: case3 선택
                # case3 < target < case1 < cur: case1 선택
                # target < case1 < case3 < cur: case1 선택
                # target < case3 < case1 < cur: case3 선택
                if abs(case1 - target) < abs(case3 - target):
                    print('case3')
                    right -= 1  # 조금씩가기위해 더 큰 값
                    continue
                else:
                    print('case1')
                    left -= 1
                    continue
            else:  # cur < target
                if right + 1 >= len(numbers):
                    print('case2')
                    left += 1
                    continue
                case2 = numbers[left+1]+numbers[right]
                case4 = numbers[left]+numbers[right+1]
                if abs(case2 - target) < abs(case4 - target):
                    print('case4')
                    right += 1
                    continue
                else:
                    print('case2')
                    left += 1
                    continue
        return [-1, -1]

    def twoSumTwoPointerWrong(self, numbers: List[int], target: int) -> List[int]:
        idx = 0
        num_size = len(numbers)
        while idx < num_size:
            numbers[idx] = numbers[idx] - target
            idx += 1
        left = 0
        right = num_size - 1
        opt = -math.inf
        while left < right and left >= 0 and right < num_size:
            current_bar = abs(numbers[left] + numbers[right] - target)
            if current_bar < abs(opt):
                opt = numbers[left] + numbers[right] - target
            if current_bar == 0:
                return [left + 1, right + 1]
            next_bar_left = abs(numbers[left+1] + numbers[right] - target)
            next_bar_right = abs(numbers[left] + numbers[right-1] - target)
            if current_bar > next_bar_left or current_bar > next_bar_right:
                if next_bar_right <= next_bar_left:
                    right -= 1
                else:
                    left += 1
            else:
                left += 1
                right -= 1
        print(opt)
        print(left, right)
        return [-1, -1]

    def twoSumBinary(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        while left < len(numbers)-1:
            subject = target - numbers[left]
            start = left + 1
            end = len(numbers) - 1
            while end - start >= 0:
                mid = (start+end)//2
                if numbers[mid] == subject:
                    return [left+1, mid+1]
                elif numbers[mid] > subject:
                    end = mid - 1
                else:
                    start = mid+1
            left += 1
        return [-1, -1]

    def twoSumBinaryCompression(self, numbers: List[int], target: int) -> List[int]:
        new_num = []
        new_num.append(0)
        new_num.append(1)
        idx = 2
        while idx < len(numbers):
            if numbers[idx] != numbers[idx-2]:
                new_num.append(idx)
            idx += 1
        left = 0
        while left < len(new_num)-1:
            subject = target - numbers[new_num[left]]
            start = left + 1
            end = len(new_num) - 1
            while end - start >= 0:
                mid = (start+end)//2
                if numbers[new_num[mid]] == subject:
                    return [new_num[left]+1, new_num[mid]+1]
                elif numbers[new_num[mid]] > subject:
                    end = mid - 1
                else:
                    start = mid+1
            left += 1
        return [-1, -1]

    def twoSumBruteForce(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        while left < len(numbers) - 1:
            right = left + 1
            while right < len(numbers):
                su = numbers[left] + numbers[right]
                if su == target:
                    return [left+1, right+1]
                right += 1
            left += 1
        return [0, 1]


tcs = [
    # [[2, 7, 11, 15], 9, [1, 2]],
    # [[2, 3, 4], 6, [1, 3]],
    # [[-1, 0], -1, [1, 2]],
    # [[5, 25, 75], 100, [2, 3]],
    [
        [
            12, 13, 23, 28, 43,
            44, 59, 60, 61, 68,
            70, 86, 88, 92, 124,
            125, 136, 168, 173, 173,
            180, 199, 212, 221, 227,
            230, 277, 282, 306, 314,
            316, 321, 325, 328, 336,
            337, 363, 365, 368, 370,
            370, 371, 375, 384, 387,
            394, 400, 404, 414, 422,
            422, 427, 430, 435, 457,
            493, 506, 527, 531, 538,
            541, 546, 568, 583, 585,
            587, 650, 652, 677, 691,
            730, 737, 740, 751, 755,
            764, 778, 783, 785, 789,
            794, 803, 809, 815, 847,
            858, 863, 863, 874, 887,
            896, 916, 920, 926, 927,
            930, 933, 957, 981, 997
        ], 542, [24, 32]],
    [[3, 3, 5, 8, 18, 21, 22, 22, 22, 24, 26, 28, 29, 31, 31, 34, 37, 37, 40, 43, 43, 43, 44, 47, 48, 51, 51, 51, 52, 54, 55, 56, 59, 59, 60, 74, 74, 76, 76, 81, 82, 82, 82, 85, 89, 91, 91, 94, 99, 101, 101, 106, 116, 118, 121, 126, 127, 128, 128, 128, 131, 134, 135, 138, 140, 143, 145, 151, 152, 153, 154, 156, 158, 158, 158, 160, 169, 173, 174, 177, 178, 180, 189, 190, 190, 191, 191, 196, 197, 203, 203, 206, 206, 206, 208, 210, 212, 215, 216, 218, 218, 219, 223, 225, 227, 229, 232, 232, 233, 234, 235, 235, 236, 237, 238, 239, 245, 249, 250, 251, 254, 254, 256, 260, 261, 262, 270, 271, 271, 274, 275, 284, 285, 286, 290, 290, 291, 292, 292, 293, 293, 293, 295, 299, 300, 304, 304, 305, 310, 313, 313, 315, 322, 326, 327, 329, 334, 336, 337, 339, 339, 340, 341, 343, 344, 347, 347, 356, 356, 359, 359, 361, 364, 364, 368, 368, 369, 376, 378, 380, 380, 380, 386, 387, 389, 391, 391, 397, 399, 404, 405, 413, 415, 418, 418, 423, 426, 428, 429, 430, 432, 434, 437, 439, 459, 460, 461, 461, 463, 472, 479, 480, 484, 484, 486, 487, 492, 494, 498, 499, 500, 501, 501, 504, 505, 505, 507, 513, 517,
        517, 519, 519, 522, 525, 525, 529, 530, 530, 533, 536, 537, 538, 539, 542, 544, 553, 557, 561, 561, 564, 567, 568, 568, 570, 570, 572, 574, 575, 575, 579, 580, 581, 582, 590, 591, 594, 594, 597, 600, 605, 607, 608, 611, 614, 615, 615, 619, 621, 622, 623, 626, 627, 628, 630, 631, 632, 634, 638, 640, 641, 642, 648, 648, 649, 659, 662, 668, 673, 678, 678, 682, 682, 683, 683, 686, 686, 687, 691, 692, 693, 698, 700, 700, 706, 711, 711, 712, 714, 714, 718, 722, 727, 730, 730, 733, 733, 741, 744, 745, 747, 749, 754, 755, 755, 758, 760, 762, 763, 764, 769, 770, 771, 771, 776, 777, 784, 785, 789, 790, 792, 795, 795, 796, 797, 798, 806, 806, 806, 809, 812, 813, 815, 819, 820, 823, 827, 830, 837, 840, 843, 848, 850, 851, 851, 852, 857, 858, 858, 859, 861, 863, 866, 869, 869, 873, 874, 874, 883, 885, 887, 889, 891, 893, 899, 901, 903, 905, 905, 905, 909, 912, 917, 919, 920, 921, 922, 926, 935, 940, 941, 944, 945, 946, 947, 948, 950, 950, 951, 952, 956, 956, 959, 962, 964, 965, 968, 970, 971, 971, 972, 973, 976, 978, 982, 983, 985, 985, 988, 989, 991, 994, 994, 995, 995, 997, 997], 101, [99, 99]]
]

for tc in tcs:
    sol = Solution().twoSum(tc[0], tc[1])
    print(sol == tc[2])
    if sol != tc[2]:
        print(sol)
