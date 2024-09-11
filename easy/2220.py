class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()

    # def minBitFlips(self, start: int, goal: int) -> int:
    #     return bin(start ^ goal).count('1')
        
    # def minBitFlips(self, start: int, goal: int) -> int:
    #     res = 0
        
    #     while start or goal:
    #         if start & 1 != goal & 1:
    #             res += 1
    #         start >>= 1
    #         goal >>= 1
        
    #     return res


def main():
    sol = Solution()
    print(sol.minBitFlips(10, 7))
    print(sol.minBitFlips(3, 4))

if __name__ == '__main__':
    main()