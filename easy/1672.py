from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = -1

        for money in accounts:
            result = max(sum(money), result)
        
        return result


def main():
    sol = Solution()
    print(sol.maximumWealth([[1,2,3],[3,2,1]]))
    print(sol.maximumWealth([[1,5],[7,3],[3,5]]))
    print(sol.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))

if __name__ == '__main__':
    main()