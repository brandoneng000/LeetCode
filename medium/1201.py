from math import gcd

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def helper(mid) -> bool:
            total = (mid // a + mid // b + mid // c - 
                     mid // ab - mid // ac - mid // bc + mid // abc)
            
            return total >= n
        
        ab = a * b // gcd(a, b)
        ac = a * c // gcd(a, c)
        bc = b * c // gcd(b, c)
        abc = a * bc // gcd(a, bc)
        left, right = 1, 10 ** 10
        while left < right:
            mid = left + (right - left) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
            
    # def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
    #     choices = [a, b, c]

    #     for _ in range(n):
    #         cur = min(choices)

    #         if choices[0] == cur:
    #             choices[0] += a
    #         if choices[1] == cur:
    #             choices[1] += b
    #         if choices[2] == cur:
    #             choices[2] += c
        
    #     return cur

def main():
    sol = Solution()
    print(sol.nthUglyNumber(n = 3, a = 2, b = 3, c = 5))
    print(sol.nthUglyNumber(n = 4, a = 2, b = 3, c = 4))
    print(sol.nthUglyNumber(n = 5, a = 2, b = 11, c = 13))

if __name__ == '__main__':
    main()