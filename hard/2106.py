from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = k * 2 + 1
        middle = k
        fruit_line = [0] * n
        res = 0
        
        for pos, f in fruits:
            if startPos - k - 1 < pos < startPos + k + 1:
                fruit_line[pos - (startPos - k)] = f
            
            if pos == startPos:
                res = f

        left_total = sum(fruit_line[:middle + 1])
        left = 0
        res = max(res, left_total)
        # print(left_total, fruit_line[:middle + 1])
        
        for r in range(middle + 1, n):
            left_total -= fruit_line[left]
            left_total -= fruit_line[left + 1]
            left += 2
            left_total += fruit_line[r]
            res = max(res, left_total)
        
        right_total = sum(fruit_line[middle:])
        right = n - 1
        res = max(res, right_total)

        # print(right_total, fruit_line[middle:])

        for l in range(middle - 1, -1, -1):
            right_total -= fruit_line[right]
            right_total -= fruit_line[right - 1]
            right -= 2
            right_total += fruit_line[l]
            res = max(res, right_total)
        
        return res


        
def main():
    sol = Solution()
    print(sol.maxTotalFruits(fruits = [[0,2],[3,4],[5,1],[8,10],[13,3],[17,6],[22,2],[28,9],[35,5],[43,1],[52,7]], startPos = 20, k = 15))
    print(sol.maxTotalFruits(fruits = [[2,8],[6,3],[8,6],[9,31]], startPos = 5, k = 4))
    print(sol.maxTotalFruits(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4))
    print(sol.maxTotalFruits(fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4))
    print(sol.maxTotalFruits(fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2))

if __name__ == '__main__':
    main()