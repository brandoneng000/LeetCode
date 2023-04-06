from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items = {}

        for value, weight in items1:
            items[value] = items.get(value, 0) + weight
        
        for value, weight in items2:
            items[value] = items.get(value, 0) + weight
        
        return sorted(items.items())

def main():
    sol = Solution()
    print(sol.mergeSimilarItems(items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]))
    print(sol.mergeSimilarItems(items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]))
    print(sol.mergeSimilarItems(items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]))

if __name__ == '__main__':
    main()