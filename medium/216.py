from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []

        def calculate_sum(cur: List[int], start: int):
            if len(cur) == k:
                if sum(cur) == n:
                    self.res.append(cur.copy())
                return
            if sum(cur) > n:
                return
            
            for num in range(start, 10):
                cur.append(num)
                calculate_sum(cur, num + 1)
                cur.pop()
        
        calculate_sum([], 1)
        return self.res

def main():
    sol = Solution()
    print(sol.combinationSum3(k = 3, n = 7))
    print(sol.combinationSum3(k = 3, n = 9))
    print(sol.combinationSum3(k = 4, n = 1))

if __name__ == '__main__':
    main()