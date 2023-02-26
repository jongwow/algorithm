# 아기 상어가 있는 좌표들
# inf 로 이뤄진 2차원 배열,dist 선언
# 아기상어들 순회하면서
# - bfs로 seaMap이 0인 애들에 대해서 거리 설정
# - dist[y][x] = min(dist[y][x], currentDist)
# 2차원 배열 모두 순회하면서
# - 가장 값이 큰 값을 반환

import math


dirs = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def solvev1(seaMap, N, M):

    sharks = []
    for y in range(N):
        for x in range(M):
            if seaMap[y][x] == 1:
                sharks.append((y, x))
    distMaps = []
    while len(sharks) != 0:
        shark = sharks.pop(0)
        visitedMap = [[0 for j in range(M)] for i in range(N)]
        distMap = [[0 for j in range(M)] for i in range(N)]
        Q = []
        Q.append(shark)
        while len(Q) != 0:
            posY, posX = Q.pop(0)
            # print(posY, posX)
            for dir in dirs:
                nY = posY + dir[0]
                nX = posX + dir[1]
                if boundary(N, M, nY, nX) and visitedMap[nY][nX] == 0 and seaMap[nY][nX] == 0:
                    visitedMap[nY][nX] = 1
                    distMap[nY][nX] = distMap[posY][posX] + 1
                    # print('nY, nX', nY, nX, ': ', distMap[nY][nX])
                    Q.append((nY, nX))
        distMaps.append(distMap)
        # print(distMap)

    ret = math.inf
    for y in range(N):
        for x in range(M):
            for i in range(len(distMaps)):
                if seaMap[y][x] != 1:
                    ret = min(distMaps[i][y][x], ret)
    return ret


X = 1
Y = 0


def printMap(da):
    for y in da:
        print(y)


def solvev2(seaMap, N, M, cY, cX):
    distMap = [[0 for j in range(M)] for i in range(N)]
    visitedMap = [[0 for j in range(M)] for i in range(N)]
    Q = []
    Q.append((cY, cX))
    result = math.inf
    while len(Q) != 0:
        pos = Q.pop(0)
        for dir in dirs:
            nY = pos[Y] + dir[Y]
            nX = pos[X] + dir[X]
            if boundary(N, M, nY, nX) and visitedMap[nY][nX] == 0:
                print(nY, nX)
                visitedMap[nY][nX] = 1
                distMap[nY][nX] = distMap[pos[Y]][pos[X]] + 1
                Q.append((nY, nX))
                if seaMap[nY][nX] == 1:
                    if result > distMap[nY][nX]:
                        result = distMap[nY][nX]
            if boundary(N, M, nY, nX) and visitedMap[nY][nX] != 0:
                print('---', nY, nX)
    printMap(distMap)
    return result


def innerSolve(seaMap, N, M, cY, cX):
    distMap = [[0 for j in range(M)] for i in range(N)]
    visitedMap = [[0 for j in range(M)] for i in range(N)]
    Q = []
    Q.append((cY, cX))
    result = math.inf
    while len(Q) != 0:
        pos = Q.pop(0)
        if seaMap[pos[Y]][pos[X]] == 1:
            return distMap[pos[Y]][pos[X]]
        for dir in dirs:
            nY = pos[Y] + dir[Y]
            nX = pos[X] + dir[X]
            if boundary(N, M, nY, nX) and visitedMap[nY][nX] == 0:
                visitedMap[nY][nX] = 1
                distMap[nY][nX] = distMap[pos[Y]][pos[X]] + 1
                Q.append((nY, nX))
    return result


def solve(seaMap, N, M):
    distMap = [[0 for j in range(M)] for i in range(N)]
    ret = 0
    for y in range(N):
        for x in range(M):
            c = innerSolve(seaMap, N, M, y, x)
            if c > ret:
                ret = c
            distMap[y][x] = c
    # printMap(distMap)
    return ret


def boundary(yy, xx, y, x):
    if 0 <= x and x < xx and 0 <= y and y < yy:
        return True
    return False


if __name__ == "__main__":
    f = open("./17086.txt", 'r')
    N, M = map(int, f.readline().split())
    seaMap = []
    for _ in range(N):
        seaMap.append(list(map(int, f.readline().split())))
    ret = solve(seaMap, N, M)
    print(ret)
