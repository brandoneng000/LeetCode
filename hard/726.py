from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        stack = [Counter()]
        i = 0
        cur_val = 0
        cur_ele = '1'

        while i < n:
            val = formula[i]

            if val.isdigit():
                cur_val = cur_val * 10 + int(val)
            elif val.islower():
                cur_ele += val
            elif val.isupper():
                if cur_ele:
                    stack[-1][cur_ele] += cur_val or 1
                cur_ele = val
                cur_val = 0
            elif val == '(':
                if cur_ele:
                    stack[-1][cur_ele] += cur_val or 1

                stack.append(Counter())
                cur_ele = ''
                cur_val = 0
            elif val == ')':
                if cur_ele:
                    stack[-1][cur_ele] += cur_val or 1
                cur_ele = ''
                cur_val = 0

                multiplier = 0
                while i + 1 < n and formula[i + 1].isdigit():
                    i += 1
                    multiplier = multiplier * 10 + int(formula[i])
                temp = stack.pop()

                if multiplier:
                    for element in temp:
                        temp[element] *= multiplier
                
                stack[-1].update(temp)

            i += 1
        
        if cur_ele:
            stack[-1][cur_ele] += cur_val or 1

        stack[-1].pop('1')

        return ''.join([element + (str(stack[-1][element]) if stack[-1][element] > 1 else '') for element in sorted(stack[-1])])
        
def main():
    sol = Solution()
    print(sol.countOfAtoms("((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"))
    print(sol.countOfAtoms("((HHe28Be26He)9)34"))
    print(sol.countOfAtoms("H2O"))
    print(sol.countOfAtoms("Mg(OH)2"))
    print(sol.countOfAtoms("K4(ON(SO3)2)2"))

if __name__ == '__main__':
    main()