from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        largest_population = 0
        cur_population = 0
        year = 1950
        death = []
        logs.sort()

        for log in logs:
            while death and log[0] >= death[0]:
                death.pop(0)
                cur_population -= 1
            death.append(log[1])
            death.sort()
            cur_population += 1
            if cur_population > largest_population:
                largest_population = cur_population
                year = log[0]
        
        return year

            

def main():
    sol = Solution()
    print(sol.maximumPopulation([[1993,1999],[2000,2010]]))
    print(sol.maximumPopulation([[1950,1961],[1960,1971],[1970,1981]]))
    print(sol.maximumPopulation([[2033,2034],[2039,2047],[1998,2042],[2047,2048],[2025,2029],[2005,2044],[1990,1992],[1952,1956],[1984,2014]]))

if __name__ == '__main__':
    main()