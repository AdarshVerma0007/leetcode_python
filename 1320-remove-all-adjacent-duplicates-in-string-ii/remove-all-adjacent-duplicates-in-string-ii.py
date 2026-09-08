class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        res = ""
        for c in s:
            if not st:
                st.append([c,1])
                continue
            if st[-1][0] != c:
                st.append([c,1])
                continue
            st[-1][1] += 1
            if st[-1][1]==k:
                st.pop()
        while st:
            char,num = st.pop()
            res = char * num + res
        return res
