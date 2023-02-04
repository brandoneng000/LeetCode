from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        increased = False
        decreased = False
        index = 0

        while index < len(arr) - 1 and arr[index] < arr[index + 1]:
            increased = True
            index += 1
        
        while index < len(arr) - 1 and arr[index] > arr[index + 1]:
            decreased = True
            index += 1

        return index == len(arr) - 1 and increased and decreased

def main():
    sol = Solution()
    print(sol.validMountainArray([2,1]))
    print(sol.validMountainArray([3,5,5]))
    print(sol.validMountainArray([0,3,2,1]))
    print(sol.validMountainArray([0,3,1]))

if __name__ == '__main__':
    main()