#https://neetcode.io/problems/merge-intervals/question?list=neetcode250

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])

        result: List[List[int]] = []

        curr = intervals[0]

        for i in range(1, len(intervals)):
            if curr[1] < intervals[i][0]:
                result.append(curr)
                curr = intervals[i]   
            else:
                curr[0] = min(curr[0], intervals[i][0])
                curr[1] = max(curr[1], intervals[i][1])

        result.append(curr)

        return result
        