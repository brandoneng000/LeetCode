from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        max_capture = 0
        j = 0

        for index, fort in enumerate(forts):
            if fort:
                if forts[j] == -fort:
                    max_capture = max(max_capture, index - j - 1)
                j = index
        
        return max_capture
        

def main():
    sol = Solution()
    print(sol.captureForts([1,0,0,-1,0,0,0,0,1]))
    print(sol.captureForts([0,0,1,-1]))

if __name__ == '__main__':
    main()