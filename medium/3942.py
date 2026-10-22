from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        start = nums.index(0)
        asc = desc = True

        for i in range(1, n):
            val = nums[(start + i) % n]

            if val != i:
                asc = False
            if val != n - i:
                desc = False

            if not asc and not desc:
                return -1

        if asc:
            return min(start, n - start + 2)

        return min(n - start, start + 2)

def main():
    sol = Solution()
    print(sol.minOperations([0,2,1]))
    print(sol.minOperations([1,0,2]))
    print(sol.minOperations([2,0,1,3]))

if __name__ == '__main__':
    main()