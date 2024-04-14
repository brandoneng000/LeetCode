class Solution:
    def minimizeResult(self, expression: str) -> str:
        res = '(' + expression + ')'
        lowest_min = eval(expression)

        left, right = expression.split('+')
        left_side = ['(' + left]
        right_side = [right + ')']
        
        for i in range(1, len(left)):
            left_side.append(left[:i] + "*(" + left[i:])
        
        for i in range(1, len(right)):
            right_side.append(right[:i] + ')*' + right[i:])
        
        for l in left_side:
            for r in right_side:
                cur_exp = '+'.join([l, r])
                cur = eval(cur_exp)
                
                if cur < lowest_min:
                    res = cur_exp
                    lowest_min = cur

        return res.replace('*', '')

def main():
    sol = Solution()
    print(sol.minimizeResult("247+38"))
    print(sol.minimizeResult("12+34"))
    print(sol.minimizeResult("999+999"))

if __name__ == '__main__':
    main()