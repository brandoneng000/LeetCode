from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0

        for num in arr:
            if num % 2:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        
        return False


def main():
    sol = Solution()
    print(sol.threeConsecutiveOdds([2,6,4,1]))
    print(sol.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))

if __name__ == '__main__':
    main()