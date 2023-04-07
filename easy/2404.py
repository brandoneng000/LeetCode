from typing import List
import collections

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums_dict = collections.Counter(nums)
        size = 0
        res = 100000

        for num in nums_dict:
            if not num & 1:
                if nums_dict[num] > size:
                    size = nums_dict[num]
                    res = num
                elif nums_dict[num] == size:
                    res = min(res, num)


        return res if res != 100000 else -1


def main():
    sol = Solution()
    print(sol.mostFrequentEven([0,1,2,2,4,4,1]))
    print(sol.mostFrequentEven([4,4,4,9,2,4]))
    print(sol.mostFrequentEven([29,47,21,41,13,37,25,7]))
    print(sol.mostFrequentEven([0,1,2,2,4,4,1]))

if __name__ == '__main__':
    main()