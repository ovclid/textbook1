#CH12-03 신비로운 수, 소수 판별하라!-에라토스테네스의 체

##################################################################
##에라토스테네스의 체

n=1000
number = [False, False] + [True] * (n-1)

primes=[ ]

for i in range(2, n+1):
  if number[i] :
    primes.append(i)
    for j in range(2*i, n+1, i):
        number[j] = False
print(primes)
