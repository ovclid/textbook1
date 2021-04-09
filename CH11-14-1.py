#CH11-14. [Pillow]이미지 처리

##################################################################
##이미지를 45° 회전

from PIL import Image, ImageTk 
import tkinter as tk

window = tk.Tk( )
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack( )

im = Image.open("d:\\lenna.png")

out = im.rotate(45) 	# 이미지를 45° 회전합니다.

tk_img = ImageTk.PhotoImage(out)

canvas.create_image(250, 250, image=tk_img)
window.mainloop( )
