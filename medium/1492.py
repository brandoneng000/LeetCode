import collections

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        front = []
        back = collections.deque()

        for factor in range(1, int(n ** 0.5) + 1):
            if n % factor == 0:
                front.append(factor)
                if n // factor == factor:
                    break
                back.appendleft(n // factor)
            if len(front) == k:
                return front[-1]
        
        combine = front + list(back)
        return combine[k - 1] if k <= len(combine) else -1

def main():
    sol = Solution()
    print(sol.kthFactor(n = 24, k = 6))
    print(sol.kthFactor(n = 4, k = 1))
    print(sol.kthFactor(n = 12, k = 3))
    print(sol.kthFactor(n = 7, k = 2))
    print(sol.kthFactor(n = 4, k = 4))

if __name__ == '__main__':
    main()