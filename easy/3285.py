from typing import List

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        n = len(height)
        res = []

        for i in range(1, n):
            if height[i - 1] > threshold:
                res.append(i)
        
        return res
        
def main():
    sol = Solution()
    print(sol.stableMountains(height = [1,2,3,4,5], threshold = 2))
    print(sol.stableMountains(height = [10,1,10,1,10], threshold = 3))
    print(sol.stableMountains(height = [10,1,10,1,10], threshold = 10))

if __name__ == '__main__':
    main()