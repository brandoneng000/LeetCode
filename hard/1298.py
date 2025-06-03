from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        owned_keys = set()
        closed_boxes = deque()
        empty_boxes = set()
        cur_boxes = deque(initialBoxes)
        res = 0

        while cur_boxes:
            box = cur_boxes.popleft()

            if box in empty_boxes:
                continue

            if status[box] == 0 and box not in owned_keys:
                closed_boxes.append(box)
                continue

            empty_boxes.add(box)
            res += candies[box]
            owned_keys.update(keys[box])
            cur_boxes.extend(containedBoxes[box])

            size = len(closed_boxes)

            for _ in range(size):
                temp = closed_boxes.popleft()

                if temp in owned_keys:
                    cur_boxes.append(temp)
                else:
                    closed_boxes.append(temp)
        
        return res

        
def main():
    sol = Solution()
    print(sol.maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]))
    print(sol.maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]))

if __name__ == '__main__':
    main()