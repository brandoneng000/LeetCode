from typing import List, Dict
import collections
import copy

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = collections.defaultdict(list)

        for start, end in sorted(tickets)[::-1]:
            flights[start].append(end)
        
        route = []

        def visit(airport):
            while flights[airport]:
                visit(flights[airport].pop())
            route.append(airport)
        
        visit('JFK')
        return route[::-1]

    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     def dfs(cur: List[str], flights: Dict):
    #         if len(cur) == n + 1:
    #             return (True, cur)
            
    #         destinations = flights[cur[-1]].copy()

    #         for dest in destinations:
    #             flights[cur[-1]].remove(dest)
    #             complete, trip = dfs(cur + [dest], flights)
                
    #             if complete:
    #                 return (True, trip)
                
    #             flights[cur[-1]].append(dest)

    #         return (False, cur)
        
    #     n = len(tickets)
    #     self.res = []
    #     flights = collections.defaultdict(list)

    #     for origin, dest in tickets:
    #         flights[origin].append(dest)
    #         if dest not in flights:
    #             flights[dest] = []

    #     for start in flights:
    #         flights[start].sort()

    #     return dfs(['JFK'], flights)[1]
        
        

def main():
    sol = Solution()
    print(sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
    print(sol.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))
    print(sol.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
    print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))

if __name__ == '__main__':
    main()