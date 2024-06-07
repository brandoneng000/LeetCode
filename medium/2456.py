from typing import List

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        popularity = {}
        most_popular = {}

        for c, id, v in zip(creators, ids, views):
            popularity[c] = popularity.get(c, 0) + v
            if most_popular.get(c, [0, "zzzzzzzz"])[0] == v:
                most_popular[c] = (v, min(most_popular.get(c, [0, "zzzzzzzz"])[1], id))
            elif most_popular.get(c, [0, "zzzzzzzz"])[0] < v:
                most_popular[c] = (v, id)
        
        max_popular = max(popularity.values())

        return [[c, most_popular[c][1]] for c in popularity if popularity[c] == max_popular]

        
def main():
    sol = Solution()
    print(sol.mostPopularCreator(creators = ["a"], ids = ["a"], views = [0]))
    print(sol.mostPopularCreator(creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]))
    print(sol.mostPopularCreator(creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]))

if __name__ == '__main__':
    main()