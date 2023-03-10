from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for op in operations:
            if '+' == op[1]:
                result += 1
            else:
                result -= 1
        
        return result

def main():
    sol = Solution()
    print(sol.finalValueAfterOperations(["--X","X++","X++"]))
    print(sol.finalValueAfterOperations(["++X","++X","X++"]))
    print(sol.finalValueAfterOperations(["X++","++X","--X","X--"]))

if __name__ == '__main__':
    main()