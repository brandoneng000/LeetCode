from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise  = hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare


def main():
    sol = Solution()
    print(sol.findDuplicate([1,2,3,3]))
    print(sol.findDuplicate([1,3,4,2,2]))
    print(sol.findDuplicate([3,1,3,4,2]))

if __name__ == '__main__':
    main()