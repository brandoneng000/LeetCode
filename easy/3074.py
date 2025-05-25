from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        
        for i, box in enumerate(sorted(capacity, reverse=True), 1):
            apples -= box

            if apples <= 0:
                return i
        
        return len(capacity)
        
def main():
    sol = Solution()
    print(sol.minimumBoxes(apple = [1,3,2], capacity = [4,3,1,5,2]))
    print(sol.minimumBoxes(apple = [5,5,5], capacity = [2,4,2,7]))

if __name__ == '__main__':
    main()