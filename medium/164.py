from typing import List
import collections

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        high = max(nums)
        low = min(nums)
        if n <= 2 or high == low:
            return high - low

        bucket = collections.defaultdict(list)
        
        for num in nums:
            index = n - 2 if num == high else (num - low) * (n - 1) // (high - low)
            bucket[index].append(num)
        
        candidates = [[min(bucket[i]), max(bucket[i])] for i in range(n - 1) if bucket[i]]
        return max(y[0] - x[1] for x, y in zip(candidates, candidates[1:]))


        
def main():
    sol = Solution()
    print(sol.maximumGap([3,6,9,1]))
    print(sol.maximumGap([10]))

if __name__ == '__main__':
    main()