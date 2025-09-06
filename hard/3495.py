from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def get(num: int):
            i = 1
            base = 1
            count = 0

            while base <= num:
                count += ((i + 1) // 2) * (min(base * 2 - 1, num) - base + 1)
                i += 1
                base *= 2

            return count
        
        res = 0

        for x, y in queries:
            res += (get(y) - get(x - 1) + 1) // 2
        
        return res

def main():
    sol = Solution()
    print(sol.minOperations([[1,2],[2,4]]))
    print(sol.minOperations([[2,6]]))

if __name__ == '__main__':
    main()