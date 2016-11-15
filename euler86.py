import math;

l = 2;
count = 0;
target = 10**6;

while(count < target):
  l += 1;
  p = l;
  l2 = l*l;

  for wh in range(2, l*2 + 1):

    h2 = wh*wh + l2;

    while(p*p < h2):
      p += 1;

    if (p*p == h2):
      count += wh / 2 if (wh <= l) else 1 + (l - (wh+1)/2);
      p += 1;


print l;
