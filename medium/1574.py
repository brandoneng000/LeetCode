from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        arr = [0] + arr + [float('inf')]

        left = 0
        right = len(arr) - 1
        res = len(arr) - 1

        while left < len(arr) - 2 and arr[left] <= arr[left + 1]:
            left += 1

        while left >= 0:
            while right - 1 > left and arr[right - 1] >= arr[left] and arr[right] >= arr[right - 1]:
                right -= 1
            res = min(res, right - left - 1)
            left -= 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))
    print(sol.findLengthOfShortestSubarray([5,4,3,2,1]))
    print(sol.findLengthOfShortestSubarray([1,2,3]))

if __name__ == '__main__':
    main()