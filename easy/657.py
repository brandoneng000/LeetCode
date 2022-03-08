class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from typing import Counter
        counter = Counter(moves)
        return counter['U'] == counter['D'] and counter['L'] == counter['R']

def main():
    sol = Solution()
    print(sol.judgeCircle("UD"))

if __name__ == '__main__':
    main()