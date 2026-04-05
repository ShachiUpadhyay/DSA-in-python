#https://neetcode.io/problems/non-overlapping-intervals/question

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        count : int =0

        prev = intervals[0]
        i : int = 1

        while i<len(intervals):
            if prev[1]<=intervals[i][0]:
                prev = intervals[i]
                i += 1
            else:
                if prev[1]>intervals[i][1]:
                    prev = intervals[i]
                i += 1
                count += 1
        
        return count


