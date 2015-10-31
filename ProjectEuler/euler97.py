"""
power of 2's
1's place cycles every 4
10's place cycles every 20
100's place cycles every 100

cycle = 4 * 5^(p-1)
"""

lowestDigits=10
cycle = 4 * 5**(lowestDigits-1)
power = 7830457
power %= cycle

print ((28433*2**power+1) % (10**lowestDigits))
