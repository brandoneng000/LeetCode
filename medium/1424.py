from typing import List
import collections

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # row - 1 and col + 1
        n = len(nums)
        res = []
        q = collections.deque([(0, 0)])

        while q:
            row, col = q.popleft()

            res.append(nums[row][col])

            if col == 0 and row + 1 < n:
                q.append((row + 1, col))

            if col + 1 < len(nums[row]):
                q.append((row, col + 1))

        return res


def main():
    sol = Solution()
    # print(sol.findDiagonalOrder([[1,2,3,4,5],[6,7],[8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],[9,10,11],[12,13,14,15,16]]))
    print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))

if __name__ == '__main__':
    main()