# 2
# 5
# 둘 중 어느게 큰지

# for i in range(2, 10):
#     n = i
#     cnt_2 = 0
#     while n % 2 == 0:
#         cnt_2 += 1
#         n = n // 2
#     n = i
#     cnt_5 = 0
#     while n % 5 == 0:
#         cnt_5 += 1
#         n = n // 5
#     print(cnt_2 >= cnt_5, cnt_2, cnt_5)

def trailingZeroesV2(n: int) -> int:
    if n == 0:
        return 0
    c_2 = 0
    c_5 = 0
    while n >= 1:
        nn = n
        while nn >= 1:
            if nn % 2 != 0:
                break
            c_2 += 1
            nn = nn // 2
        nn = n
        while nn >= 1:
            if nn % 5 != 0:
                break
            c_5 += 1
            nn = nn // 5
        n -= 1
    if c_2 < c_5:
        print('HERE:', n)
    return min(c_2, c_5)


for i in range(1, 100):
    trailingZeroesV2(i)
