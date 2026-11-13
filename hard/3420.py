from typing import List
from heapq import heappush, heappop

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        operations = 0

        heap = []
        cnt = [[] for _ in range(n)]
        pos = [n] * n
        st = []

        left = 0

        for right in range(n):
            while st and nums[right] >= nums[st[-1]]:
                pos[st[-1]] = right
                st.pop()

            if st:
                cnt[st[-1]].append(right)
            st.append(right)

            heappush(heap, (-nums[right], right))
            operations += max(0, -heap[0][0] - nums[right])

            while operations > k:
                for i in cnt[left]:
                    operations -= (nums[left] - nums[i]) * (min(pos[i], right + 1) - i)
                left += 1

            while heap and heap[0][1] < left:
                heappop(heap)

            res += right - left + 1

        return res

def main():
    sol = Solution()
    print(sol.countNonDecreasingSubarrays(nums = [6,3,1,2,4,4], k = 7))
    print(sol.countNonDecreasingSubarrays(nums = [6,3,1,3,6], k = 4))

if __name__ == '__main__':
    main()