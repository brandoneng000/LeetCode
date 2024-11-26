from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        res = [0] * k

        for i in range(n):
            res[i % k] = max(res[i % k] + energy[i], energy[i])
        
        return max(res)
        

def main():
    sol = Solution()
    print(sol.maximumEnergy(energy = [5,2,-10,-5,1], k = 3))
    print(sol.maximumEnergy(energy = [-2,-3,-1], k = 2))

if __name__ == '__main__':
    main()