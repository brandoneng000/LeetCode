from typing import List
import collections

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = set()
        food = collections.defaultdict(collections.Counter)

        for p, n, f in orders:
            food[f][int(n)] += 1
            table.add(int(n))
        
        food_items = sorted(food)
        res = [["Table"] + food_items]

        for n in sorted(table):
            cur = [str(n)]
            for f in food_items:
                cur.append(str(food[f][n]))
            res.append(cur)

        return res

def main():
    sol = Solution()
    print(sol.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))
    print(sol.displayTable([["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]))
    print(sol.displayTable([["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]))

if __name__ == '__main__':
    main()