from typing import List
from collections import deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        supply = set(supplies)
        res = set()
        q = deque(range(n))

        while q:
            cur = q.popleft()

            if recipes[cur] in res:
                continue

            if not (set(ingredients[cur]) - supply):
                supply.add(recipes[cur])
                res.add(recipes[cur])
                q = deque(range(n))

        return list(res)


        
def main():
    sol = Solution()
    print(sol.findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]))
    print(sol.findAllRecipes(recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]))
    print(sol.findAllRecipes( ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]))

if __name__ == '__main__':
    main()