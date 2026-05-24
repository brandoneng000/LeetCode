from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        def dfs(pos: int):
            if pos in visited:
                return
            
            visited[pos] = 1

            i = pos - 1

            while i >= 0 and pos - i <= d and arr[pos] > arr[i]:
                dfs(i)
                visited[pos] = max(visited[pos], visited[i] + 1)
                i -= 1
            
            i = pos + 1

            while i < n and i - pos <= d and arr[pos] > arr[i]:
                dfs(i)
                visited[pos] = max(visited[pos], visited[i] + 1)
                i += 1

        n = len(arr)
        visited = {}

        for i in range(n):
            dfs(i)
        
        return max(visited.values())
        
def main():
    sol = Solution()
    print(sol.maxJumps(arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2))
    print(sol.maxJumps(arr = [3,3,3,3,3], d = 3))
    print(sol.maxJumps(arr = [7,6,5,4,3,2,1], d = 1))

if __name__ == '__main__':
    main()