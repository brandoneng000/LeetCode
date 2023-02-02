from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        
        for op in operations:
            if op == '+':
                score.append(score[-1] + score[-2])
            elif op == 'D':
                score.append(score[-1] * 2)
            elif op == 'C':
                score.pop()
            else:
                score.append(int(op))
        
        return sum(score)

def main():
    sol = Solution()
    print(sol.calPoints(["5","2","C","D","+"]))
    print(sol.calPoints(["5","-2","4","C","D","9","+","+"]))
    print(sol.calPoints(["1","C"]))

if __name__ == '__main__':
    main()