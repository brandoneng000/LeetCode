from typing import List
import collections

class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     nums_count = collections.Counter(nums[:k])
    #     res = [max(nums_count)]

    #     for i in range(len(nums) - k):
    #         nums_count[nums[i]] -= 1
    #         nums_count[nums[i + k]] += 1
    #         if nums_count[nums[i]] == 0:
    #             nums_count.pop(nums[i])
    #             res.append(max(nums_count))
    #         elif res[-1] < nums[i + k]:
    #             res.append(nums[i + k])
    #         else:
    #             res.append(res[-1])

    #     return res

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cur = collections.deque()
        res = []

        for i in range(k):
            while cur and nums[i] >= nums[cur[-1]]:
                cur.pop()
            cur.append(i)
        
        res.append(nums[cur[0]])

        for i in range(k, len(nums)):
            if cur and cur[0] == i - k:
                cur.popleft()
            while cur and nums[i] >= nums[cur[-1]]:
                cur.pop()
            
            cur.append(i)
            res.append(nums[cur[0]])
        
        return res

    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     res = []
        
    #     for i in range(0, len(nums) - k + 1):
    #         res.append(max(nums[i: i + k]))
        
    #     return res

def main():
    sol = Solution()
    print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(sol.maxSlidingWindow(nums = [1], k = 1))

if __name__ == '__main__':
    main()