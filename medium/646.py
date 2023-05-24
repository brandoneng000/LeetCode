from typing import List

class Solution:
    # def findLongestChain(self, pairs: List[List[int]]) -> int:
    #     pairs.sort()
    #     dp = [1] * len(pairs)

    #     for i in range(len(pairs)):
    #         for j in range(i):
    #             if pairs[j][1] < pairs[i][0]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
        
    #     return max(dp)
    
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        current = -float('inf')
        res = 0
        for pair in pairs:
            if current < pair[0]:
                current = pair[1]
                res += 1
        
        return res


def main():
    sol = Solution()
    print(sol.findLongestChain([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]))
    print(sol.findLongestChain([[1,2],[2,3],[3,4]]))
    print(sol.findLongestChain([[1,2],[7,8],[4,5]]))

if __name__ == '__main__':
    main()