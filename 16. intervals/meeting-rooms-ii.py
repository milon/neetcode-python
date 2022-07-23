from typing import List

"""
Time Complexity: O(nlog(n))
Space Complexity: O(1)
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted(intervals, key=lambda x: x[0])
        end = sorted(intervals, key=lambda x: x[1])
        rooms, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[s]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            rooms = max(rooms, count)
        return rooms
