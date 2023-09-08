from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            temp1 = res[-1] + [0]
            temp2 = [0] + res[-1]
            
            res.append([temp1[i] + temp2[i] for i in range(len(temp1))])
        
        return res

    # def generate(self, numRows: int) -> List[List[int]]:
    #     res = [[1] for _ in range(numRows)]

    #     for i in range(1, numRows):
    #         for j in range((len(res[i - 1]) // 2)):
    #             res[i].append(res[i - 1][j] + res[i - 1][j + 1])
            
    #         if i % 2 == 1:
    #             res[i] += (res[i][::-1].copy())
    #         else:
    #             res[i] += res[i][:-1][::-1]
        
    #     return res

def main():
    sol = Solution()
    print(sol.generate(2))
    print(sol.generate(5))
    print(sol.generate(1))

if __name__ == '__main__':
    main()