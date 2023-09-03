# from typing from

# 1116 ~ 1136
class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        dirs = list(filter(lambda p: p != "", dirs))
        result = []
        for di in dirs:
            if di == ".":
                pass
            elif di == "..":
                if len(result) != 0:
                    result.pop()
            else:
                result.append(di)
        if len(result) == 0:
            return "/"
        result.insert(0, "")
        result_path = "/".join(result)
        return result_path


tcs = [
    '/home/',
    "/../",
    "/home/./foo/",
    "/home//foo/",
    "/a/./b/../../c/",
]

for tc in tcs:
    sol = Solution().simplifyPath(tc)
    print(sol)
