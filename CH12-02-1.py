#CH12-02 신비로운 수, 소수 판별하라! #2

##################################################################
##짝수는 2로 나누어떨어지는 수입니다. 입력한 숫자가 짝수라면
##소수 판별을 해 볼 필요도 없이 “소수가 아닙니다.”라고 판별할 수 있습니다. 

import time
start = time.time( )  

n = int(input("n값을 입력 하세요: "))

count = 1

for a in range(2, n+1):
    
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
