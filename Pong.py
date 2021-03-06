import turtle

win = turtle.Screen()
win.title("Pong Python por 71-M0")
win.bgcolor("black")
win.setup(width=800 , height=600)
win.tracer(0)

#Bloco A
blca = turtle.Turtle()
blca.speed(0)
blca.shape("square")
#blca.shapesize(5 , 1)
blca.shapesize(stretch_wid=5 , stretch_len=1)
blca.color("white")
blca.penup()
blca.goto(-350 , 0)

#Bloco B
blcb = turtle.Turtle()
blcb.speed(0)
blcb.shape("square")
#blcb.shapesize(5 , 1)
blcb.shapesize(stretch_wid=5 , stretch_len=1)
blcb.color("white")
blcb.penup()
blcb.goto(350 , 0)

#Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = -0.2

#Função
def blca_up():
    y = blca.ycor()
    y += 20
    blca.sety(y)

def blca_down():
    y = blca.ycor()
    y += -20
    blca.sety(y)

def blcb_up():
    y = blcb.ycor()
    y += 20
    blcb.sety(y)

def blcb_down():
    y = blcb.ycor()
    y += -20
    blcb.sety(y)

#Teclado
win.listen()
win.onkeypress(blca_up, "w")
win.onkeypress(blca_down, "s")
win.onkeypress(blcb_up, "Up")
win.onkeypress(blcb_down, "Down")

#Main Loop
while True:
    win.update()

    #Mover bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)
        
    #Borda
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
    
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1   
    
    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx *= -1
    
    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx *= -1   

    #Colisão 
    if bola.xcor() < -340 and bola.ycor() < blca.ycor() + 50 and bola.ycor() > blca.ycor() - 50:
        bola.dx *= -1 
    
    elif bola.xcor() > 340 and bola.ycor() < blcb.ycor() + 50 and bola.ycor() > blcb.ycor() - 50:
        bola.dx *= -1
       



