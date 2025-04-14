from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        res = 0
        total = [0] * 1001

        for i in range(n):
            for j in range(i + 1, n):
                if abs(arr[i] - arr[j]) <= b:
                    li, ri = arr[i] - a, arr[i] + a
                    lj, rj = arr[j] - c, arr[j] + c
                    left = max(0, li, lj)
                    right = min(1000, ri, rj)
                
                    if left <= right:
                        res += total[right] if left == 0 else total[right] - total[left - 1]

            for j in range(arr[i], 1001):
                total[j] += 1
        
        return res

    # def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
    #     result = []
        
    #     def checkTriplets(stack: List[int]):
    #         if abs(stack[0] - stack[1]) > a:
    #             return False
    #         elif abs(stack[1] - stack[2]) > b:
    #             return False
    #         elif abs(stack[0] - stack[2]) > c:
    #             return False
    #         return True

    #     def findGoodTriplets(arr: List[int], stack: List[int], index: int):
    #         if len(stack) == 3:
    #             if checkTriplets(stack):
    #                 result.append(stack.copy())
    #             else:
    #                 return
            
    #         for i in range(index, len(arr)):
    #             stack.append(arr[i])
    #             findGoodTriplets(arr, stack, i + 1)
    #             stack.pop()
        
    #     findGoodTriplets(arr, [], 0)
    #     return len(result)
    
    # def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
    #     def checkTriplet(first: int, second: int, third: int) -> bool:
    #         if abs(first - second) > a:
    #             return False
    #         elif abs(second - third) > b:
    #             return False
    #         elif abs(first - third) > c:
    #             return False
    #         return True

    #     result = 0
    #     size = len(arr)
    #     for i in range(size):
    #         for j in range(i + 1, size):
    #             for k in range(j + 1, size):
    #                 result += checkTriplet(arr[i], arr[j], arr[k])
        
    #     return result


def main():
    sol = Solution()
    print(sol.countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))
    print(sol.countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1))
    print(sol.countGoodTriplets(arr = [23,17,14,37,37,2,16,17,35,34,20,18,22,24,39,29,11,17,38,5,32,7,3,36,36,34,45], a = 9, b = 23, c = 23))

if __name__ == '__main__':
    main()