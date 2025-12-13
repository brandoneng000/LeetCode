from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def check_code(code: str):
            for c in code:
                if not c.isalnum() and c != '_':
                    return False
                    
            return True

        business_category = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        res = []

        for c, business, active in zip(code, businessLine, isActive):
            if c and check_code(c) and business in business_category and active:
                res.append((c, business))
        
        return [c for c, b in sorted(res, key=lambda x: (business_category[x[1]], x[0]))]


        
def main():
    sol = Solution()
    print(sol.validateCoupons(code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [True,True,True,True]))
    print(sol.validateCoupons(["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [False,True,True]))

if __name__ == '__main__':
    main()