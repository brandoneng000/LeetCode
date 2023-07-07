from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, 0
        res = 1

        while right < n:
            while left < n - 1 and arr[left] == arr[left + 1]:
                left += 1
            while right < n - 1 and (arr[right - 1] > arr[right] < arr[right + 1] or arr[right - 1] < arr[right] > arr[right + 1]):
                right += 1
            res = max(res, right - left + 1)
            left = right
            right += 1
        
        return res
        

def main():
    sol = Solution()
    print(sol.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
    print(sol.maxTurbulenceSize([4,8,12,16]))
    print(sol.maxTurbulenceSize([100]))

if __name__ == '__main__':
    main()