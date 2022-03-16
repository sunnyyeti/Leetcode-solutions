# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

 

# Example 1:

# Input: time = "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
# It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:

# Input: time = "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
 

# Constraints:

# time.length == 5
# time is a valid time in the form "HH:MM".
# 0 <= HH < 24
# 0 <= MM < 60
class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = list({int(char) for char in time if char.isdigit()})
        all_times = []
        tmp = []
        def bt():
            if len(tmp)==4:
                hour = 10*tmp[0]+tmp[1]
                minutes = 10*tmp[2]+tmp[3]
                if 0<=hour<24 and 0<=minutes<60:
                    all_times.append("{:02d}:{:02d}".format(hour,minutes))
                return
            for d in digits:
                tmp.append(d)
                bt()
                tmp.pop()
        bt()
        all_times.sort()
        for t in all_times:
            if t>time:
                return t
        return all_times[0]
        
                