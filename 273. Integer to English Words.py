# Share
# Convert a non-negative integer num to its English words representation.

 

# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:

# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:

# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Example 4:

# Input: num = 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
 

# Constraints:

# 0 <= num <= 231 - 1
# Accepted
# 240,054
# Submissions
# 841,991
class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return 'Zero'
        num = str(num)
        #print(num)
        def read(number,unit):
            ones = {
                '1': 'One',
                '2': 'Two',
                '3': 'Three',
                '4': 'Four',
                '5': 'Five',
                '6': 'Six',
                '7': 'Seven',
                '8': 'Eight',
                '9': 'Nine'
            }
            twos = {
                '10': 'Ten',
                '11': 'Eleven',
                '12': 'Twelve',
                '13': 'Thirteen',
                '14': 'Fourteen',
                '15': 'Fifteen',
                '16': 'Sixteen',
                '17': 'Seventeen',
                '18': 'Eighteen',
                '19': 'Nineteen'
            }
            tens = {
                '2': 'Twenty',
                '3': 'Thirty',
                '4': "Forty",
                '5': 'Fifty',
                '6': 'Sixty',
                '7': 'Seventy',
                '8': 'Eighty',
                '9': 'Ninety'
            }
            ans = []
            number = number.zfill(3)
            #print(number)
            if number[0] in ones:
                ans.append(ones[number[0]])
                ans.append('Hundred')
            if number[1:] in twos:
                ans.append(twos[number[1:]])
            else:
                if number[1] in tens:
                    ans.append(tens[number[1]])
                #print(number[2],'fff')
                if number[2] in ones:
                    ans.append(ones[number[2]])
            ans = (' '.join(ans)+ (f" {unit}" if unit else "")) if ans else ""
            return ans
        ans = []
        ans.append(read(num[:-9],"Billion"))
        ans.append(read(num[-9:-6],"Million"))
        ans.append(read(num[-6:-3],'Thousand'))
        ans.append(read(num[-3:],''))
        return ' '.join(filter(lambda x: x,ans)).strip()
            