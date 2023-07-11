from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = max(weights)
        total_weight = sum(weights)
        
        def check_weight(weight: int):
            cur = 0
            count = 1
            for w in weights:
                cur += w
                if cur > weight:
                    count += 1
                    cur = w
            
            return count <= days
        
        while max_weight < total_weight:
            weight = (max_weight + total_weight) // 2
            if check_weight(weight):
                total_weight = weight
            else:
                max_weight = weight + 1
                
        return max_weight


def main():
    sol = Solution()
    print(sol.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))
    print(sol.shipWithinDays(weights = [3,2,2,4,1,4], days = 3))
    print(sol.shipWithinDays(weights = [1,2,3,1,1], days = 4))

if __name__ == '__main__':
    main()