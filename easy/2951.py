from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        res = []

        for i in range(1, n - 1):
            if mountain[i - 1] < mountain[i] > mountain[i + 1]:
                res.append(i)
        
        return res
        
def main():
    sol = Solution()
    print(sol.findPeaks([2,4,4]))
    print(sol.findPeaks([1,4,3,8,5]))

if __name__ == '__main__':
    main()