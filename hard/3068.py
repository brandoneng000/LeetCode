from typing import List
from collections import deque, defaultdict

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        delta = [(num ^ k) - num for num in nums]
        delta.sort(reverse=True)
        res = sum(nums)

        for i in range(0, n, 2):
            if i == n - 1:
                break

            path_delta = delta[i] + delta[i + 1]

            if path_delta > 0:
                res += path_delta
            else:
                break
        
        return res

        
def main():
    sol = Solution()
    print(sol.maximumValueSum(nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]))
    print(sol.maximumValueSum(nums = [2,3], k = 7, edges = [[0,1]]))
    print(sol.maximumValueSum(nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]))

if __name__ == '__main__':
    main()