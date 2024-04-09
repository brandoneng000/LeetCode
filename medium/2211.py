class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        left, right = 0, n - 1

        while left < n and directions[left] == 'L':
            left += 1
        
        while right > -1 and directions[right] == 'R':
            right -= 1
        
        res = 0
        for i in range(left, right + 1):
            if directions[i] != 'S':
                res += 1

        return res

        
def main():
    sol = Solution()
    print(sol.countCollisions("LRLRLRLRLRLRLRLRLRRLRLLRLLRLRLLRLRLR"))
    print(sol.countCollisions("RLRSLL"))
    print(sol.countCollisions("LLRR"))

if __name__ == '__main__':
    main()