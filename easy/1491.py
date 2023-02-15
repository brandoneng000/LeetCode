from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)

def main():
    sol = Solution()
    print(sol.average([4000,3000,1000,2000]))
    print(sol.average([1000,2000,3000]))

if __name__ == '__main__':
    main()