class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def helper(s: str):
            n = len(s)
            res = []

            for i in range(n - 1):
                res.append(str((int(s[i]) + int(s[i + 1])) % 10))
            
            return ''.join(res)
        
        while len(s) > 2:
            s = helper(s)
        
        return s[0] == s[1]

        
def main():
    sol = Solution()
    print(sol.hasSameDigits("3902"))
    print(sol.hasSameDigits("34789"))

if __name__ == '__main__':
    main()