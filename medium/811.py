from typing import List
import collections

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = collections.defaultdict(int)
        for cpdomain in cpdomains:
            visits, domain = cpdomain.split()
            visits = int(visits)
            domain = domain.split('.')
            for i in range(len(domain) - 1, -1, -1):
                d = ".".join(domain[i:])
                domains[d] += visits
        
        return [f'{domains[d]} {d}' for d in domains]
                

def main():
    sol = Solution()
    print(sol.subdomainVisits(["9001 discuss.leetcode.com"]))
    print(sol.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))

if __name__ == '__main__':
    main()