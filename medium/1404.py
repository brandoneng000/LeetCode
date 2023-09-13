class Solution:
    def numSteps(self, s: str) -> int:
        carry = 0
        res = 0

        for index in range(len(s) - 1, 0, -1):
            if int(s[index]) + carry == 1:
                carry = 1
                res += 2
            else:
                res += 1
        
        return res + carry

    # def numSteps(self, s: str) -> int:
    #     res = 0
    #     num = int(s, 2)

    #     while num != 1:
    #         if num % 2:
    #             num += 1
    #         else:
    #             num //= 2
    #         res += 1
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.numSteps("1101"))
    print(sol.numSteps("10"))
    print(sol.numSteps("1"))

if __name__ == '__main__':
    main()