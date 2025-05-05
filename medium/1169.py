from typing import List
from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # name, time(minutes), amount, city
        users = defaultdict(list)
        res = set()

        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            users[name].append([int(time), int(amount), city, i])
        
        for name in users:
            users[name].sort()
            n = len(users[name])
            left = 0

            for right in range(n):
                if users[name][right][1] > 1000:
                    res.add(users[name][right][3])
                
                while left < right and users[name][right][0] - users[name][left][0] > 60:
                    left += 1
                
                if left != right:
                    temp = set()
                    cities = set()

                    for i in range(left, right + 1):
                        cities.add(users[name][i][2])
                        temp.add(users[name][i][3])

                    if len(cities) != 1:
                        res |= temp
            

        return [transactions[i] for i in res]

        
def main():
    sol = Solution()
    print(sol.invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,100,beijing"]))
    print(sol.invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]))
    print(sol.invalidTransactions(transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]))

if __name__ == '__main__':
    main()