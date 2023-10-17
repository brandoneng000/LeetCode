class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        close = 0

        for p in s:
            if p == '(':
                if close % 2 == 1:
                    res += 1
                    close -= 1
                close += 2
            else:
                close -= 1
                
                if close < 0:
                    res += 1
                    close += 2


        return res + close
        
def main():
    sol = Solution()
    print(sol.minInsertions("()()))))))"))
    print(sol.minInsertions("()()))))))(())(())())()())))))))))))(()()()())()))))))))))))))()(()()())"))
    print(sol.minInsertions("(()))"))
    print(sol.minInsertions("())"))
    print(sol.minInsertions("))())("))

if __name__ == '__main__':
    main()