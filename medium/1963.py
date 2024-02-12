class Solution:
    def minSwaps(self, s: str) -> int:
        open_bracket = close_bracket = 0
        res = 0

        for b in s:
            if b == '[':
                open_bracket += 1
            else:
                close_bracket += 1
            
            if close_bracket > open_bracket:
                res += 1
                close_bracket -= 1
                open_bracket += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.minSwaps("][]["))
    print(sol.minSwaps("]]][[["))
    print(sol.minSwaps("[]"))

if __name__ == '__main__':
    main()