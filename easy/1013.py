from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3:
            return False
        
        left, right = 1, len(arr) - 2
        average = sum(arr) // 3
        left_sum, right_sum = arr[0], arr[-1]

        while left <= right:
            if left < right and left_sum != average:
                left_sum += arr[left]
                left += 1
            if left < right and right_sum != average:
                right_sum += arr[right]
                right -= 1
            if left_sum == average == right_sum:
                return True
            if left == right:
                return False
        
        return False
        



def main():
    sol = Solution()
    print(sol.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
    print(sol.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
    print(sol.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
    print(sol.canThreePartsEqualSum([4,5,6,7]))

if __name__ == '__main__':
    main()