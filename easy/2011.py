from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if '+' == op[1] else -1 for op in operations)

    # def finalValueAfterOperations(self, operations: List[str]) -> int:
    #     res = 0

    #     for op in operations:
    #         res += 1 if '+' == op[1] else -1
        
    #     return res

    # def finalValueAfterOperations(self, operations: List[str]) -> int:
    #     result = 0
    #     for op in operations:
    #         if '+' == op[1]:
    #             result += 1
    #         else:
    #             result -= 1
        
    #     return result

def main():
    sol = Solution()
    print(sol.finalValueAfterOperations(["--X","X++","X++"]))
    print(sol.finalValueAfterOperations(["++X","++X","X++"]))
    print(sol.finalValueAfterOperations(["X++","++X","--X","X--"]))

if __name__ == '__main__':
    main()