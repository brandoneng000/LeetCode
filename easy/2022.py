from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        if len(original) != m * n:
            return result
        
        temp = []
        for num in original:
            temp.append(num)
            if len(temp) == n:
                result.append(temp)
                temp = []
        
        return result


def main():
    sol = Solution()
    print(sol.construct2DArray(original = [1,2,3,4], m = 2, n = 2))
    print(sol.construct2DArray(original = [1,2,3], m = 1, n = 3))
    print(sol.construct2DArray(original = [1,2], m = 1, n = 1))

if __name__ == '__main__':
    main()