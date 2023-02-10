from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # Return the number of values in arr1 that fulfill |arr1[i]-arr2[j]| <= d where j is all arr2[j] is all vals in arr2
        result = 0

        for num in arr1:
            index = 0
            while(index < len(arr2) and abs(num - arr2[index]) > d):
                index += 1
            if index == len(arr2):
                result += 1
        
        return result

def main():
    sol = Solution()
    print(sol.findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))
    print(sol.findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3))
    print(sol.findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))

if __name__ == '__main__':
    main()