#CH11-13. [Pillow]윈도우에 이미지 표시하

##################################################################
##이미지 파일을 윈도우에 보이도록

from PIL import Image, ImageTk 

import tkinter as tk

window = tk.Tk( )
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack( )

img = Image.open("D:\\lenna.png")


tk_img = ImageTk.PhotoImage(img)

canvas.create_image(250, 250, image=tk_img)

window.mainloop( )
