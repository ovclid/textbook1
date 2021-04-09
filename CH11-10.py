#CH11-10 [tkinter]MyPaint 프로그램

##################################################################
##MyPaint 프로그램

from tkinter import *

def paint(event):
      x1, y1 = ( event.x-1 ), ( event.y+1 )
      x2, y2 = ( event.x-1 ), ( event.y+1 )
      canvas.create_oval( x1, y1, x2, y2)

window = Tk( )
canvas = Canvas(window)
canvas.pack( )
canvas.bind("<B1-Motion>", paint)
window.mainloop( )
