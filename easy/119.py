from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for _ in range(1, rowIndex + 1):
            next_row = [1] + [0] * (len(res) - 1) + [1]
            
            for i in range(1, len(next_row) - 1):
                next_row[i] = res[i - 1] + res[i]
            
            res = next_row

        return res
        
def main():
    sol = Solution()
    print(sol.getRow(3))
    print(sol.getRow(0))
    print(sol.getRow(1))

if __name__ == '__main__':
    main()