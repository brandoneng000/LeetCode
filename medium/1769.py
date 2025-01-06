from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n

        balls_left = moves_left = 0
        balls_right = moves_right = 0

        for i in range(n):
            res[i] += moves_left
            balls_left += int(boxes[i])
            moves_left += balls_left

            j = n - 1 - i
            res[j] += moves_right
            balls_right += int(boxes[j])
            moves_right += balls_right
        
        return res

    # def minOperations(self, boxes: str) -> List[int]:
    #     n = len(boxes)
    #     balls = [i for i in range(n) if boxes[i] == '1']
    #     res = [0] * n

    #     for i in range(n):
    #         res[i] = sum(abs(i - j) for j in balls)
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.minOperations("110"))
    print(sol.minOperations("001011"))

if __name__ == '__main__':
    main()