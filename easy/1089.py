from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index = 0
        while index < len(arr):
            if arr[index] == 0:
                arr.insert(index + 1, 0)
                arr.pop()
                index += 1
            index += 1


def main():
    sol = Solution()
    arr = [1,0,2,3,0,4,5,0]
    sol.duplicateZeros(arr)
    print(arr)
    arr = [1,2,3]
    sol.duplicateZeros(arr)
    print(arr)


if __name__ == '__main__':
    main()