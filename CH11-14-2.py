#CH11-14. [Pillow]이미지 처리

##################################################################
##이미지를 흐리게 처리
from PIL import Image, ImageTk, ImageFilter 
import tkinter as tk

window = tk.Tk( )
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack( )

im = Image.open("d:\\lenna.png")

out = im.filter(ImageFilter.BLUR) #이미지를 흐리게 합니다.

tk_img = ImageTk.PhotoImage(out)

canvas.create_image(250, 250, image=tk_img)
window.mainloop( )
