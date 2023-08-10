from typing import List

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        extra_tomato = tomatoSlices - (2 * cheeseSlices)
        tomatoes = extra_tomato // 2
        cheese = cheeseSlices - tomatoes
        return [tomatoes, cheese] if tomatoes >= 0 and tomatoes % 2 != 1 and cheese >= 0 else []


    # def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
    #     if tomatoSlices % 2 == 1 or 2 * cheeseSlices > tomatoSlices:
    #         return []
        
    #     JUMBO, SMALL = 0, 1
    #     burgers = [0, 0]
        
    #     while 2 * cheeseSlices < tomatoSlices and cheeseSlices > 0 and tomatoSlices > 0:
    #         tomatoSlices -= 4
    #         cheeseSlices -= 1
    #         burgers[JUMBO] += 1
        
    #     if 2 * cheeseSlices == tomatoSlices:
    #         burgers[SMALL] = cheeseSlices
    #     else:
    #         return []

    #     return burgers

def main():
    sol = Solution()
    print(sol.numOfBurgers(tomatoSlices = 16, cheeseSlices = 7))
    print(sol.numOfBurgers(tomatoSlices = 17, cheeseSlices = 4))
    print(sol.numOfBurgers(tomatoSlices = 4, cheeseSlices = 17))

if __name__ == '__main__':
    main()