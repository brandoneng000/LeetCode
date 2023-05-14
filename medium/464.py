class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        cache = {}

        def can_win(choices, remainder):
            if choices[-1] >= remainder:
                return True
            
            seen = tuple(choices)
            if seen in cache:
                return cache[seen]
            
            for index in range(len(choices)):
                if not can_win(choices[: index] + choices[index + 1:], remainder - choices[index]):
                    cache[seen] = True
                    return True
            
            cache[seen] = False
            return False

        sum_choices = (maxChoosableInteger + 1) * maxChoosableInteger / 2
        if sum_choices < desiredTotal:
            return False
        
        if sum_choices == desiredTotal:
            return maxChoosableInteger % 2
        
        choices = list(range(1, maxChoosableInteger + 1))
        return can_win(choices, desiredTotal)

def main():
    sol = Solution()
    print(sol.canIWin(maxChoosableInteger = 10, desiredTotal = 11))
    print(sol.canIWin(maxChoosableInteger = 10, desiredTotal = 0))
    print(sol.canIWin(maxChoosableInteger = 10, desiredTotal = 1))
    print(sol.canIWin(maxChoosableInteger = 10, desiredTotal = 300))

if __name__ == '__main__':
    main()