class Solution:
    def findComplement(self, num: int) -> int:
        cur = 1

        while cur <= num:
            cur *= 2

        return num ^ (cur - 1)

    # def findComplement(self, num: int) -> int:
    #     temp = num
    #     mask = 0
    #     while temp:
    #         temp //= 2
    #         mask = (mask << 1) + 1

    #     return num ^ mask

def main():
    sol = Solution()
    print(sol.findComplement(2))
    print(sol.findComplement(5))
    print(sol.findComplement(1))

if __name__ == '__main__':
    main()