from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def helper(res: List[int], index: int, used: List[bool]):
            if index >= len(res):
                return True
            
            if res[index] != 0:
                return helper(res, index + 1, used)
            else:
                for i in range(n, 0, -1):
                    if used[i]:
                        continue
                    
                    used[i] = True
                    res[index] = i

                    if i == 1:
                        if helper(res, index + 1, used):
                            return True
                    elif (index + i < len(res) and res[index + i] == 0):
                        res[i + index] = i
                        if helper(res, index + 1, used):
                            return True
                        res[index + i] = 0
                    
                    res[index] = 0
                    used[i] = False
            
            return False
        
        res = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        helper(res, 0, used)
        return res
        
def main():
    sol = Solution()
    print(sol.constructDistancedSequence(3))
    print(sol.constructDistancedSequence(5))

if __name__ == '__main__':
    main()