from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        balls = [i for i in range(n) if boxes[i] == '1']
        res = [0] * n

        for i in range(n):
            res[i] = sum(abs(i - j) for j in balls)
        
        return res
        
def main():
    sol = Solution()
    print(sol.minOperations("110"))
    print(sol.minOperations("001011"))

if __name__ == '__main__':
    main()