#CH12-07. 히스토그램을 그려봅시다.

##################################################################
##히스토그램

#파일을 읽어 데이터를 처리하는 부분
a = [ ]				#파일의 모든 내용을 읽어 임시 저장하는 리스트
data = [' ', ' ', ' ', ' ', ' ']	#공백으로 구분된 자료를 항목별로 분리하여 저장하는 리스트
score = [0, 0, 0, 0, 0]		#항목별 설문 
total = 0

infile = open("F:\\interest.txt", "r")	#데이터 파일을 불러옵니다.
lines = infile.readlines( )			#파일을 한 줄씩 읽어서 a리스트에 저장합니다.
for i in lines:
    a.append(i)

for i in range(0, 5):		#공백으로 구분된 자료들을 하나하나 data리스트 저장합니다.
    data[i] = a[i].split( )		#data[항목][점수] 구조로 저장합니다.

for i in range(0, 5):			#항목이 5개입니다.
    for j in range(1, 26):		#25명에게 자료를 조사하였습니다.
        score[i]+= int(data[i][j])		#항목별로 점수를 합산합니다.
        
    total += score[i]			#모든 항목의 점수를 합산합니다.
    print(data[i][0] + "=" + str(score[i]) + "점")		#항목별 총점을 출력합니다.

print("합계="+str(total))					#모든 항목의 총점을 출력합니다.
infile.close( )

# 터틀 그래픽으로 히스토그램을 그리는 부분
import turtle
t = turtle.Turtle( )
t.shape("turtle")
pen = ["red", "blue", "orange", "green", "purple"]	#히스토그램의 항목별 색깔
t.pensize(2)

def bar(category, s) :		#히스토그램을 그리는 함수: 항목과 점수를 전달 받습니다.
    t.begin_fill( )
    t.left(90)
    t.forward(s)				#전달 받은 점수는 막대의 높이가 됩니다.
    t.write(category+" "+str(s)+"점")	#점수 문자 출력
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(s)
    t.left(90)
    t.end_fill( )
    t.forward(10)

for i in range(0, 5):
    t.color(pen[i])			#히스토그램의 항목의 색을 저장합니다.
    category = data[i][0]		#항목 이름을 저장합니다.
    s = int(score[i])			#해당 항목 점수의 총합을 저장합니다.
    bar(category, s)			#히스토그램을 그리는 함수를 호출합니다.
