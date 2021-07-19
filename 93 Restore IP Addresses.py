# Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

# A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

 

# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:

# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:

# Input: s = "1111"
# Output: ["1.1.1.1"]
# Example 4:

# Input: s = "010010"
# Output: ["0.10.0.10","0.100.1.0"]
# Example 5:

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

# Constraints:

# 0 <= s.length <= 3000
# s consists of digits only.
from functools import cache
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        @cache
        def all_possible_start(index,splits):
            if index >= len(s):
                return []
            if splits == 1:
                num = int(s[index:])
                if not 0<=num<=255:
                    return []
                elif (num>0 and s[index]=='0') or (num==0 and index<len(s)-1):
                    return []
                else:
                    return [s[index:]]
            if s[index] == '0':
                all_possibles_nexts = all_possible_start(index+1,splits-1)
                all_possible_now = [s[index]+'.'+next_ for next_ in all_possibles_nexts]
                return all_possible_now
            all_possible_now = []
            for end in range(index,min(index+3,len(s))):
                prefix = s[index:end+1]
                if 0<=int(prefix)<=255:
                    all_possibles_nexts = all_possible_start(end+1,splits-1)
                    all_possible_now.extend((prefix+'.'+n for n in all_possibles_nexts))
            return all_possible_now
        return all_possible_start(0,4)
                
                