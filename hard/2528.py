from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        def check(val: int):
            diff = count[::]
            total = 0
            remaining = k

            for i in range(n):
                total += diff[i]

                if total < val:
                    add = val - total

                    if remaining < add:
                        return False
                    
                    remaining -= add
                    end = min(n, i + 2  * r + 1)
                    diff[end] -= add
                    total += add
            
            return True

        n = len(stations)
        count = [0] * (n + 1)

        for i in range(n):
            left = max(0, i - r)
            right = min(n, i + r + 1)
            count[left] += stations[i]
            count[right] -= stations[i]
        
        left = min(stations)
        right = sum(stations) + k
        res = 0

        while left <= right:
            middle = (left + right) // 2
            if check(middle):
                res = middle
                left = middle + 1
            else:
                right = middle - 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxPower(stations = [1,2,4,5,0], r = 1, k = 2))
    print(sol.maxPower(stations = [4,4,4,4], r = 0, k = 3))

if __name__ == '__main__':
    main()