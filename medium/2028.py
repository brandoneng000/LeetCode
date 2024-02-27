from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        size = m + n
        max_size = 6 * n
        difference = mean * size - sum(rolls)
        
        if difference < n or difference > max_size:
            return []
        
        res = []
        while difference - 6 > n - 1:
            res.append(6)
            difference -= 6
            n -= 1
        
        if difference > n:
            res.append(difference - (n - 1))
            n -= 1
            difference -= 1

        return res + [1 for _ in range(n)]

        
def main():
    sol = Solution()
    print(sol.missingRolls(rolls = [6,1,6,2,4,4,5], mean = 5, n = 16))
    print(sol.missingRolls(rolls = [3,2,4,3], mean = 4, n = 2))
    print(sol.missingRolls(rolls = [1,5,6], mean = 3, n = 4))
    print(sol.missingRolls(rolls = [1,2,3,4], mean = 6, n = 4))

if __name__ == '__main__':
    main()