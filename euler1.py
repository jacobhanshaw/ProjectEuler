result = 0
term0 = 1
term1 = 1

while term1 < 4000000:
    term1 += term0
    term0 = term1 - term0
    if term1 % 2 == 0:
        result += term1

print result
