class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cur_pen = min_pen = customers.count('Y')
        res = 0

        for i, c in enumerate(customers):
            if c == 'Y':
                cur_pen -= 1
            else:
                cur_pen += 1
            
            if cur_pen < min_pen:
                res = i + 1
                min_pen = cur_pen
        
        return res

def main():
    sol = Solution()
    print(sol.bestClosingTime("YYNY"))
    print(sol.bestClosingTime("NNNNN"))
    print(sol.bestClosingTime("YYYY"))

if __name__ == '__main__':
    main()