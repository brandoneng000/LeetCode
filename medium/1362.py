from typing import List

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def find_divisors(num: int) -> List[List[int]]:
            res = [[1, num]]

            for i in range(2, int((num) ** 0.5) + 1):
                if num % i == 0:
                    res.append([i, num // i])
            
            return res
        
        return min(find_divisors(num + 1) + find_divisors(num + 2), key=lambda x: abs(x[1] - x[0]))
        

def main():
    sol = Solution()
    print(sol.closestDivisors(8))
    print(sol.closestDivisors(123))
    print(sol.closestDivisors(999))

if __name__ == '__main__':
    main()