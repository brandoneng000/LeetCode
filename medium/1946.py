from typing import List

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        n = len(num)
        res = list(num)
        mutated = False
        change_str = [str(change[i]) for i in range(len(change))]

        for i in range(n):
            if res[i] < change_str[int(res[i])]:
                mutated = True
            
            if mutated:
                if res[i] <= change_str[int(res[i])]:
                    res[i] = change_str[int(res[i])]
                else:
                    break
        
        return ''.join(res)
        
def main():
    sol = Solution()
    print(sol.maximumNumber(num = "132", change = [9,8,5,0,3,6,4,2,6,8]))
    print(sol.maximumNumber(num = "021", change = [9,4,3,5,7,2,1,9,0,6]))
    print(sol.maximumNumber(num = "5", change = [1,4,7,5,3,2,5,6,9,4]))

if __name__ == '__main__':
    main()