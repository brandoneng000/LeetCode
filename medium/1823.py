from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque(range(1, n + 1))

        while len(q) > 1:
            for _ in range(k - 1):
                temp = q.popleft()
                q.append(temp)
            
            q.popleft()
        
        return q[0]

        
def main():
    sol = Solution()
    print(sol.findTheWinner(n = 5, k = 2))
    print(sol.findTheWinner(n = 6, k = 5))

if __name__ == '__main__':
    main()