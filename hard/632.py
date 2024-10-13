from typing import List
from collections import Counter

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        flat_nums = []
        freq = Counter()

        for i, row in enumerate(nums):
            flat_nums.extend([[num, i] for num in row])
        
        flat_nums.sort()
        m = len(flat_nums)
        res_start = 0
        res_end = float('inf')
        count = left = 0
        
        for right in range(m):
            freq[flat_nums[right][1]] += 1
            
            if freq[flat_nums[right][1]] == 1:
                count += 1

            while count == len(nums):
                cur_range = flat_nums[right][0] - flat_nums[left][0]

                if cur_range < res_end - res_start:
                    res_start = flat_nums[left][0]
                    res_end = flat_nums[right][0]
                
                freq[flat_nums[left][1]] -= 1

                if freq[flat_nums[left][1]] == 0:
                    count -= 1
                
                left += 1

        return [res_start, res_end]

def main():
    sol = Solution()
    print(sol.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
    print(sol.smallestRange([[1,2,3],[1,2,3],[1,2,3]]))

if __name__ == '__main__':
    main()