# Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

# Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

# Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

 

# Example 1:

# Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
# Output: [1,0,0,0,0]
# Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
 

# Note:

# 1 <= arr1.length <= 1000
# 1 <= arr2.length <= 1000
# arr1 and arr2 have no leading zeros
# arr1[i] is 0 or 1
# arr2[i] is 0 or 1
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res1 = self.binary_dec(arr1)
        res2 = self.binary_dec(arr2)
        #rint(res1,res2)
        res3 = self.dec_binary(res1+res2)
        #rint(res3)
        return res3
    
    
    def binary_dec(self,bin_list):
        res = 0
        for b in bin_list:
            res = res*-2+b
        return res
    
    def dec_binary(self,dec):
        if dec==0:
            return [0]
        ans = []
        while dec!=0:
            if dec%(-2)==0:
                ans.append(0)
                dec = dec//-2
            else:
                ans.append(1)
                dec = (dec-1)//-2
        return ans[::-1]
        
        