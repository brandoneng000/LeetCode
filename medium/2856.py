from typing import List

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        first = nums[:n // 2]
        second = nums[n // 2:]
        res = n
        index1 = index2 = 0

        while index1 < len(first) and index2 < len(second):
            if first[index1] < second[index2]:
                res -= 2
                index1 += 1
            
            index2 += 1
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.minLengthAfterRemovals([1,1,4,4,5,5]))
    print(sol.minLengthAfterRemovals([1,2,3,4]))
    print(sol.minLengthAfterRemovals([1,1,2,2,3,3]))
    print(sol.minLengthAfterRemovals([1000000000,1000000000]))
    print(sol.minLengthAfterRemovals([2,3,4,4,4]))

if __name__ == '__main__':
    main()