from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # nums = [str(num) for num in nums]
        # result = 0

        # for num in nums:
        #     if not len(num) % 2:
        #         result += 1

        # return result

        return sum([not len(str(num)) % 2 for num in nums])

def main():
    sol = Solution()
    print(sol.findNumbers([12,345,2,6,7896]))
    print(sol.findNumbers([555,901,482,1771]))

if __name__ == '__main__':
    main()