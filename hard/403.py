from typing import List
import collections
import heapq

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = { s: set() for s in stones }
        dp[0].add(0)

        for s in stones:
            for k in dp[s]:
                for step in range(k - 1, k + 2):
                    if step and s + step in dp:
                        dp[s + step].add(step)
        
        return len(dp[stones[-1]]) > 0

    # def canCross(self, stones: List[int]) -> bool:
    #     heap = []
    #     stone_set = set(stones)
    #     heapq.heappush(heap, (0, 0))

    #     while heap:
    #         cur, jump = heapq.heappop(heap)
    #         cur = -cur

    #         if cur == stones[-1]:
    #             return True

    #         if jump - 1 > 0 and cur + jump - 1 in stone_set:
    #             heapq.heappush(heap, (-(cur + jump - 1), jump - 1))
            
    #         if cur + jump in stone_set and jump > 0:
    #             heapq.heappush(heap, (-(cur + jump), jump))
            
    #         if cur + jump + 1 in stone_set:
    #             heapq.heappush(heap, (-(cur + jump + 1), jump + 1))
            
    #     return False

    # def canCross(self, stones: List[int]) -> bool:
    #     stone_set = set(stones)
    #     goal = stones[-1]
    #     q = collections.deque([(0, 1)])

    #     while q:
    #         cur, jump = q.popleft()

    #         if cur == goal:
    #             return True
        
    #         if cur + jump - 1 in stone_set and jump - 1 > 0:
    #             q.append((cur + jump - 1, jump - 1))
    #         if cur + jump in stone_set:
    #             q.append((cur + jump, jump))
    #         if cur + jump + 1 in stone_set:
    #             q.append((cur + jump + 1, jump + 1))

    #     return False


def main():
    sol = Solution()
    print(sol.canCross([0,1,3,5,6,8,12,17]))
    print(sol.canCross([0,1,2,3,4,8,9,11]))

if __name__ == '__main__':
    main()