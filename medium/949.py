from typing import List

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        self.res = ""

        def generate_pairs(cur: List[int], index: int):
            if len(cur) == 2:
                hours1 = f"{arr[cur[0]]}{arr[cur[1]]}"
                hours2 = f"{arr[cur[1]]}{arr[cur[0]]}"
                min_index = [i for i in range(len(arr)) if i not in cur]
                minutes1 = f"{arr[min_index[0]]}{arr[min_index[1]]}"
                minutes2 = f"{arr[min_index[1]]}{arr[min_index[0]]}"
                if not (0 <= int(hours1) < 24):
                    hours1 = ""
                if not (0 <= int(hours2) < 24):
                    hours2 = ""
                if not (0 <= int(minutes1) < 60):
                    minutes1 = ""
                if not (0 <= int(minutes2) < 60):
                    minutes2 = ""
                if (not hours1 and not hours2) or (not minutes1 and not minutes2):
                    return
                self.res = max(self.res, f"{max(hours1, hours2)}:{max(minutes1, minutes2)}")
            
            for i in range(index, len(arr)):
                cur.append(i)
                generate_pairs(cur, i + 1)
                cur.pop()
        
        generate_pairs([], 0)
        return self.res

def main():
    sol = Solution()
    print(sol.largestTimeFromDigits([1,2,3,4]))
    print(sol.largestTimeFromDigits([5,5,5,5]))

if __name__ == '__main__':
    main()