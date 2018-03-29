from tkinter import *
root=Tk()


canvas=Canvas(root, width = 640, height = 640)
canvas.pack()
count=0
for i in range(0,8):
    
    canvas.create_line(80*i,0,80*i,640)
    canvas.create_line(0,80*i,640,80*i)
    canvas.create_line(0+count,80,80+count,160)
    canvas.create_line(0+count,560,80+count,480)
    count+=80





mainloop()


