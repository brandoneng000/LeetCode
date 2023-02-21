from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        box_units = {}
        units = 0

        for box in boxTypes:
            box_units[box[1]] = box_units.get(box[1], 0) + box[0]

        for unit in sorted(box_units.keys(), reverse=True):
            if truckSize < box_units[unit]:
                units += unit * truckSize
                truckSize = 0
            else:
                units += unit * box_units[unit]
                truckSize -= box_units[unit]
            
            if truckSize == 0:
                break

        return units

def main():
    sol = Solution()
    print(sol.maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))
    print(sol.maximumUnits([[5,10],[2,5],[4,7],[3,9]], truckSize = 10))

if __name__ == '__main__':
    main()