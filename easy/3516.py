class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist_xz = abs(x - z)
        dist_yz = abs(y - z)

        if dist_xz == dist_yz:
            return 0
        elif dist_xz > dist_yz:
            return 2
        else:
            return 1
        
def main():
    sol = Solution()
    print(sol.findClosest(x = 2, y = 7, z = 4))
    print(sol.findClosest(x = 2, y = 5, z = 6))
    print(sol.findClosest(x = 1, y = 5, z = 3))

if __name__ == '__main__':
    main()