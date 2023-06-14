from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        for i in range(min(10, len(num))):
            cur = num[:i + 1]
            if cur != '0' and cur.startswith('0'):
                break
            cur = int(cur)
            for j in range(i + 1, min(i + 10, len(num))):
                next = num[i + 1: j + 1]
                if next != '0' and next.startswith('0'):
                    break
                next = int(next)
                fib = [cur, next]
                k = j + 1
                while k < len(num):
                    next_val = fib[-1] + fib[-2]
                    next_str = str(next_val)
                    if next_val <= 2 ** 31 - 1 and num[k:].startswith(next_str):
                        k += len(next_str)
                        fib.append(next_val)
                    else:
                        break
                else:
                    if len(fib) >= 3:
                        return fib
        
        return []


def main():
    sol = Solution()
    print(sol.splitIntoFibonacci("1101111"))
    print(sol.splitIntoFibonacci("112358130"))
    print(sol.splitIntoFibonacci("0123"))

if __name__ == '__main__':
    main()