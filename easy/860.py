from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tens = 0
        fives = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10 and fives > 0:
                fives -= 1
                tens += 1
            elif bill == 20 and fives > 0 and tens > 0:
                fives -= 1
                tens -= 1
            elif bill == 20 and fives > 2:
                fives -= 3
            else:
                return False
        
        return True

    # def lemonadeChange(self, bills: List[int]) -> bool:
    #     money = { 5: 0, 10: 0 }
        
    #     for bill in bills:
    #         if bill == 5:
    #             money[bill] += 1
    #         elif bill == 10:
    #             if money[5]:
    #                 money[5] -= 1
    #                 money[10] += 1
    #             else:
    #                 return False
    #         else:
    #             if money[10] and money[5]:
    #                 money[10] -= 1
    #                 money[5] -= 1
    #             elif money[5] >= 3:
    #                 money[5] -= 3
    #             else:
    #                 return False
        
    #     return True

def main():
    sol = Solution()
    print(sol.lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]))
    print(sol.lemonadeChange([5,5,5,10,20]))
    print(sol.lemonadeChange([5,5,10,10,20]))

if __name__ == '__main__':
    main()