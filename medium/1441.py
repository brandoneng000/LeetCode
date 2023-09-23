from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        index = 0

        for i in range(1, n + 1):
            res.append("Push")
            if i == target[index]:
                index += 1
            else:
                res.append("Pop")
            
            if index == len(target):
                break
        
        return res

def main():
    sol = Solution()
    print(sol.buildArray(target = [1,3], n = 3))
    print(sol.buildArray(target = [1,2,3], n = 3))
    print(sol.buildArray(target = [1,2], n = 4))

if __name__ == '__main__':
    main()