class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def expr() -> set:
            nonlocal idx
            res = set()

            while True:
                res |= term()

                if idx < n and expression[idx] == ',':
                    idx += 1
                    continue
                else:
                    break

            return res

        def term() -> set:
            nonlocal idx
            res = {""}

            while idx < n and (expression[idx] == '{' or expression[idx].islower()):
                sub = item()
                tmp = set()

                for left in res:
                    for right in sub:
                        tmp.add(left + right)
                res = tmp

            return res

        def item() -> set:
            nonlocal idx
            res = set()

            if expression[idx] == '{':
                idx += 1
                res = expr()
            else:
                res = {expression[idx]}
            idx += 1

            return res

        n = len(expression)
        idx = 0
        res = expr()

        return sorted(res)

        
def main():
    sol = Solution()
    print(sol.braceExpansionII("{a,b}{c,{d,e}}"))
    print(sol.braceExpansionII("{{a,z},a{b,c},{ab,z}}"))

if __name__ == '__main__':
    main()