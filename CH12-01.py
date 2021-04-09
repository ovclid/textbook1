#CH12-01 신비로운 수, 소수 판별하라! #1

##################################################################
##소수 판별

import time
start = time.time( )  

n = int(input("n값을 입력하세요: "))

count = 1

for a in range(2, n+1):
    if n % a == 0 :
        count += 1

if(count == 2):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
        
print("time :", time.time( ) - start)  
