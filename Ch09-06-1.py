#CH09-06. 딕셔너리와 반복문의 궁합

##################################################################
##반복문과 딕셔너리의 keys( ), values( )

phone_book = {'홍길동':'010-1234-5678',
	      '강감찬':'010-1111-2222',
              '이순신':'010-3333-4444'}

for i in phone_book.keys( ):
    print(i)

for i in phone_book.values( ):
    print(i)
