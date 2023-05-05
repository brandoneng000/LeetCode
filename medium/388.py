class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res = 0
        input = input.split('\n')
        stack = []
        
        for file_dir in input:
            tab_count = file_dir.count('\t')
            while len(stack) >= tab_count + 1:
                stack.pop()
            
            stack.append(file_dir.replace('\t', ''))
            
            if '.' in file_dir:
                res = max(res, len("/".join(stack)))

        return res

def main():
    sol = Solution()
    print(sol.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
    print(sol.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
    print(sol.lengthLongestPath("a"))
    print(sol.lengthLongestPath("a\n\tb1\n\t\tf1.txt\n\taaaaa\n\t\tf2.txt"))

if __name__ == '__main__':
    main()