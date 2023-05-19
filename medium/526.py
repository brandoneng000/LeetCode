from typing import List

class Solution:
    def countArrangement(self, n: int) -> int:
        self.res = 0
        def generate(cur: set):
            if len(cur) == n:
                self.res += 1
                return
            
            for i in range(1, n + 1):
                if i not in cur and (i % (len(cur) + 1) == 0 or ((len(cur) + 1) % i == 0)):
                    cur.add(i)
                    generate(cur)
                    cur.remove(i)

        generate(set())
        return self.res

def main():
    sol = Solution()
    print(sol.countArrangement(7))
    print(sol.countArrangement(10))
    print(sol.countArrangement(15))
    print(sol.countArrangement(5))
    print(sol.countArrangement(2))
    print(sol.countArrangement(1))

if __name__ == '__main__':
    main()