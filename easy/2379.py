class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        left = 0
        num_whites = 0
        res = float('inf')

        for right in range(n):
            if blocks[right] == 'W':
                num_whites += 1
            
            if right - left + 1 == k:
                res = min(res, num_whites)
            
                if blocks[left] == 'W':
                    num_whites -= 1
                
                left += 1
        
        return res


    # def minimumRecolors(self, blocks: str, k: int) -> int:
    #     res = 1000
        
    #     for index in range(len(blocks) - k + 1):
    #         res = min(res, blocks[index: index + k].count('W'))

    #     return res

        # return min(blocks[index: index + k].count('W') for index in range(len(blocks) - k + 1))

        

def main():
    sol = Solution()
    print(sol.minimumRecolors(blocks = "WBBWWBBWBW", k = 7))
    print(sol.minimumRecolors(blocks = "WBWBBBW", k = 2))
    print(sol.minimumRecolors(blocks = "WBWWWWWBWWWWWBWWWBW", k = 2))

if __name__ == '__main__':
    main()