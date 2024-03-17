from typing import List

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        left, right = 0, n - 1
        res = 0
        alice, bob = capacityA, capacityB

        while left <= right:
            if left == right:
                if plants[left] > max(alice, bob):
                    res += 1
            else:
                if plants[left] > alice:
                    alice = capacityA
                    res += 1
                if plants[right] > bob:
                    bob = capacityB
                    res += 1
                alice -= plants[left]
                bob -= plants[right]

            left += 1
            right -= 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.minimumRefill(plants = [2,2,3,3], capacityA = 5, capacityB = 5))
    print(sol.minimumRefill(plants = [2,2,3,3], capacityA = 3, capacityB = 4))
    print(sol.minimumRefill(plants = [5], capacityA = 10, capacityB = 8))

if __name__ == '__main__':
    main()