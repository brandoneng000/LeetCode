from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        arr = [str(num) for num in arr]
        arr_string = ','.join(arr) + ','
        
        for index in range(0, len(arr) - m):
            check = ','.join(arr[index: index + m]) + ','
            check *= k
            if check in arr_string:
                return True
        
        return False

def main():
    sol = Solution()
    print(sol.containsPattern(arr = [1,2,4,4,4,4], m = 1, k = 3))
    print(sol.containsPattern(arr = [1,2,1,2,1,1,1,3], m = 2, k = 2))
    print(sol.containsPattern(arr = [1,2,1,2,1,3], m = 2, k = 3))
    print(sol.containsPattern(arr = [99,9], m = 1, k = 3))
    print(sol.containsPattern(arr = [3,2,2,1,2,2,1,1,1,2,3,2,2], m = 3, k = 2))
    print(sol.containsPattern(arr = [4,2,2,2,2,4,3,4,2,1,3,4,3,4,4,2,1,3,4], m = 3, k = 2))

if __name__ == '__main__':
    main()