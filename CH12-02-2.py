#CH12-02 신비로운 수, 소수 판별하라! #2

##################################################################
##입력한 수가 소수이더라도 2부터 그 수까지 모두 따져볼 필요는 없습니다.

import time
start = time.time( )  

n = int(input("n값을 입력 하세요: "))

count = 1

b = (n+1)//2
for a in range(2, b):
    if n % 2 == 0 :
        count += 3
        break

    elif n % a == 0 :
        count += 1

if(count == 2):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
        
print("time :", time.time( ) - start)  

