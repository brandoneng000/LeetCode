from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        low = high = cur = 0

        for diff in differences:
            cur += diff
            low = min(low, cur)
            high = max(high, cur)

            if high - low > upper - lower:
                return 0
        
        return (upper - lower) - (high - low) + 1

    # def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
    #     n = len(differences)
    #     prefix = [0]

    #     for i in range(n):
    #         prefix.append(prefix[-1] + differences[i])
        
    #     low, high = min(prefix), max(prefix)
    #     lower_bound = lower - low
    #     upper_bound = upper - high

    #     if lower_bound > upper_bound:
    #         return 0
        
    #     return upper_bound - lower_bound + 1
        
def main():
    sol = Solution()
    print(sol.numberOfArrays(differences = [1,-3,4], lower = 1, upper = 6))
    print(sol.numberOfArrays(differences = [3,-4,5,1,-2], lower = -4, upper = 5))
    print(sol.numberOfArrays(differences = [4,-7,2], lower = 3, upper = 6))

if __name__ == '__main__':
    main()