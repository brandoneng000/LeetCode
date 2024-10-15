from collections import deque

class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        res = 0
        white = 0
        
        for i in range(n):
            if s[i] == '0':
                res += i - white
                white += 1
        
        return res

    
    # def minimumSteps(self, s: str) -> int:
    #     n = len(s)
    #     left = 0
    #     right = n - 1

    #     while left < n and s[left] == '0':
    #         left += 1

    #     while right > 0 and s[right] == '1':
    #         right -= 1

    #     if left > right:
    #         return 0
        
    #     ball_q = deque(list(s[left: right + 1]))
    #     ones = ball_q.count('1')
    #     res = 0

    #     while ball_q:
    #         ball = ball_q.popleft()

    #         if ball == '1':
    #             ones -= 1
    #             res += len(ball_q) - ones
        
    #     return res

        
def main():
    sol = Solution()
    print(sol.minimumSteps("111111111100100010"))
    print(sol.minimumSteps("1001001"))
    print(sol.minimumSteps("101"))
    print(sol.minimumSteps("100"))
    print(sol.minimumSteps("0111"))

if __name__ == '__main__':
    main()