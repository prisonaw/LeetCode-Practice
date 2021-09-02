class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals
    
        ans = []
    
        intervals.sort(key=lambda x:x[0]) # sort based on starting indicies of intervals
    
        ans.append(intervals[0])
        prevInterval = ans[0]
    
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prevInterval[1]:
            # starting idx is within ending idx of previous, merge
                prevInterval[1] = max(prevInterval[1], intervals[i][1]) # max ending idx of cur and previous interval
            else:
            # starting idx is greater than prev ending idx
                prevInterval = intervals[i]
                ans.append(intervals[i])
        return ans

                