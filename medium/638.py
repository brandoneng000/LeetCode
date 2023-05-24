from typing import List

class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        if tuple(needs) in self.cache:
            return self.cache[tuple(needs)]
        
        cur_total = sum(p * n for p, n in zip(price, needs))
    
        for s in special:
            temp = needs.copy()
            exit_status = False
            for i in range(len(temp)):
                n = temp[i] - s[i]
                if n < 0:
                    exit_status = True
                    break
                temp[i] = n
            if not exit_status:
                cur_total = min(cur_total, s[i + 1] + self.shoppingOffers(price, special, temp))
        
        self.cache[tuple(needs)] = cur_total
        return cur_total

def main():
    sol = Solution()
    print(sol.shoppingOffers([2,2], [[1,1,1],[1,1,2],[1,1,3],[1,1,4],[1,1,5],[1,1,6],[1,1,7],[1,1,8],[1,1,9],[1,1,10],[1,1,11],[1,1,12],[1,1,13],[1,1,14],[1,1,15]], [10, 10]))
    print(sol.shoppingOffers([6,3,6,9,4,7], [[1,2,5,3,0,4,29],[3,1,3,0,2,2,19]], [4,1,5,2,2,4]))
    print(sol.shoppingOffers([1,1,1], [[1,1,1,0],[2,2,1,1]], [1,1,0]))
    print(sol.shoppingOffers(price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]))
    print(sol.shoppingOffers(price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]))

if __name__ == '__main__':
    main()