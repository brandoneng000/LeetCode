class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)

        for i in range(len(s)):
            # check if current character is '?'
            if s[i] == '?':
                for c in 'abc':
                    # check if it is the first char in string, if not check if the char is different from previous one
                    # then check if it is the last char, if not check if the char is different from next one
                    # if char is different then both change '?' into char
                    if (i == 0 or s[i - 1] != c) and (i + 1 == len(s) or s[i + 1] != c):
                        s[i] = c
                        break
        
        return "".join(s)
        
def main():
    sol = Solution()
    print(sol.modifyString("?zs"))
    print(sol.modifyString("ubv?w"))
    print(sol.modifyString("a?a"))
    print(sol.modifyString("j?qg??b"))

if __name__ == '__main__':
    main()