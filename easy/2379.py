class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 1000
        
        for index in range(len(blocks) - k + 1):
            res = min(res, blocks[index: index + k].count('W'))

        return res

        # return min(blocks[index: index + k].count('W') for index in range(len(blocks) - k + 1))

        

def main():
    sol = Solution()
    print(sol.minimumRecolors(blocks = "WBBWWBBWBW", k = 7))
    print(sol.minimumRecolors(blocks = "WBWBBBW", k = 2))
    print(sol.minimumRecolors(blocks = "WBWWWWWBWWWWWBWWWBW", k = 2))

if __name__ == '__main__':
    main()