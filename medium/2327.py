from collections import deque

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 1000000007
        delay_q = deque([0] * delay)
        forget_q = deque([0] * forget)
        share = 0
        delay_q[-1] = 1
        forget_q[-1] = 1

        for _ in range(1, n):
            d = delay_q.popleft()
            f = forget_q.popleft()
            share = (share + d - f) % mod 
            delay_q.append(share)
            forget_q.append(share)

        return (share + sum(delay_q)) % mod
        
def main():
    sol = Solution()
    print(sol.peopleAwareOfSecret(n = 425, delay = 81, forget = 118))
    print(sol.peopleAwareOfSecret(n = 6, delay = 2, forget = 4))
    print(sol.peopleAwareOfSecret(n = 4, delay = 1, forget = 3))

if __name__ == '__main__':
    main()