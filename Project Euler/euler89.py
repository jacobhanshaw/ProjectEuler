"""
Given that the roman numerals follow these rules:

Numerals must be arranged in descending order of size.
M, C, and X cannot be equalled or exceeded by smaller denominations.
D, L, and V can each only appear once.

Things to replace:
IIII  with IV: 2
VIIII with IX: 3
XXXX  with XL: 2
LXXXX with XC: 3
CCCC  with CD: 2
DCCCC with CM: 3

Generalized rule:

Any four in a row (except M) can be replaced to save at least 2 characters.

More specific rule:

If character before the 4 in a row is the next sized roman numeral, 1 more
character is replaced.
"""

neededStreak=4

replaced=0
baseExpFile = open("p089_roman.txt")

for line in baseExpFile:
    numeral=line.rstrip()
    last=""
    streak=0

    for i in range(len(numeral)):
        if numeral[i]==last and last <> 'M':
            streak+=1
            if streak==neededStreak:
                replaced+=2
                checkI=i-neededStreak
                if checkI >= 0 and \
                    ((numeral[i]=='I' and numeral[checkI]=='V') \
                       or (numeral[i]=='X' and numeral[checkI]=='L') \
                         or (numeral[i]=='C' and numeral[checkI]=='D')):
                    replaced+=1
        else:
            last=numeral[i]
            streak=1

print "Replaced:",replaced
