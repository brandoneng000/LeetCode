from typing import List
import collections

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = collections.defaultdict(list)
        res = 0

        for index, num in enumerate(nums):
            pairs[num].append(index)
        
        for pair in pairs.values():
            for i in range(len(pair) - 1, -1, -1):
                for j in range(i - 1, -1, -1):
                    if not (pair[i] * pair[j]) % k:
                        res += 1

        return res                



def main():
    sol = Solution()
    print(sol.countPairs(nums = [3,1,2,2,2,1,3], k = 2))
    print(sol.countPairs(nums = [3,1,2,2,2,2,1,3], k = 2))
    print(sol.countPairs(nums = [1,2,3,4], k = 1))

if __name__ == '__main__':
    main()