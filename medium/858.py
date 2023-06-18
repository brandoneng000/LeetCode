import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        common = math.lcm(p, q)
        
        if common // q % 2 == 0:
            return 2
        
        return common // p % 2

def main():
    sol = Solution()
    print(sol.mirrorReflection(p = 2, q = 1))
    print(sol.mirrorReflection(p = 3, q = 1))

if __name__ == '__main__':
    main()