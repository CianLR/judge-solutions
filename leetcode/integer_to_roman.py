from collections import OrderedDict

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        vals = OrderedDict([
            ('M', 1000),
            ('D', 500),
            ('C', 100),
            ('L', 50),
            ('X', 10),
            ('V', 5),
            ('I', 1)
        ])
        numeral = ''
        for c in vals:
            while vals[c] <= num:
                numeral += c
                num -= vals[c]
        
        replace = OrderedDict([
            ('DCCCC', 'CM'),
            ('CCCC', 'CD'),
            ('LXXXX', 'XC'),
            ('XXXX', 'XL'),
            ('VIIII', 'IX'),
            ('IIII', 'IV')
        ])
        for rep in replace:
            numeral = numeral.replace(rep, replace[rep])
        return numeral
        
