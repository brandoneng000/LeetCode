from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        dif = arr[1] - arr[0]

        for index in range(2, len(arr)):
            if arr[index] - arr[index - 1] != dif:
                return False
        
        return True

def main():
    sol = Solution()
    print(sol.canMakeArithmeticProgression([3,5,1]))
    print(sol.canMakeArithmeticProgression([1,2,4]))

if __name__ == '__main__':
    main()