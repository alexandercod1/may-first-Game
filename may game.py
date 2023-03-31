import turtle

#setup orange game

Game= turtle.Screen()

Game.title(" orange for agricultural Crops Game")

Game.setup(width=1000, height=800)

Game.tracer(0)

#Tracer hjälper till så att spelat inte laggar och ska vara som en live video

Game.bgcolor(.1, .1, .1 ) 

screen = turtle.Screen()

image = r"C:\Users\02alsa09\Desktop\may first Game\Image\logo-01.gif"

screen.addshape(image)
turtle.shape(image)
# sätta upp spelts delar #bållen 
ball= turtle.Turtle()
ball.speed(0) # här bestämer vi hur snabbt bållen ska vara 0 är jätte snabbt 
ball.shape("square")
ball.color("white")  
ball.goto(x=0, y=0) #start postion 
ball.penup() # när objekt rör sig lämnar de skugga backom och penup ta bort det och den gör objekt effektivare 
ball_dx , ball_dy= 1, 1
ball_speed= 1
# center line 

center_line= turtle.Turtle () 
center_line.speed(0) 
center_line.shape("square")
center_line.color("white")
center_line.shapesize(stretch_len=.1, stretch_wid=800 )
center_line.penup()
center_line.goto(0,0)
#första spelaren 
player1= turtle.Turtle()  
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_len=1, stretch_wid=5)
player1.penup()
player1.color("blue")
player1.goto(x=-350, y=0)

#andra spelaren 
player2= turtle.Turtle()  
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_len=1, stretch_wid=5)
player2.penup()
player2.color("orange") 
player2.goto(x=350, y=0)

#score text 
score = turtle.Turtle()
score.speed(0) 
score.color("white")
score.penup()
score.goto(x=0, y=260)
score.write( "player1: 0 player2:0", align="center", font=("courier",14,"normal"))
score.hideturtle() #vi döljer objekt för vi vill bara se texten 

p1_score, p2score = 0,0 

# nu ska vi  få objekt att röra på sig
players_speed= 40
def p1_move_up():
    player1.sety(player1.ycor() + players_speed)

def p1_move_down():
    player1.sety(player1.ycor() - players_speed)


def p2_move_up():
    player2.sety(player2.ycor() + players_speed)

def p2_move_Down():
    player2.sety(player2.ycor() - players_speed)

# nu ska vi få tägentbordet att funka
Game.listen()

# de gör att tangentbordet att regare med spelaren /input

Game.listen()
Game.onkeypress(p1_move_up, "w")
Game.onkeypress(p1_move_down, "s")

Game.onkeypress(p2_move_up,"Up")
Game.onkeypress(p2_move_Down,"Down") 


# game loop den gör att spelat är i gåg hela tiden eller upprebar 

while True:
    Game.update()

    #ball movement 
    ball.setx(ball.xcor() + (ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))

    #ball& borders collision
    if(ball.ycor()>290):
        ball.sety(290)
        ball_dy *= -1

    if(ball.ycor() <-290):
        ball.sety(-290)
        ball_dy *=-1 

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (player1.ycor()-60) and ball.ycor() < (player1.ycor()+60):
        ball.setx(-340)
        ball_dx *=-1 

    if ball.xcor() >  340 and ball.xcor() < 350 and ball.ycor() > (player2.ycor()-60) and ball.ycor() < (player2.ycor()+60):
        ball.setx(340)
        ball_dx *=-1 


    if (ball.xcor () > 390):
        ball.goto(0, 0)
        ball_dx *= -1 

    if (ball.xcor () < -390):
        ball.goto(0, 0)
        ball_dx *= -1
