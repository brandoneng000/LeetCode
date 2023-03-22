from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        index_odd = []
        index_even = []

        for index, val in enumerate(nums):
            if index & 1:
                index_odd.append(val)
            else:
                index_even.append(val)

        index_even.sort()
        index_odd.sort(reverse=True)

        for index in range(len(nums)):
            if index & 1:
                nums[index] = index_odd[index // 2]
            else:
                nums[index] = index_even[index // 2]
        
        return nums


def main():
    sol = Solution()
    print(sol.sortEvenOdd([4,1,2,3]))
    print(sol.sortEvenOdd([2,1]))

if __name__ == '__main__':
    main()