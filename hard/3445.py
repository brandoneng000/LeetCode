class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def get_status(count_a: int, count_b: int):
            return ((count_a & 1) << 1) | (count_b & 1) 
        
        n = len(s)
        res = -float('inf')

        for a in "01234":
            for b in "01234":
                if a == b:
                    continue

                best = [float('inf')] * 4
                count_a = count_b = 0
                prev_a = prev_b = 0
                left = -1

                for right in range(n):
                    count_a += s[right] == a
                    count_b += s[right] ==  b

                    while right - left >= k and count_b - prev_b >= 2:
                        left_status = get_status(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)
                    
                        left += 1
                        prev_a += s[left] == a
                        prev_b += s[left] == b
                    
                    right_status = get_status(count_a, count_b)

                    if best[right_status ^ 0b10] != float('inf'):
                        res = max(res, count_a - count_b - best[right_status ^ 0b10])
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxDifference(s = "12233", k = 4))
    print(sol.maxDifference(s = "1122211", k = 3))
    print(sol.maxDifference(s = "110", k = 3))

if __name__ == '__main__':
    main()