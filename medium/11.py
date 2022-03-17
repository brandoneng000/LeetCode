from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0
        
        while start < end:
            max_area = max(max_area, (end - start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        
        return max_area
            
def main():
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))

if __name__ == '__main__':
    main()