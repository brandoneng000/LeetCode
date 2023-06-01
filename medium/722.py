from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        block_comment = False
        for line in source:
            if not block_comment:
                code = ""
            index, end = 0, len(line)
            while index < end:
                if block_comment:
                    if line[index: index + 2] == '*/' and index + 1 < end:
                        index += 2
                        block_comment = False
                        continue
                    index += 1
                else:
                    if line[index: index + 2] == '/*' and index + 1 < end:
                        index += 2
                        block_comment = True
                        continue
                    if line[index: index + 2] == '//' and index + 1 < end:
                        break
                    code += line[index]
                    index += 1
            if code and not block_comment:
                res.append(code)
            
        return res

def main():
    sol = Solution()
    print(sol.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
    print(sol.removeComments(["a/*comment", "line", "more_comment*/b"]))

if __name__ == '__main__':
    main()