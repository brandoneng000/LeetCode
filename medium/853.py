from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        res = 0
        cur = 0

        for p, s in zip(position, speed):
            stack.append((p, s))
        
        stack.sort()
        time = []
        for p, s in stack:
            time.append((target - p) / s)
        
        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t
        
        
        return res

def main():
    sol = Solution()
    print(sol.carFleet(target = 11, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
    print(sol.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
    print(sol.carFleet(target = 10, position = [3], speed = [3]))
    print(sol.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]))

if __name__ == '__main__':
    main()