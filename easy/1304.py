from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [0] if n % 2 == 1 else []

        for index in range(1, (n // 2) + 1):
            result.append(index)
            result.append(-index)
        
        return result

def main():
    sol = Solution()
    print(sol.sumZero(5))
    print(sol.sumZero(3))
    print(sol.sumZero(1))

if __name__ == '__main__':
    main()