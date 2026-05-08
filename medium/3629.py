from typing import List
from collections import deque

class Solution:
    N = 10 ** 6 + 5
    prime = [True] * N
    prime[0] = prime[1] = False

    for i in range(2, 1001):
        if prime[i]:
            for j in range(i * i, N, i):
                prime[j] = False

    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        limit = nums[0]

        for num in nums:
            limit = max(limit, num)

        head = [-1] * (limit + 1)
        nxt = [-1] * n

        for i in range(n):
            val = nums[i]
            nxt[i] = head[val]
            head[val] = i

        dp = [-1] * n
        dp[0] = 0
        q = deque([0])
        visited = set()

        while q:
            node = q.popleft()

            if node == n - 1:
                return dp[node]
            
            right = node + 1

            if right < n and dp[right] == -1:
                dp[right] = dp[node] + 1
                q.append(right)
            
            left = node - 1

            if left >= 0 and dp[left] == -1:
                dp[left] = dp[node] + 1
                q.append(left)
            
            val = nums[node]

            if Solution.prime[val] and val not in visited:
                visited.add(val)

                for i in range(val, limit + 1, val):
                    j = head[i]

                    while j != -1:
                        if dp[j] == -1:
                            dp[j] = dp[node] + 1
                            q.append(j)
                        j = nxt[j]
                    head[i] = -1
        
        return -1

        
def main():
    sol = Solution()
    print(sol.minJumps([1,2,4,6]))
    print(sol.minJumps([2,3,4,7,9]))
    print(sol.minJumps([4,6,5,8]))

if __name__ == '__main__':
    main()