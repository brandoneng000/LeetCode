from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        num_dict = {}
        for index in range(len(nums)):
            num_dict[index + 1] = 0
        
        for num in nums:
            num_dict[num] += 1

        res = [key for key, value in num_dict.items() if 0 == value]
        return res


def main():
    sol = Solution()
    print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print(sol.findDisappearedNumbers([1,1]))
    print(sol.findDisappearedNumbers([]))

if __name__ == '__main__':
    main()