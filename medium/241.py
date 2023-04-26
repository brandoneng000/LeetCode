from typing import List

class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def diffWaysToCompute(self, expression: str) -> List[int]: 
        def recursion(input):
            if input in self.cache:
                return self.cache[input]
            if input.isdigit():
                self.cache[input] = [int(input)]
                return [int(input)]

            ret = []
            for i, c in enumerate(input):
                if c in "+-*":
                    l = self.diffWaysToCompute(input[:i])
                    r = self.diffWaysToCompute(input[i + 1:])
                    ret.extend(eval(str(x) + c + str(y)) for x in l for y in r)
            
            self.cache[input] = ret
            
            return ret
        
        return recursion(expression)

def main():
    sol = Solution()
    print(sol.diffWaysToCompute("2-1-1"))
    print(sol.diffWaysToCompute("2*3-4*5"))
    # print(sol.diffWaysToCompute("2*3-4*5*2+3+5+6+1"))

if __name__ == '__main__':
    main()