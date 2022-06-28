class Solution:
    def numDecodings(self, s: str) -> int:
        cache = { len(s) : 1 }

        def dfs(i):
            if i in cache:
                return cache[i]
            
            if s[i] == "0":
                return 0

            # runs until all valid single digits are used
            res = dfs(i + 1)

            # runs to grab all double digits between 10-26
            # after grabbing first double then grabs all singles afterwards
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            cache[i] = res
            return res
        
        return dfs(0)
                

def main():
    sol = Solution()
    print(sol.numDecodings("12"))

if __name__ == '__main__':
    main()