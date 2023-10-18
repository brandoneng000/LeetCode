from typing import List
import collections
import heapq

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        prereqs = collections.defaultdict(set)
        in_degree = [0] * n

        for prev_course, next_course in relations:
            prereqs[prev_course - 1].add(next_course - 1)
            in_degree[next_course - 1] += 1
        
        q = collections.deque()
        max_time = [0] * n

        for course in range(n):
            if in_degree[course] == 0:
                q.append(course)
                max_time[course] = time[course]
        
        while q:
            course = q.popleft()

            for next_course in prereqs[course]:
                max_time[next_course] = max(max_time[next_course], max_time[course] + time[next_course])
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)

        return max(max_time)
        

    # def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
    #     prereqs = collections.defaultdict(set)
    #     completed = {}

    #     for prev_course, next_course in relations:
    #         prereqs[next_course].add(prev_course)

    #     for course in range(1, n + 1):
    #         if course not in prereqs:
    #             completed[course] = time[course - 1]
        
    #     while len(completed) < n:
    #         for course in prereqs:
    #             cur_time = 0
    #             if course in completed:
    #                 continue
    #             for pre in prereqs[course]:
    #                 if completed.get(pre, -1) == -1:
    #                     break
    #                 cur_time = max(cur_time, completed[pre])
    #             else:
    #                 completed[course] = cur_time + time[course - 1]
        
    #     return max(completed.values())

    # def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
    #     prereqs = collections.defaultdict(set)
    #     completed = set()
    #     heap = []

    #     for prev_course, next_course in relations:
    #         prereqs[next_course].add(prev_course)

    #     for course in range(1, n + 1):
    #         if course not in prereqs:
    #             heapq.heappush(heap, (time[course - 1], course))

    #     while heap:
    #         cur_time, course = heapq.heappop(heap)
    #         completed.add(course)

    #         while heap and heap[0][0] == cur_time:
    #             cur_time, course = heapq.heappop(heap)
    #             completed.add(course)
            
    #         remove_course = set()
    #         for course in prereqs:
    #             if not prereqs[course] - completed:
    #                 remove_course.add(course)
    #                 heapq.heappush(heap, (cur_time + time[course - 1], course))
            
    #         for course in remove_course:
    #             prereqs.pop(course)

    #     return cur_time
        
def main():
    sol = Solution()
    print(sol.minimumTime(n = 3, relations = [[1,3],[2,3]], time = [3,2,5]))
    print(sol.minimumTime(n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]))

if __name__ == '__main__':
    main()