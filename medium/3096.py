from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        alice = 0
        bob = sum(1 if p == 1 else -1 for p in possible)

        for i in range(n - 1):
            alice += 1 if possible[i] == 1 else -1
            bob += -1 if possible[i] == 1 else 1

            if alice > bob:
                return i + 1

        return -1
        
def main():
    sol = Solution()
    print(sol.minimumLevels([1,0,1,0]))
    print(sol.minimumLevels([1,1,1,1,1]))
    print(sol.minimumLevels([0,0]))

if __name__ == '__main__':
    main()