class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # preorder = preorder.split(',')
        # if preorder[0] == '#': 
        #     return len(preorder) == 1
        
        # left_and_right = 2
        # branch_stack = []
        # tree_stack = [preorder[0]]

        # for val in preorder[1:]:
        #     if not tree_stack:
        #         return False
        #     if val.isdigit():
        #         left_and_right -= 1
        #         tree_stack.append(val)
        #         branch_stack.append(left_and_right)
        #         left_and_right = 2
        #     elif val == '#':
        #         left_and_right -= 1
            
        #     while left_and_right == 0 and tree_stack:
        #         tree_stack.pop()
        #         if branch_stack:
        #             left_and_right = branch_stack.pop()
            
        # return not tree_stack
        preorder = preorder.split(',')
        none_count = 1
        for val in preorder:
            if none_count == 0:
                return False
            
            if val == '#':
                none_count -= 1
            else:
                none_count += 1

        return none_count == 0

        

def main():
    sol = Solution()
    print(sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
    print(sol.isValidSerialization("1,#"))
    print(sol.isValidSerialization("9,#,#,1"))
    print(sol.isValidSerialization("1,#,#,#,#"))
    print(sol.isValidSerialization("#,#,#"))

if __name__ == '__main__':
    main()