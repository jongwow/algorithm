# data = list(map(int, input().split()))
def printMatrix(mat):
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            print(mat[y][x], end = ' ')
        print()
def rotate(list_2d):
    n = len(list_2d) # 행 길이 계산
    m = len(list_2d[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = list_2d[i][j]
    return new

def rotate2(original):
    return [[row[i] for row in original[::-1]] for i in range(len(original[0]))]
def isAttachable(big, small, sY, sX):
    # 크기 먼저 비교
    stickerWidth = len(small[0])
    stickerHeight = len(small)
    laptopWidth =len(big[0])
    laptopHeight =  len(big)
    if sY + stickerHeight > laptopHeight:
        return False
    if sX + stickerWidth > laptopWidth:
        return False
    # return True
    for y in range(stickerHeight):
        for x in range(stickerWidth):
            if small[y][x] == 1:
                if big[sY+y][sX+x] == 0:
                    continue
                else:
                    return False
            else:
                continue    
    return True
    
def attachSticker(big, small, sY, sX):
    stickerWidth = len(small[0])
    stickerHeight = len(small)
    cnt = 0
    for y in range(stickerHeight):
        for x in range(stickerWidth):
            if small[y][x] == 1:
                cnt += 1
                big[sY+y][sX+x] = 1
    return cnt

def solve(n, m, stickers):
    laptop = [[0 for j in range(m)] for i in range(n)]
    result = 0
    for sticker in stickers:
        st1 = rotate(sticker)
        st2 = rotate(st1)
        st3 = rotate(st2)
        attached = False
        for sts in [sticker, st1, st2, st3]:
            for y in range(n):
                for x in range(m):
                    if isAttachable(laptop, sts, y, x):
                        result += attachSticker(laptop, sts, y, x)
                        attached = True
                        break
                if attached:
                    break
            if attached:
                break
    printMatrix(laptop)
    print()
    return result

if __name__ == "__main__":
    f = open("./18808.txt", 'r')
    N, M, K = map(int, f.readline().split())
    stickers = []
    for _ in range(K):
        x, y = map(int, f.readline().split())
        stickers.append([list(map(int, f.readline().split())) for _ in range(x)])
    f.close()
    result = solve(N, M, stickers)
    print(result)


# n,m,k = map(int, sys.stdin.readline().split())
# sts = []
# for _ in range(k):
#     x, y = map(int, sys.stdin.readline().split())
#     sts.append([list(map(int, sys.stdin.readline().split())) for _ in range(x)])
# result = solve(n,m,sts)
# print(result)