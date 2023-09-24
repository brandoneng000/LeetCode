from typing import List

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            
            return abs(x)
        
        res = []

        for i in range(2, n + 1):
            for j in range(1, i):
                if gcd(i, j) == 1:
                    res.append(f"{j}/{i}")
        
        return res
        
def main():
    sol = Solution()
    print(sol.simplifiedFractions(2))
    print(sol.simplifiedFractions(3))
    print(sol.simplifiedFractions(4))

if __name__ == '__main__':
    main()