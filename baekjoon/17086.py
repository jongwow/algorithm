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


def boundary(yy, xx, y, x):
    if 0 <= x and x < xx and 0 <= y and y < yy:
        return True
    return False


def innerSolve(seaMap, N, M, cY, cX):
    X = 1
    Y = 0
    distMap = [[0 for j in range(M)] for i in range(N)]
    visitedMap = [[0 for j in range(M)] for i in range(N)]
    Q = []
    Q.append((cY, cX))
    result = 55
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
    return ret


if __name__ == "__main__":
    f = open("./17086.txt", 'r')
    N, M = map(int, f.readline().split())
    seaMap = []
    for _ in range(N):
        seaMap.append(list(map(int, f.readline().split())))
    ret = solve(seaMap, N, M)
    print(ret)
