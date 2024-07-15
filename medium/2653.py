from typing import List
from collections import deque

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        freq = [0] * 51
        res = []
        left = 0

        for right in range(n):
            if nums[right] < 0:
                freq[abs(nums[right])] += 1
            
            if right - left + 1 >= k:
                count = 0

                for l in range(50, -1, -1):
                    count += freq[l]
                    if count >= x:
                        res.append(-l)
                        break
            
                if count < x:
                    res.append(0)
                if nums[left] < 0:
                    freq[abs(nums[left])] -= 1
                left += 1
            
        return res

    # def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
    #     n = len(nums)
    #     res = []
    #     cur = deque(nums[:k - 1])

    #     for i in range(k - 1, n):
    #         cur.append(nums[i])
    #         val = sorted(cur)[x - 1]
    #         res.append(val if val <= 0 else 0)
    #         cur.popleft()

    #     return res
        
def main():
    sol = Solution()
    print(sol.getSubarrayBeauty(nums = [1,-1,-3,-2,3], k = 3, x = 2))
    print(sol.getSubarrayBeauty(nums = [-1,-2,-3,-4,-5], k = 2, x = 2))
    print(sol.getSubarrayBeauty(nums = [-3,1,2,-3,0,-3], k = 2, x = 1))

if __name__ == '__main__':
    main()