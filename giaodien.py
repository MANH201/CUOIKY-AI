from cProfile import label
from tkinter import scrolledtext
from functools import partial
from tkinter import *
import PIL.Image
import PIL
from PIL import ImageTk, ImageSequence
from PIL import Image
import tkinter as tk
from Tro_li_ao import thread_mutiii

# tạo giao diện chính
manh = tk.Tk()
manh.title("Trợ lí ảo")
manh.geometry("450x500+1000+100")
manh.iconbitmap("Picture/logo1.ico")
manh.resizable(False, False)
manh.configure(bg='light blue')
manh.attributes("-topmost",True)
# tạo hình nền
load = Image.open("Picture/nen.jpg")
load_main = ImageTk.PhotoImage(load.resize((450,200)))
load_label = tk.Label(image=load_main,border=0,bg='white')
load_label.place(x=0,y=0)
# tạo ảnh gif
# def play_gif():
#     global img
#     img = Image.open("Picture/1.2.gif")

#     lbl= Label(manh,bg='light blue')
#     lbl.place(x=0,y=420)
#     for img in ImageSequence.Iterator(img):
#         img = img.resize((500,80))
#         img = ImageTk.PhotoImage(img)
#         lbl.config(image=img)
#         manh.update()
#         time.sleep(0.05)
#     manh.after(0,play_gif)

# tạo nút nhấn
record_open = Image.open(r"Picture\micro1.png")
img_record = ImageTk.PhotoImage(record_open.resize((80,80)))
but = tk.Button(manh,image=img_record,border=0,bg='light blue',command = partial(thread_mutiii))   
but.place(x=175,y=350)
#but1 = tk.Button(manh,image=img_record,border=0,bg='light blue',command = partial(play_gif))
#but1.place(x=175,y=350)
# tạo tên bạn
user_label = Label(manh,text="Bạn:",border=1,bg='light blue',font=("Helvetica",13,"bold"))
user_label.place(x=67,y=300)
# tạo tên trợ lí ảo
assistant_lable = Label(manh,text="Trợ lí ảo:",border=1,bg='light blue',font=("Helvetica",13,"bold"))
assistant_lable.place(x=30,y=230)

scrollable_text=scrolledtext.ScrolledText(manh,state='disabled',height=6.5,
    width=31,relief='sunken',bd=5,wrap=tk.WORD,bg='#add8e6',fg='#800000')
scrollable_text.place(x=110,y=220)



manh.mainloop() 
