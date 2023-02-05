alphabets = "abcdefghijklmnopqrstuvwxyz@@@@"
def printMatrix(mat):
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            print(mat[y][x], end = ' ')
        print()

def getIndexOfChar(char):
    num = ord(char) - ord('a')
    col = num % 5
    row = int(num / 5)
    return (row, col)

def getPathTuple(startChar, endChar):
    sCharIndex = getIndexOfChar(startChar)
    eCharIndex = getIndexOfChar(endChar)
    diffIndex = (-sCharIndex[0]+eCharIndex[0], -sCharIndex[1]+eCharIndex[1])
    return diffIndex

def getPathStr(diffTuple):
    row, col = diffTuple

    path = ""
    # 우상 (-,+)
    if row < 0 and col > 0:
    # - 세로먼저.
        path += (-row)*"U"
        path += col*"R"
    # 좌하 (+,-)
    elif row > 0 and col < 0:
    # - 가로먼저.
        path += (-col)*"L"
        path += row*"D"
    # 우하 (+, +)
    elif row >= 0 and col >= 0:
    # - 상관없음.
        path += col*"R"
        path += row*"D"
    # 좌상
    elif row <= 0 and col <= 0:
    # - 상관없음.
        path += (-col)*"L"
        path += (-row)*"U"
    else:
        assert False
    # print(diffTuple, path)
    return path

def getPath(startChar, endChar):
    diffTuple = getPathTuple(startChar=startChar, endChar=endChar)
    return getPathStr(diffTuple) + "!"


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        alphabetBoard = [['@' for j in range(5)] for i in range(6)]
        aIndex = 0
        for y in range(6):
            for x in range(5):
                alphabetBoard[y][x] = alphabets[aIndex]
                aIndex+=1
        printMatrix(alphabetBoard)
        y = 0
        x = 0
        resultPath = ""
        startCh = alphabetBoard[y][x]
        for targetCh in target:
            path = getPath(startCh, targetCh)
            startCh = targetCh
            resultPath += path
        return resultPath

if __name__ == "__main__":
    target = "leet"
    output = Solution().alphabetBoardPath(target=target)
    print(output)