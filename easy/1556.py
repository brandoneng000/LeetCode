from collections import deque


class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        res = deque()
        
        for i in range(1, len(n) + 1):
            res.appendleft(n[-i])
            if i % 3 == 0:
                res.appendleft(".")

        if res[0] == ".":
            res.popleft()

        return "".join(res)

def main():
    sol = Solution()
    print(sol.thousandSeparator(987))
    print(sol.thousandSeparator(1234))
    print(sol.thousandSeparator(123456))

if __name__ == '__main__':
    main()