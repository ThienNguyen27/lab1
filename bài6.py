from turtle import *
for a in range(4):
    forward(100)
    left(90)
penup() # nhất bút
left(180)
forward(10)
left(90)
forward(10)
left(180)
pendown() # hạ bút vẽ tiếp
for b in range(4):
    forward(120)
    right(90)
for c in range(8):
    forward(121)
    right(90)    
mainloop()