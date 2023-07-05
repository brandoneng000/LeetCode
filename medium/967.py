from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def helper(cur: int, n: int, k: int):
            if n == 0:
                res.append(cur)
                return
            
            if (cur) % 10 + k < 10:
                helper(cur * 10 + (cur) % 10 + k, n - 1, k)
            if (cur) % 10 - k >= 0:
                helper(cur * 10 + (cur) % 10 - k, n - 1, k)

        res = []

        for i in range(1, 10):
            helper(i, n - 1, k)
        
        return list(set(res))

def main():
    sol = Solution()
    print(sol.numsSameConsecDiff(n = 3, k = 7))
    print(sol.numsSameConsecDiff(n = 2, k = 1))

if __name__ == '__main__':
    main()