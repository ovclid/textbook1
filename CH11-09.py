#CH11-09. [tkinter]윈도우 창 메뉴 만들기

##################################################################
##윈도우 창의 메뉴를 생성

import tkinter as tk

def open( ):		
    pass

def quit( ):		
    window.quit( )

window = tk.Tk( ) 	# 윈도우를 생성합니다.

menubar = tk.Menu(window) 

filemenu = tk.Menu(menubar)

filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="종료", command=quit)


menubar.add_cascade(label="파일", menu=filemenu)

window.config(menu=menubar)
window.mainloop( )
