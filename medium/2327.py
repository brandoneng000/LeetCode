from collections import deque

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 1000000007
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0

        for time in range(2, n + 1):
            if time - delay > 0:
                share = (share + dp[time - delay]) % mod
            if time - forget > 0:
                share = (share - dp[time - forget]) % mod
            dp[time] = share
        
        res = 0
        for i in range(n - forget + 1, n + 1):
            res = (res + dp[i]) % mod
        
        return res

    # def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
    #     mod = 1000000007
    #     delay_q = deque([0] * delay)
    #     forget_q = deque([0] * forget)
    #     share = 0
    #     delay_q[-1] = 1
    #     forget_q[-1] = 1

    #     for _ in range(1, n):
    #         d = delay_q.popleft()
    #         f = forget_q.popleft()
    #         share = (share + d - f) % mod 
    #         delay_q.append(share)
    #         forget_q.append(share)

    #     return (share + sum(delay_q)) % mod
        
def main():
    sol = Solution()
    print(sol.peopleAwareOfSecret(n = 425, delay = 81, forget = 118))
    print(sol.peopleAwareOfSecret(n = 6, delay = 2, forget = 4))
    print(sol.peopleAwareOfSecret(n = 4, delay = 1, forget = 3))

if __name__ == '__main__':
    main()