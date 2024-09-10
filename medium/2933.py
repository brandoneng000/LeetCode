from typing import List
from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        def military_to_min(time: str):
            return int(time[:2]) * 60 + int(time[2:])
        
        employees = defaultdict(list)
        res = []

        for name, access in access_times:
            employees[name].append(military_to_min(access))
        
        for name in employees:
            employees[name].sort()

            for i in range(2, len(employees[name])):
                if employees[name][i] - employees[name][i - 2] < 60:
                    res.append(name)
                    break
        
        return res

        
def main():
    sol = Solution()
    print(sol.findHighAccessEmployees(access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]))
    print(sol.findHighAccessEmployees(access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]))
    print(sol.findHighAccessEmployees(access_times = [["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]))

if __name__ == '__main__':
    main()