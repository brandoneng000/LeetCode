class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        for n in range(1, min(a, b) + 1):
            res += a % n == 0 and b % n == 0
        
        return res
                

def main():
    sol = Solution()
    print(sol.commonFactors(12,6))
    print(sol.commonFactors(25,30))

if __name__ == '__main__':
    main()