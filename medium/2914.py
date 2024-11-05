
class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        res = 0
        
        for i in range(0, n - 1, 2):
            res += s[i] != s[i + 1]
        
        return res

    # def minChanges(self, s: str) -> int:
    #     n = len(s)
    #     res = 0

    #     if s.count('1') == n or s.count('1') == 0:
    #         return res
        
    #     i = 0
    #     j = i + 1

    #     while j < n:
    #         if s[i] != s[j]:
    #             res += 1
            
    #         i += 2
    #         j += 2
                
    #     return res
        
def main():
    sol = Solution()
    print(sol.minChanges("11000111"))
    print(sol.minChanges("1001"))
    print(sol.minChanges("10"))
    print(sol.minChanges("0000"))

if __name__ == '__main__':
    main()