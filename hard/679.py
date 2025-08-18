from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums: List[int]) -> bool:
            n = len(nums)
            if n == 1:
                return abs(nums[0] - 24.0) < EPS

            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue

                    next_nums = [nums[k] for k in range(n) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    candidates = [a + b, a - b, b - a, a * b]

                    if abs(b) > EPS:
                        candidates.append(a / b)
                    
                    if abs(a) > EPS:
                        candidates.append(b / a)
                    
                    for val in candidates:
                        if dfs(next_nums + [val]):
                            return True
                
            return False
        
        EPS = 1e-6
        return dfs([float(num) for num in cards])


        
def main():
    sol = Solution()
    print(sol.judgePoint24([4,1,8,7]))
    print(sol.judgePoint24([1,2,1,2]))

if __name__ == '__main__':
    main()