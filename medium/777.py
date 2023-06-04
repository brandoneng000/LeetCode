class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        size = len(start)
        start_l = [i for i in range(size) if start[i] == 'L']
        end_l = [i for i in range(size) if end[i] == 'L']

        start_r = [i for i in range(size) if start[i] == 'R']
        end_r = [i for i in range(size) if end[i] == 'R']

        for i, j in zip(start_l, end_l):
            if i < j:
                return False
            
        for i, j in zip(start_r, end_r):
            if i > j:
                return False
            
        return True

def main():
    sol = Solution()
    print(sol.canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX"))
    print(sol.canTransform(start = "X", end = "L"))

if __name__ == '__main__':
    main()