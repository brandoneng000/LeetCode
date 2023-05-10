from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = []
        start_index = []
        cache = {}
        for index, (start, end) in enumerate(intervals):
            start_index.append(start)
            cache[start] = index
        
        start_index.sort()
        for start, end in intervals:
            location = self.binary_search(start_index, end)
            if location < len(start_index):
                res.append(cache.get(start_index[location], -1))
            else:
                res.append(-1)
        
        return res
    
    def binary_search(self, arr: List[int], target: int):
        left, right = 0, len(arr) - 1

        while left <= right:
            middle = (left + right) // 2
            if arr[middle] == target:
                return middle
            elif arr[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return left

def main():
    sol = Solution()
    print(sol.findRightInterval([[1,2]]))
    print(sol.findRightInterval([[3,4],[2,3],[1,2]]))
    print(sol.findRightInterval([[1,4],[2,3],[3,4]]))

if __name__ == '__main__':
    main()