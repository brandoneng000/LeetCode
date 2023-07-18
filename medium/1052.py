from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        total = sum(c for c, g in zip(customers, grumpy) if g == 0)
        max_tech = tech = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)

        for i in range(minutes, len(customers)):
            if grumpy[left] == 1:
                tech -= customers[left]
            if grumpy[i] == 1:
                tech += customers[i]
            max_tech = max(max_tech, tech)
            left += 1
        
        return total + max_tech

def main():
    sol = Solution()
    print(sol.maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3))
    print(sol.maxSatisfied(customers = [1], grumpy = [0], minutes = 1))

if __name__ == '__main__':
    main()