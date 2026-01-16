from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def get_gaps(fences: List[int], limit: int):
            fences = sorted([1] + fences + [limit])
            gaps = set()

            for i in range(len(fences)):
                for j in range(i + 1, len(fences)):
                    gaps.add(fences[j] - fences[i])
            
            return gaps
        
        mod = 1_000_000_007
        h_dist = get_gaps(hFences, m)
        v_dist = get_gaps(vFences, n)

        common = h_dist & v_dist

        if not common:
            return -1

        max_side = max(common)
        return (max_side * max_side) % mod


    # def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
    #     mod = 1000000007
    #     hFences.extend([1, m])
    #     vFences.extend([1, n])
    #     hFences.sort()
    #     vFences.sort()
    #     h_dist = set()
    #     v_dist = set()

    #     for i in range(len(hFences)):
    #         for j in range(i + 1, len(hFences)):
    #             h_dist.add(hFences[j] - hFences[i])
        
    #     for i in range(len(vFences)):
    #         for j in range(i + 1, len(vFences)):
    #             v_dist.add(vFences[j] - vFences[i])

    #     return (max(h_dist & v_dist) ** 2) % mod if h_dist & v_dist else -1 



        
def main():
    sol = Solution()
    print(sol.maximizeSquareArea(m = 4, n = 3, hFences = [2,3], vFences = [2]))
    print(sol.maximizeSquareArea(m = 6, n = 7, hFences = [2], vFences = [4]))

if __name__ == '__main__':
    main()