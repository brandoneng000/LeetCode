from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_num = min(nums)
        max_num = max(nums)
        num_set = set(nums)
        res = []


        for i in range(min_num, max_num + 1):
            if i in num_set:
                continue
            res.append(i)

        return res


def main():
    sol = Solution()
    print(sol.findMissingElements([1,4,2,5]))
    print(sol.findMissingElements([7,8,6,9]))
    print(sol.findMissingElements([5,1]))

if __name__ == '__main__':
    main()