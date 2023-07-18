from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        left = n

        while left >= 0 and arr[left] >= arr[left - 1]:
            left -= 1
        
        if left <= 0:
            return arr
        
        k = left - 1
        right = n
        while right >= left:
            if arr[right] < arr[k] and arr[right] != arr[right - 1]:
                arr[k], arr[right] = arr[right], arr[k]
                return arr
            
            right -= 1
        
        return arr


def main():
    sol = Solution()
    print(sol.prevPermOpt1([3,1,1,3]))
    print(sol.prevPermOpt1([3,2,1]))
    print(sol.prevPermOpt1([1,1,5]))
    print(sol.prevPermOpt1([1,9,4,6,7]))

if __name__ == '__main__':
    main()