class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        res = left = right = 0

        for m in moves:
            if m == 'L':
                left += 1
            elif m == 'R':
                right += 1
            else:
                res += 1
        
        return abs(left - right) + res

    # def furthestDistanceFromOrigin(self, moves: str) -> int:
    #     return abs(moves.count('L') - moves.count('R')) + moves.count('_')

    # def furthestDistanceFromOrigin(self, moves: str) -> int:
    #     blank = left = right = 0

    #     for d in moves:
    #         if d == 'R':
    #             right += 1
    #         elif d == 'L':
    #             left += 1
    #         else:
    #             blank += 1
        
    #     if left > right:
    #         return left - right + blank
    #     else:
    #         return right - left + blank
        
def main():
    sol = Solution()
    print(sol.furthestDistanceFromOrigin("L_RL__R"))
    print(sol.furthestDistanceFromOrigin("_R__LL_"))
    print(sol.furthestDistanceFromOrigin("_______"))

if __name__ == '__main__':
    main()