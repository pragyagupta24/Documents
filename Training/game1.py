import pgzrun

b = Rect(50,50), (100,50)
vx=1 #global variable

def draw():
    screen.fill('black')
    screen.draw.filled_rect(b, 'blue')

def update():
    b.x += vx

pgzrun.go()      