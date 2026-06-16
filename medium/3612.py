class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for ch in s:
            if ch == '*':
                if res:
                    res.pop()
            elif ch == '#':
                res += res
            elif ch == '%':
                res.reverse()
            else:
                res.append(ch)
        
        return ''.join(res)
        
def main():
    sol = Solution()
    print(sol.processStr("a#b%*"))
    print(sol.processStr("z*#"))

if __name__ == '__main__':
    main()