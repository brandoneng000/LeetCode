from typing import List
from bisect import bisect_left

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        j = n - 1
        visited = set()

        for i in range(n // 2 - 1, -1, -1):
            if nums[i] * 2 <= nums[j] and j not in visited:
                visited.add(j)
                visited.add(i)
                res += 2
                j -= 1
            
        
        return res


        
def main():
    sol = Solution()
    print(sol.maxNumOfMarkedIndices(nums = [42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40]))
    print(sol.maxNumOfMarkedIndices(nums = [3,5,2,4]))
    print(sol.maxNumOfMarkedIndices(nums = [9,2,5,4]))
    print(sol.maxNumOfMarkedIndices(nums = [7,6,8]))

if __name__ == '__main__':
    main()