class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for i in range(len(intervals)):
            events.append((intervals[i][0], 1))
            events.append((intervals[i][1], 0))
        events.sort()
        max_ = 0
        cur = 0
        for a in events:
            if a[1] == 1:
                cur += 1
            else:
                cur -= 1
            max_ = max(cur, max_)

        return max_
