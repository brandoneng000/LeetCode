import collections

class Solution:
    def originalDigits(self, s: str) -> str:
        res = []
        s_count = collections.Counter(s)
        num_words = { 0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 
                     5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
        nums = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        for num in nums:
            temp = collections.Counter(num_words[num])
            s_count_total = sum(s_count.values())

            while s_count and s_count_total - len(num_words[num]) == sum((s_count - temp).values()):
                res.append(str(num))
                s_count -= temp
                s_count_total -= len(num_words[num])
        
        res.sort()
        return "".join(res)
        

def main():
    sol = Solution()
    print(sol.originalDigits("owoztneoer"))
    print(sol.originalDigits("fviefuro"))
    print(sol.originalDigits("zerozero"))

if __name__ == '__main__':
    main()