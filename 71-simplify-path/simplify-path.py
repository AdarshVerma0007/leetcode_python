class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        path = path.split("/")
        for el in path:
            if stk and el =="..":
                stk.pop()
            elif el not in [".","",".."]:
                stk.append(el)

        return "/"+"/".join(stk)