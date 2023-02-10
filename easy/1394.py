from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = 0

        for num in set(arr):
            if num == arr.count(num):
                result = max(result, num)

        return result if result else -1

def main():
    sol = Solution()
    print(sol.findLucky([2,2,3,4]))
    print(sol.findLucky([1,2,2,3,3,3]))
    print(sol.findLucky([2,2,2,3,3]))

if __name__ == '__main__':
    main()