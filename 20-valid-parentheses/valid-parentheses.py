class Solution:
    def isValid(self, s: str) -> bool:
        st= []
        for i in range(len(s)):
            if (s[i]=='(' or s[i]=='{' or s[i] =='['):
                st.append(s[i])
            elif s[i] == ')':
                if not st or st[-1] != '(':
                    return False
                st.pop()
            elif s[i] == '}':
                if not st or st[-1] != '{':
                    return False
                st.pop()
            elif s[i] == ']':
                if not st or st[-1] != '[':
                    return False
                st.pop()
        return not st