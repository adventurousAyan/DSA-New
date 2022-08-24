from typing import List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        def dfs(receipe, seen):

            # If receipe in supplies, return True
            if receipe in visited:
                return True

            # If receipe is already seen , return False
            if receipe in seen:
                return False

            # Add the recipe to seen
            seen.add(receipe)

            # Get the ingredients
            ingreds = d1.get(receipe, [])
            # If there are no ingredients
            if len(ingreds) == 0:
                return False
            # For each ingredient, do dfs
            for ingred in ingreds:
                if not dfs(ingred, seen):
                    return False

            # Add to the supply set
            visited.add(receipe)
            return True

        n = len(recipes)
        ls = []
        visited = set(supplies)
        d1 = {}

        # Make the map
        for i in range(n):
            d1[recipes[i]] = ingredients[i]

        # For each recipes fo dfs, take a seen array
        for receipe in d1:
            if dfs(receipe, set()):
                ls.append(receipe)
        return ls
