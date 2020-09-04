import turtle
import random
import math
import winsound

#setting up the screen
turtle.Screen()
turtle.title("trial")
turtle.bgpic("background.gif")
turtle.setup(width=820,height=820)
turtle.tracer(0)

#creating border
bd=turtle.Turtle()
bd.penup()
bd.goto(-390,-390)
bd.pendown()
bd.pensize(3)
bd.color("white")
bd.lt(90)
for i in range (4):
	bd.fd(780)
	bd.rt(90)

bd.penup()
bd.hideturtle()

#registering shapes for the game
objects=["apple_fruit.gif", "bomb.gif","stone.gif","bucket.gif"]
for object in objects:
    turtle.register_shape(object)

#creating player
player=turtle.Turtle()
player.speed(0)
player.shape("bucket.gif")
player.color("white")
player.penup()
player.goto(0,-350)

#creating score count
score=0

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)
pen.write("score: 0 ", align="center", font=("none 24 normal"))

#creating the stone
#total number of stones
no_of_stones = 10
#creating list of stone
stones=[]

#creating stone from list
for i in range (no_of_stones):
	stones.append(turtle.Turtle())
	for stone in stones:
		stone.speed(0)
		stone.shape("stone.gif")
		stone.color("red")
		stone.penup()
		stone.goto(0,350)
		stone.setheading(-90)
		x = random.randint(-350, 350)
		y = random.randint(100, 250)
		stone.setposition(x, y)

stonespeed=0.3

#creating the fruit
#total number of fruits
no_of_fruits = 10
#creating list of fruits
fruits=[]

#creating fruit from list
for i in range (no_of_fruits):
	fruits.append(turtle.Turtle())
	for fruit in fruits:
		fruit.speed(0)
		fruit.shape("apple_fruit.gif")
		fruit.color("cyan")
		fruit.penup()
		fruit.goto(0,350)
		x = random.randint(-350, 350)
		y = random.randint(100, 250)
		fruit.setposition(x, y)

fruitspeed=0.3

#creating the bomb
#total number of bombs
no_of_bombs = 10
#creating list of bombs
bombs=[]

#creating bomb from list
for i in range (no_of_bombs):
	bombs.append(turtle.Turtle())
	for bomb in bombs:
		bomb.speed(0)
		bomb.shape("bomb.gif")
		bomb.color("green")
		bomb.penup()
		bomb.goto(0,350)
		x = random.randint(-350, 350)
		y = random.randint(100, 250)
		bomb.setposition(x, y)

bombspeed=0.3

#move the player

def player_left():
	y=player.xcor()
	y -= 20
	player.setx(y)


def player_right():
	y=player.xcor()
	y += 20
	player.setx(y)

#keyboard input
turtle.listen()
turtle.onkeypress(player_left,"Left")
turtle.onkeypress(player_right,"Right")

while True:
	turtle.update()

	#moving the stone downwards
	for stone in stones:
		y = stone.ycor()
		y -= stonespeed
		stone.sety(y)
	
	#moving the bomb downwards
	for bomb in bombs:
		y = bomb.ycor()
		y -= bombspeed
		bomb.sety(y)

	#moving the fruit downwards
	for fruit in fruits:
		y = fruit.ycor()
		y -= fruitspeed
		fruit.sety(y)

	#border checking
	if player.xcor() > 380:
		player.setx(380)
	

	if player.xcor() < -380:
		player.setx(-380)

	#collision between the player and the stone
	if (stone.ycor() < -330 and stone.ycor() > -370 ) and (stone.xcor() < player.xcor() + 40 and stone.xcor() > player.xcor() - 40):
		stone.hideturtle()
		#winsound.PlaySound("hit_by_stone.wav",winsound.SND_ASYNC)
		score -= 5
		pen.clear()
		pen.write("score: {}".format(score), align="center", font=("none 24 normal"))

	#collision between the player and the fruit
	if (fruit.ycor() < -330 and fruit.ycor() > -370 ) and (fruit.xcor() < player.xcor() + 40 and fruit.xcor() > player.xcor() - 40):
		fruit.hideturtle()
		#winsound.PlaySound("eat_fruit.wav",winsound.SND_ASYNC)
		score += 10
		pen.clear()
		pen.write("score: {}".format(score), align="center", font=("none 24 normal"))
	
	#collision between the player and the bomb
	if (bomb.ycor() < -330 and bomb.ycor() > -370 ) and (bomb.xcor() < player.xcor() + 40 and bomb.xcor() > player.xcor() - 40):
		bomb.hideturtle()
		#winsound.PlaySound("game_over.wav",winsound.SND_ASYNC)
		print("you collide with a bomb \n Game Over!!! \n Your final score :",score)
		exit()
			

	#reseting the stone after it touches the border
	for stone in stones: 
		if stone.ycor() < -380:
			stone.hideturtle()
			#Reset the stone
			x = random.randint(-350, 350)
			y = random.randint(100, 400)
			stone.showturtle()
			stone.setposition(x, y)

	#reseting the fruit after it touches the border
	for fruit in fruits: 
		if fruit.ycor() < -380:
			fruit.hideturtle()
			#Reset the fruit
			x = random.randint(-350, 350)
			y = random.randint(100, 400)
			fruit.showturtle()
			fruit.setposition(x, y)

	#reseting the bomb after it touches the border
	for bomb in bombs: 
		if bomb.ycor() < -380:
			bomb.hideturtle()
			#Reset the bomb
			x = random.randint(-350, 350)
			y = random.randint(100, 400)
			bomb.showturtle()
			bomb.setposition(x, y)