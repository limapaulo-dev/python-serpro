def romanToInt(s):

        romanDic = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000, }
        
        intFromRoman = 0

        for roman in s:
            intFromRoman += int(romanDic[roman])
      
        if(s.count("IV") or s.count("IX")):
              intFromRoman -= 2
        if(s.count("XL") or s.count("XC")):
              intFromRoman -= 20
        if(s.count("CD") or s.count("CM")):
              intFromRoman -= 200

        return intFromRoman

print(romanToInt("MCD"))