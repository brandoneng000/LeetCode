class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            if s[i] != ('1' if i % 2 == 0 else '0'):
                res += 1
        
        return min(res, n - res)
            

    # def minOperations(self, s: str) -> int:
    #     res = 0
    #     temp = 0
    #     alternate = bool(int(s[0]))
    #     for bit in s:
    #         if alternate != int(bit):
    #             res += 1
    #         if not alternate != int(bit):
    #             temp += 1
    #         alternate = not alternate
        
    #     return min(temp, res)
        
        
def main():
    sol = Solution()
    print(sol.minOperations("0100"))
    print(sol.minOperations("10"))
    print(sol.minOperations("1111"))

if __name__ == '__main__':
    main()