from typing import List
import collections

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)

        for i in sorted(count):
            if count[i] > 0:
                for j in range(k)[::-1]:
                    count[i + j] -= count[i]
                    if count[i + j] < 0:
                        return False
        
        return True
    
    # def isPossibleDivide(self, nums: List[int], k: int) -> bool:
    #     n = len(nums)
    #     if n % k != 0:
    #         return False
        
    #     nums.sort()
    #     count = collections.Counter()

    #     for n in nums:
    #         if count.get(n, 0) > 0:
    #             count[n] -= 1
    #             if count[n] == 0:
    #                 count.pop(n)
    #         else:
    #             for i in range(n + 1, n + k):
    #                 count[i] += 1
        
    #     return not count
        

def main():
    sol = Solution()
    print(sol.isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4))
    print(sol.isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3))
    print(sol.isPossibleDivide(nums = [1,2,3,4], k = 3))

if __name__ == '__main__':
    main()