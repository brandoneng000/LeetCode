from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        unique = len(set(nums))
        count = {}
        res = 0
        right = 0

        for left in range(n):
            if left > 0:
                remove = nums[left - 1]
                count[remove] -= 1

                if count[remove] == 0:
                    count.pop(remove)
            
            while right < n and len(count) < unique:
                add = nums[right]
                count[add] = count.get(add, 0) + 1
                right += 1

            if len(count) == unique:
                res += n - right + 1
        
        return res

    # def countCompleteSubarrays(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     count = len(set(nums))
    #     res = 0

    #     for i in range(n):
    #         cur = set()
    #         for j in range(i, n):
    #             cur.add(nums[j])

    #             if len(cur) == count:
    #                 res += n - j
    #                 break
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.countCompleteSubarrays([1,3,1,2,2]))
    print(sol.countCompleteSubarrays([5,5,5,5]))

if __name__ == '__main__':
    main()