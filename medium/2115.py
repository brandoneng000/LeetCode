from typing import List
from collections import deque, defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        supply = set(supplies)
        recipe_to_index = { recipe: index for index, recipe in enumerate(recipes) }
        dependency_graph = defaultdict(list)
        in_degree = [0] * n

        for recipe_index, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                if ingredient not in supply:
                    dependency_graph[ingredient].append(recipes[recipe_index])
                    in_degree[recipe_index] += 1
        
        q = deque(index for index, count in enumerate(in_degree) if count == 0)
        created_recipes = []

        while q:
            recipe_index = q.popleft()
            recipe = recipes[recipe_index]
            created_recipes.append(recipe)

            for dependent_recipe in dependency_graph[recipe]:
                in_degree[recipe_to_index[dependent_recipe]] -= 1

                if in_degree[recipe_to_index[dependent_recipe]] == 0:
                    q.append(recipe_to_index[dependent_recipe])
        
        return created_recipes


    # def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    #     n = len(recipes)

    #     q = deque(range(n))
    #     supply = set(supplies)
    #     created_recipe = []
    #     last_size = -1

    #     while len(supply) > last_size:
    #         last_size = len(supply)
    #         size = len(q)

    #         while size > 0:
    #             size -= 1
    #             recipe_index = q.popleft()

    #             if all(ingredient in supply for ingredient in ingredients[recipe_index]):
    #                 supply.add(recipes[recipe_index])
    #                 created_recipe.append(recipes[recipe_index])
    #             else:
    #                 q.append(recipe_index)
            
    #     return created_recipe

    # def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    #     n = len(recipes)
    #     supply = set(supplies)
    #     res = set()
    #     q = deque(range(n))

    #     while q:
    #         cur = q.popleft()

    #         if recipes[cur] in res:
    #             continue

    #         if not (set(ingredients[cur]) - supply):
    #             supply.add(recipes[cur])
    #             res.add(recipes[cur])
    #             q = deque(range(n))

    #     return list(res)


        
def main():
    sol = Solution()
    print(sol.findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]))
    print(sol.findAllRecipes(recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]))
    print(sol.findAllRecipes( ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]))

if __name__ == '__main__':
    main()