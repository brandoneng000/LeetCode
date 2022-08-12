class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for directory in path:
            if directory == '..':
                if stack:
                    stack.pop()     
            elif directory == '.' or directory == '':
                pass
            else:
                stack.append(directory)


        return '/' + "/".join(stack)

def main():
    sol = Solution()
    print(sol.simplifyPath("/home/"))
    print(sol.simplifyPath("/../"))
    print(sol.simplifyPath("/home//foo/"))
    print(sol.simplifyPath("/home/duck/../asdf"))
    print(sol.simplifyPath("/home/duck/./asdf"))

if __name__ == '__main__':
    main()