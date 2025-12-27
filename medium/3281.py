from typing import List

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        def check(middle: int):
            x = -float('inf')

            for s in start:
                x += middle
                if x > s + d:
                    return False
                x = max(x, s)
            
            return True
        
        start.sort()
        left = 0
        right = 2_000_000_000

        while left < right:
            middle = (left + right + 1) // 2

            if check(middle):
                left = middle
            else:
                right = middle - 1
            
        return left
    
        
def main():
    sol = Solution()
    print(sol.maxPossibleScore(start = [6,0,3], d = 2))
    print(sol.maxPossibleScore(start = [2,6,13,13], d = 5))

if __name__ == '__main__':
    main()