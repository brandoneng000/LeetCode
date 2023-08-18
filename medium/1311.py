from typing import List
import collections

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q = collections.deque([id])
        watch_freq = collections.Counter()
        cur_level = 0
        seen = set([id])

        while q and cur_level < level:
            size = len(q)

            for _ in range(size):
                f = q.popleft()

                for acquaintance in friends[f]:
                    if acquaintance not in seen:
                        seen.add(acquaintance)
                        q.append(acquaintance)
            
            cur_level += 1
        
        for person in q:
            for video in watchedVideos[person]:
                watch_freq[video] += 1

        return sorted(watch_freq, key=lambda x: (watch_freq[x], x))

def main():
    sol = Solution()
    print(sol.watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1))
    print(sol.watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2))

if __name__ == '__main__':
    main()