from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)

        while left < right:
            mid = (left + right) // 2
            cur_sum = 0

            for q in quantities:
                cur_sum += (q + mid - 1) // mid
            
            if cur_sum > n:
                left = mid + 1
            else:
                right = mid
        
        return left


        
def main():
    sol = Solution()
    print(sol.minimizedMaximum(n = 6, quantities = [11,6]))
    print(sol.minimizedMaximum(n = 7, quantities = [15,10,10]))
    print(sol.minimizedMaximum(n = 1, quantities = [100000]))

if __name__ == '__main__':
    main()