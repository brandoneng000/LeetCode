from typing import List
import collections

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # min_colors = collections.defaultdict(lambda: 1000)
        # max_colors = collections.defaultdict(int)
        # max_distance = 0

        # for index, val in enumerate(colors):
        #     min_colors[val] = min(min_colors[val], index)
        #     max_colors[val] = max(max_colors[val], index)
       
        # for color in colors:
        #     for dif in colors:
        #         if color != dif:
        #             max_distance = max(max_distance, abs(max_colors[color] - min_colors[dif]))

        # return max_distance
        left, right = 0, len(colors) - 1
        while colors[0] == colors[right]:
            right -= 1
        while colors[-1] == colors[left]:
            left += 1
        return max(len(colors) - 1 - left, right)

def main():
    sol = Solution()
    print(sol.maxDistance(colors = [1,1,1,6,1,1,1]))
    print(sol.maxDistance(colors = [1,8,3,8,3]))
    print(sol.maxDistance([0,1]))

if __name__ == '__main__':
    main()