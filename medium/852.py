from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            middle = (left + right) // 2

            if arr[middle - 1] < arr[middle] > arr[middle + 1]:
                return middle
            elif arr[middle] < arr[middle + 1]:
                left = middle + 1
            else:
                right = middle - 1
        
        return left


def main():
    sol = Solution()
    print(sol.peakIndexInMountainArray([3,4,5,1]))
    print(sol.peakIndexInMountainArray([0,1,0]))
    print(sol.peakIndexInMountainArray([0,2,1,0]))
    print(sol.peakIndexInMountainArray([0,10,5,2]))

if __name__ == '__main__':
    main()