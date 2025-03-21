from typing import List
from collections import deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)
        
        ingredient_to_recipes = {}
        for recipe, ing_list in zip(recipes, ingredients):
            for ing in ing_list:
                if ing not in ingredient_to_recipes:
                    ingredient_to_recipes[ing] = []
                ingredient_to_recipes[ing].append(recipe)
        
        in_degree = {}
        for recipe, ing_list in zip(recipes, ingredients):
            missing = [ing for ing in ing_list if ing not in available]
            in_degree[recipe] = len(missing)
        
        queue = deque()
        for recipe in recipes:
            if in_degree[recipe] == 0:  
                queue.append(recipe)
        
        res = []
        
        while queue:
            recipe = queue.popleft()
            res.append(recipe)  
            available.add(recipe)   
            
            if recipe in ingredient_to_recipes:
                for dependent_recipe in ingredient_to_recipes[recipe]:
                    in_degree[dependent_recipe] -= 1  
                    if in_degree[dependent_recipe] == 0:  
                        queue.append(dependent_recipe)
        
        return res

sol = Solution()
print(sol.findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]))
print(sol.findAllRecipes(recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]))
print(sol.findAllRecipes(recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]))