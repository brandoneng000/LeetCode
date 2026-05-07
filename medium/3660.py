from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        def process(r: int, right_min: float, right_max: float) -> None:
            p_max, pivot_index = prev_max[r]
            cur_max = p_max if p_max <= right_min else right_max

            next_right_min = min(p_max, right_min)

            for i in range(pivot_index, r + 1):
                res[i] = cur_max
                next_right_min = min(next_right_min, nums[i])
            
            if pivot_index == 0:
                return
            
            process(pivot_index - 1, next_right_min, cur_max)

        n = len(nums)
        INF = 10 ** 33
        res = [0] * n
        prev_max = [(0, 0)] * n

        prev = (-INF, -1)

        for i, val in enumerate(nums):
            if val > prev[0]:
                prev = (val, i)
            prev_max[i] = prev

        process(n - 1, INF, 0)
        return res

        
def main():
    sol = Solution()
    print(sol.maxValue([2,1,3]))
    print(sol.maxValue([2,3,1]))

if __name__ == '__main__':
    main()