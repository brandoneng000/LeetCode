from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def sum_digits(num: int):
            res = 0

            while num:
                num, r = divmod(num, 10)
                res += r

            return (res, num)

        n = len(nums)
        num_index = { nums[i]: i for i in range(n) }
        index_num = { i: nums[i] for i in range(n) }
        nums.sort(key=lambda x: (sum_digits(x), x))
        res = 0

        for i, num in enumerate(nums):
            if i != num_index[num]:
                res += 1
                prev_num = index_num[i]
                prev_index = num_index[num]

                num_index[num], num_index[prev_num] = i, prev_index
                index_num[prev_index], index_num[i] = prev_num, num

        return res

def main():
    sol = Solution()
    print(sol.minSwaps([37,100]))
    print(sol.minSwaps([22,14,33,7]))
    print(sol.minSwaps([18,43,34,16]))

if __name__ == '__main__':
    main()