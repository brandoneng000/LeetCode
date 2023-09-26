from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res = []
        companies = [[c, i] for i, c in enumerate(favoriteCompanies)]
        companies.sort(key=lambda x: len(x[0]), reverse=True)
        cache = set()
        
        for cur, i in companies:
            c = tuple(cur)

            if not any(set(c).issubset(comp) for comp in cache):
                res.append(i)
                cache.add(c)
        
        return sorted(res)

def main():
    sol = Solution()
    print(sol.peopleIndexes([["aaaa","bbb","ccc"],["aa","bb","cc","dd","ee"]]))
    print(sol.peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))
    print(sol.peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))
    print(sol.peopleIndexes([["leetcode"],["google"],["facebook"],["amazon"]]))

if __name__ == '__main__':
    main()