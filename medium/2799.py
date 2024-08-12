from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = len(set(nums))
        res = 0

        for i in range(n):
            cur = set()
            for j in range(i, n):
                cur.add(nums[j])

                if len(cur) == count:
                    res += n - j
                    break
        
        return res
        
def main():
    sol = Solution()
    print(sol.countCompleteSubarrays([1,3,1,2,2]))
    print(sol.countCompleteSubarrays([5,5,5,5]))

if __name__ == '__main__':
    main()