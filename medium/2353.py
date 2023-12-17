from typing import List
from heapq import heappush, heappop
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating = defaultdict(int)
        self.food_cuisine = {}
        self.cuisine_rating = defaultdict(list)

        for i in range(len(foods)):
            self.food_cuisine[foods[i]] = cuisines[i]
            heappush(self.cuisine_rating[cuisines[i]], (-ratings[i], foods[i]))
            self.food_rating[foods[i]] = -ratings[i]
        

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = -newRating
        heappush(self.cuisine_rating[self.food_cuisine[food]], (-newRating, food))
        

    def highestRated(self, cuisine: str) -> str:
        while self.cuisine_rating[cuisine] and self.food_rating[self.cuisine_rating[cuisine][0][1]] != self.cuisine_rating[cuisine][0][0]:
            heappop(self.cuisine_rating[cuisine])
        
        return self.cuisine_rating[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)