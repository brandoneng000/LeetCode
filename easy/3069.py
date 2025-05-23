from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        
        return arr1 + arr2
        
def main():
    sol = Solution()
    print(sol.resultArray([2,1,3]))
    print(sol.resultArray([5,4,3,8]))

if __name__ == '__main__':
    main()