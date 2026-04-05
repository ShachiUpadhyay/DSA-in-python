#https://neetcode.io/problems/insert-new-interval/question?list=neetcode250

class Solution:
    def insert(self, intervals: List[List[int]], newinterval: List[int]) -> List[List[int]]:

        i : int = 0
    

        n = len(intervals)

        result : List[List[int]] = []

        added : bool = False

        while i < n:
            if intervals[i][1]<newinterval[0]:
                result.append(intervals[i])
                i += 1
            elif intervals[i][0] > newinterval[1]:
                if not added:
                    result.append(newinterval)
                    added = True
                result.append(intervals[i])
                i +=1
      
            else:
                newinterval[0] = min(newinterval[0], intervals[i][0])
                newinterval[1] = max(newinterval[1], intervals[i][1])
                i += 1

        if not added:
            result.append(newinterval)

        return result
        