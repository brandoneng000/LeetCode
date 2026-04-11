from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10 ** 33
        indexes = defaultdict(list)
        res = INF

        for i in range(n):
            indexes[nums[i]].append(i)
        
        for num in indexes:
            if len(indexes[num]) >= 3:
                for i in range(len(indexes[num]) - 2):
                    x = indexes[num][i]
                    y = indexes[num][i + 1]
                    z = indexes[num][i + 2]

                    res = min(res, abs(abs(x - y) + abs(y - z) + abs(z - x)))

        return res if res != INF else -1
        
def main():
    sol = Solution()
    print(sol.minimumDistance(nums = [1,2,1,1,3]))
    print(sol.minimumDistance(nums = [1,1,2,3,2,1,2]))
    print(sol.minimumDistance(nums = [1]))

if __name__ == '__main__':
    main()