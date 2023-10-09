class Solution:
    def numSub(self, s: str) -> int:
        mod = 1000000007
        res = 0

        for bits in s.split('0'):
            res += (len(bits) * (len(bits) + 1) // 2)

        return res % mod

    # def numSub(self, s: str) -> int:
    #     mod = 1000000007
    #     n = len(s)
    #     ones = { 0: 0, 1: 1 }
    #     res = 0

    #     for i in range(2, n + 1):
    #         ones[i] = i + ones[i - 1]
        
    #     for bits in s.split('0'):
    #         res += ones[len(bits)]
        
    #     return res % mod


def main():
    sol = Solution()
    print(sol.numSub("0110111"))
    print(sol.numSub("101"))
    print(sol.numSub("111111"))

if __name__ == '__main__':
    main()