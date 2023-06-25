from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_basket = {}
        left = 0

        for right, fruit in enumerate(fruits):
            fruit_basket[fruit] = fruit_basket.get(fruit, 0) + 1

            if len(fruit_basket) > 2:
                fruit_basket[fruits[left]] -= 1
                
                if fruit_basket[fruits[left]] == 0:
                    fruit_basket.pop(fruits[left])
                left += 1
        
        return right - left + 1


def main():
    sol = Solution()
    print(sol.totalFruit([1,2,1]))
    print(sol.totalFruit([0,1,2,2]))
    print(sol.totalFruit([1,2,3,2,2]))

if __name__ == '__main__':
    main()