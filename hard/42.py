from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        if n <= 2:
            return 0
        
        res = 0
        left, right = 1, n - 1

        max_left = height[0]
        max_right = height[-1]

        while left <= right:
            if height[left] > max_left:
                max_left = height[left]
            if height[right] > max_right:
                max_right = height[right]
            
            if max_left <= max_right:
                res += max_left - height[left]
                left += 1
            else:
                res += max_right - height[right]
                right -= 1
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(sol.trap([4,2,0,3,2,5]))

if __name__ == '__main__':
    main()