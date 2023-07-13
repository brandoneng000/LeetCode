from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clip_ends = {}

        for start, end in clips:
            clip_ends[start] = max(clip_ends.get(start, 0), end)
        
        cur_end = -1
        final_end = 0
        res = 0

        for i in range(time + 1):
            if i > final_end:
                break
            final_end = max(final_end, clip_ends.get(i, 0))
            if i >= cur_end:
                res += 1
                cur_end = final_end
                if cur_end >= time:
                    return res
                
        return -1


    # def videoStitching(self, clips: List[List[int]], time: int) -> int:
    #     clips.sort()
    #     end, end2, res = -1, 0, 0

    #     for i, j in clips:
    #         if end2 >= time or i > end2:
    #             break
    #         elif end < i <= end2:
    #             res, end = res + 1, end2
    #         end2 = max(end2, j)
        
    #     return res if end2 >= time else -1
        
            

def main():
    sol = Solution()
    print(sol.videoStitching(clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10))
    print(sol.videoStitching(clips = [[0,1],[1,2]], time = 5))
    print(sol.videoStitching(clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9))

if __name__ == '__main__':
    main()