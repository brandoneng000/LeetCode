from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = []

        if k > 0:
            left = 1
            right = k + 1
            cur_sum = sum(code[left:right])
        elif k < 0:
            left = k
            right = 0
            cur_sum = sum(code[left:])
        else:
            return [0] * n

        for _ in range(n):
            res.append(cur_sum)
            cur_sum -= code[left % n]
            cur_sum += code[right % n]
            left += 1
            right += 1

        return res

    # def decrypt(self, code: List[int], k: int) -> List[int]:
    #     result = []
    #     end = len(code)
        
    #     if k == 0:
    #         return [0] * len(code)
    #     if k > 0:
    #         code += code[:k]
    #         for index in range(end):
    #             temp = 0
    #             for i in range(1, k + 1):
    #                 temp += code[i + index]
    #             result.append(temp)
    #     else:
    #         for index in range(end):
    #             temp = 0
    #             for i in range(k, 0):
    #                 temp += code[i + index]
    #             result.append(temp)

    #     return result

def main():
    sol = Solution()
    print(sol.decrypt(code = [5,7,1,4], k = 3))
    print(sol.decrypt(code = [1,2,3,4], k = 0))
    print(sol.decrypt(code = [2,4,9,3], k = -2))

if __name__ == '__main__':
    main()