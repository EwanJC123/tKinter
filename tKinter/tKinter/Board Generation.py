from tkinter import *
root=Tk()


canvas=Canvas(root, width = 640, height = 640)
canvas.pack()
blockWidth=640//8
blockHeight=640//8
pawnCount=0
castleCount=0
knightCount=0
bishopCount=0
for row in range(0,8):#Check Board Generation
    for column in range(0,8):
        if (row+column)%2==0:
            canvas.create_rectangle(column*blockWidth,row*blockHeight,(column+1)*blockWidth,(row+1)*blockHeight, fill="#f7f4ad")
        else:
            canvas.create_rectangle(column*blockWidth,row*blockHeight,(column+1)*blockWidth,(row+1)*blockHeight, fill="#af8d69")



for i in range(0,8):#Grid GUI Generation
    canvas.create_line(80*i,0,80*i,640)
    canvas.create_line(0,80*i,640,80*i)


for pawnGen in range(0,8):#Pawn GUI Generation
    canvas.create_line(10+pawnCount,90,80+pawnCount-10,150)
    canvas.create_line(10+pawnCount,550,80+pawnCount-10,490)
    pawnCount+=80
    #Need To Add In Colour Variation For Each Side

for castleGen in range(0,2):#Rook GUI Generation
    canvas.create_line(40+castleCount,630,40+castleCount,570)
    canvas.create_line(40+castleCount,10,40+castleCount,70)
    castleCount+=560
    #Need To Add In Colour Variation For Each Side

for knightGen in range(0,2):#Knight GUI Generation
    canvas.create_oval(90+knightCount,630,150+knightCount,570)
    canvas.create_oval(90+knightCount,10,150+knightCount,70)
    knightCount+=400
    #Need To Add In Colour Variation For Each Side

for bishopGen in range(0,2):#Bishop GUI Generation
    canvas.create_rectangle(170+bishopCount,630,230+bishopCount,570)
    canvas.create_rectangle(170+bishopCount,10,230+bishopCount,70)
    bishopCount+=240
    #Need To Add In Colour Variation For Each Side




mainloop()


