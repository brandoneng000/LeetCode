from typing import List
import heapq

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]
        
        arr.sort(key=lambda x: (abs(x - median), x))
        return arr[n - k:]
        
def main():
    sol = Solution()
    print(sol.getStrongest(arr = [-7,22,17,3], k = 2))
    print(sol.getStrongest(arr = [1,2,3,4,5], k = 2))
    print(sol.getStrongest(arr = [1,1,3,5,5], k = 2))
    print(sol.getStrongest(arr = [6,7,11,7,6,8], k = 5))

if __name__ == '__main__':
    main()