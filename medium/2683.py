from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2 == 0
        
def main():
    sol = Solution()
    print(sol.doesValidArrayExist([1,1,0]))
    print(sol.doesValidArrayExist([1,1]))
    print(sol.doesValidArrayExist([1,0]))

if __name__ == '__main__':
    main()