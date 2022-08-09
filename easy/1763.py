class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        res = ""
        
        for j in range(len(s)):
            for i in range(j):
                substring = s[i : j + 1]
                if set(substring) == set(substring.swapcase()):
                    res = max(res, substring, key=len)

        return res

        

def main():
    sol = Solution()
    print(sol.longestNiceSubstring("YazaAay"))
    print(sol.longestNiceSubstring("Bb"))
    print(sol.longestNiceSubstring("c"))

if __name__ == '__main__':
    main()