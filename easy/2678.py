from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(detail[11: 13]) > 60 for detail in details)

    # def countSeniors(self, details: List[str]) -> int:
    #     res = 0

    #     for detail in details:
    #         res += int(detail[11: 13]) > 60

    #     return res
        
def main():
    sol = Solution()
    print(sol.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))
    print(sol.countSeniors(["1313579440F2036","2921522980M5644"]))

if __name__ == '__main__':
    main()