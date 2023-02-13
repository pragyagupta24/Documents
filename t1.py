from turtle import * # import turtle module

speed('fastest')
side = 12
size = 50



# create a hexagon
for i in range(side):
    forward(size)
    left(360/side)
    write(i)
hideturtle()
mainloop()     # hold window
   
