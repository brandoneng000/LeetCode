from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        from collections import Counter
        heights_count = Counter(heights)
        height_key = sorted(heights_count.keys())
        results = 0
        index = 0

        for height in height_key:
            while heights_count[height] > 0:
                heights_count[height] -= 1
                if heights[index] != height:
                    results += 1
                index += 1
        
        return results


def main():
    sol = Solution()
    print(sol.heightChecker([1,1,4,2,1,3]))
    print(sol.heightChecker([5,1,2,3,4]))
    print(sol.heightChecker([1,2,3,4,5]))

if __name__ == '__main__':
    main()