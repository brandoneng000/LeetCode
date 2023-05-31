from typing import List
import collections

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(index: int, emails: set()):
            if visited[index]:
                return
            visited[index] = True
            for j in range(1, len(accounts[index])):
                email = accounts[index][j]
                emails.add(email)
                for adj in emails_accounts[email]:
                    dfs(adj, emails)
        
        visited = [False] * len(accounts)
        emails_accounts = collections.defaultdict(list)
        res = []

        for i, user in enumerate(accounts):
            for j in range(1, len(user)):
                email = user[j]
                emails_accounts[email].append(i)
        
        for i, user in enumerate(accounts):
            if visited[i]:
                continue
            name = user[0]
            emails = set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res
                

def main():
    sol = Solution()
    print(sol.accountsMerge([["David","David0@m.co","David1@m.co"],
                             ["David","David3@m.co","David4@m.co"],
                             ["David","David4@m.co","David5@m.co"],
                             ["David","David2@m.co","David3@m.co"],
                             ["David","David1@m.co","David2@m.co"]]))
    print(sol.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],
                             ["John","johnsmith@mail.com","john00@mail.com"],
                             ["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
    print(sol.accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
                             ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
                             ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
                             ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
                             ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]))

if __name__ == '__main__':
    main()