from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        res = []
        bracket = False

        for key, word in knowledge:
            s = s.replace('(' + key + ')', word)

        for c in s:
            if c == '(':
                bracket = True
                res.append('?')
            elif c == ')':
                bracket = False
                continue

            if not bracket:
                res.append(c)
            
        return ''.join(res)

    # def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
    #     knowledge_dict = {}
    #     stack = []
    #     res = []

    #     for k, v in knowledge:
    #         knowledge_dict[k] = v
        
    #     for c in s:
    #         if stack:
    #             stack.append(c)
    #         else:
    #             if c == '(':
    #                 stack.append(c)
    #             else:
    #                 res.append(c)
            
    #         if stack and stack[-1] == ')':
    #             key = ''.join(stack[1:-1])
    #             stack.clear()
    #             res.append(knowledge_dict.get(key, '?'))

    #     return "".join(res)
        
def main():
    sol = Solution()
    print(sol.evaluate(s = "(name) is (age) years old", knowledge = [["name","bob"],["age","two"]]))
    print(sol.evaluate(s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]))
    print(sol.evaluate(s = "hi(name)", knowledge = [["a","b"]]))
    print(sol.evaluate(s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]))

if __name__ == '__main__':
    main()