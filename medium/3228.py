class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        res = 0
        ones = 0

        for i in range(n - 1):
            if s[i] == '1':
                ones += 1

                if s[i + 1] == '0':
                    res += ones
        
        return res

    # def maxOperations(self, s: str) -> int:
    #     n = len(s)
    #     res = 0
    #     count = 0
    #     i = 0

    #     while i < n:
    #         if s[i] == '1':
    #             count += 1
    #         else:
    #             res += count
    #             while i + 1 < n and s[i + 1] == '0':
    #                 i += 1
            
    #         i += 1
        
    #     return res


def main():
    sol = Solution()
    print(sol.maxOperations("1001101"))
    print(sol.maxOperations("00111"))

if __name__ == '__main__':
    main()