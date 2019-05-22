# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example 1:
#
# Input: a = 1, b = 2
# Output: 3
# Example 2:
#
# Input: a = -2, b = 3
# Output: 1
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            carry = a & b
            a = (a ^ b)&(0xffffffff)
            b = (carry << 1)
        return a if (a>>31)==0 else a-2**32

# class Solution {
# public:
#     int getSum(int a, int b) {
#         unsigned int c = a;
#         unsigned int d = b;
#         while (d){
#             unsigned int carry = c&d;
#             c = c^d;
#             d = carry<<1;
#         }
#         int res = c;
#         return res;
#     }
# };
if __name__=="__main__":
    print(Solution().getSum(1,2))