from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        right = 0

        for index, num in enumerate(arr):
            right = max(right, num)
            if index == right:
                res += 1
        return res


def main():
    sol = Solution()
    print(sol.maxChunksToSorted([4,3,2,1,0]))
    print(sol.maxChunksToSorted([1,0,2,3,4]))

if __name__ == '__main__':
    main()