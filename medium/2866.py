from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        prefix = [0] * n
        stack = [-1]
        cur = 0
        res = 0

        for i in range(n):
            while len(stack) > 1 and maxHeights[stack[-1]] > maxHeights[i]:
                j = stack.pop()
                cur -= (j - stack[-1]) * maxHeights[j]
            
            cur += (i - stack[-1]) * maxHeights[i]
            stack.append(i)
            prefix[i] = cur

        stack = [n]
        cur = 0

        for i in range(n - 1, -1, -1):
            while len(stack) > 1 and maxHeights[stack[-1]] > maxHeights[i]:
                j = stack.pop()
                cur -= -(j - stack[-1]) * maxHeights[j]
            
            cur += -(i - stack[-1]) * maxHeights[i]
            stack.append(i)
            res = max(res, prefix[i] + cur - maxHeights[i])
        
        return res

        
def main():
    sol = Solution()
    print(sol.maximumSumOfHeights([5,3,4,1,1]))
    print(sol.maximumSumOfHeights([6,5,3,9,2,7]))
    print(sol.maximumSumOfHeights([3,2,5,5,2,3]))

if __name__ == '__main__':
    main()