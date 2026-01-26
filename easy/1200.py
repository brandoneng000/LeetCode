from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        res = []
        min_diff = 1000000

        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                res = [[arr[i], arr[i + 1]]]
                min_diff = diff
            elif diff == min_diff:
                res.append([arr[i], arr[i + 1]])
        
        return res


    # def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    #     import heapq
    #     heapq.heapify(arr)
    #     result = []
    #     min_distance = float('inf')
    #     a = heapq.heappop(arr)
        
    #     while arr:
    #         b = heapq.heappop(arr)
    #         distance = b - a
    #         if distance < min_distance:
    #             result.clear()
    #             result.append([a, b])
    #             min_distance = distance
    #         elif distance == min_distance:
    #             result.append([a,b])
            
    #         a = b
        
    #     return result


def main():
    sol = Solution()
    print(sol.minimumAbsDifference([4,2,1,3]))
    print(sol.minimumAbsDifference([1,3,6,10,15]))
    print(sol.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))

if __name__ == '__main__':
    main()