from typing import List
import bisect

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        dp = {}

        def helper(index: int, prev: int):
            if index == len(arr1):
                return 0
            if (index, prev) in dp:
                return dp[(index, prev)]
            
            cost = float('inf')
            if arr1[index] > prev:
                cost = helper(index + 1, arr1[index])

            index_2 = bisect.bisect(arr2, prev)

            if index_2 < len(arr2):
                cost = min(cost, 1 + helper(index + 1, arr2[index_2]))
            
            dp[(index, prev)] = cost
            
            return cost
        
        res = helper(0, -1)
        return res if res != float('inf') else -1

        

def main():
    sol = Solution()
    print(sol.makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]))
    print(sol.makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [4,3,1]))
    print(sol.makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]))

if __name__ == '__main__':
    main()