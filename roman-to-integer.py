class Solution(object):
    def romanToInt(self, s):
        numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        combs = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        
        # Count:
        total = 0
        num = list(s)  # Strings are immutable and we want to edit ours.
        for i in range(1, len(num)):  # One pass to cover the combination numerals.
            if num[i-1] + num[i] in combs: 
                total += combs[num[i-1]+num[i]]
                num[i-1] = num[i] = "."  # Replace with some char not in numerals dict.
        for i in range(len(num)):  # One pass for the rest.
            if num[i] in numerals:  # Note: elements replaced in earlier loop will not pass this.
                total += numerals[num[i]]
            
        return total
        
