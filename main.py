from turtle import *
import turtle
import random
from random import randint
screen = turtle.Screen()
# Fullscreen the canvas
# Variables, List, Functions.
player = ["red", "blue", "green", "orange"]
colorText = ["red", "blue", "green", "orange"]
haveBooster = [False, False, False, False]
goto(-100, -140)
audience = []
for n in range(20):
  aud = Turtle()
  aud.color("red")
  aud.shape("turtle")
  aud.left(90)
  aud.penup()
  aud.goto((n - 10) * 20, -60)
  audience.append(aud)
for step in range(4):
    pencolor(player[step])
    pendown()
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    penup()

    forward(10)
    right(90)
    forward(15)
    pendown()
    write("b")
    penup()
    right(180)
    forward(15)
    right(90)
    forward(60)
# Begin!
speed(0)
penup()
goto(-140, 140)
for step in range(15):
  write(step, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)
# Add a turtle
playerOne = Turtle()
playerOne.color('red')
playerOne.shape('turtle')
playerOne.penup()
playerOne.goto(-160, 100)
playerOne.pendown()
for turn in range(10):
  playerOne.right(36)
# Add another turtle
PlayerTwo = Turtle()
PlayerTwo.color('blue')
PlayerTwo.shape('turtle')
PlayerTwo.penup()
PlayerTwo.goto(-160, 70)
PlayerTwo.pendown()
for turn in range(72):
  PlayerTwo.left(5)
# Add another turtle
PlayerThree = Turtle()
PlayerThree.shape('turtle')
PlayerThree.color('green')
PlayerThree.penup()
PlayerThree.goto(-160, 40)
PlayerThree.pendown()
for turn in range(60):
  PlayerThree.right(6)
# Add another turtle
PlayerFour = Turtle()
PlayerFour.shape('turtle')
PlayerFour.color('orange')
PlayerFour.penup()
PlayerFour.goto(-160, 10)
PlayerFour.pendown()
for turn in range(30):
  PlayerFour.right(12)
playerOneDistance = 0
playerTwoDistance = 0
playerThreeDistance = 0
playerFourDistance = 0
# Move turtles
playerOneSpeed = 5
playerTwoSpeed = 5
playerThreeSpeed = 5
playerFourSpeed = 5
for turn in range(100):
  randomNumberOne = randint(1, playerOneSpeed)
  randomNumberTwo = randint(1, playerTwoSpeed)
  randomNumberThree = randint(1, playerThreeSpeed)
  randomNumberFour = randint(1, playerFourSpeed)
  playerOne.forward(randomNumberOne)
  PlayerTwo.forward(randomNumberTwo)
  PlayerThree.forward(randomNumberThree)
  PlayerFour.forward(randomNumberFour)
  playerOneDistance += randomNumberOne
  playerTwoDistance += randomNumberTwo
  playerThreeDistance += randomNumberThree
  playerFourDistance += randomNumberFour
  screen.tracer(0)
  for aud in audience:
    aud.penup()
    aud.goto(aud.xcor(), aud.ycor() + random.randint(-3, 3))
  screen.update()
  # Boost Turtle Speeds
  boost = randint(1, 125)
  if boost == 25 and haveBooster[0] == False:
    playerOneSpeed = randint(6, 10)
    haveBooster[0] = True
    turtleCover1 = Turtle()
    turtleCover1.penup()
    turtleCover1.shape("square")
    turtleCover1.color("red")
    turtleCover1.goto(-85, -155)
  if boost == 50 and haveBooster[1] == False:
    playerTwoSpeed = randint(6, 10)
    haveBooster[1] = True
    turtleCover2 = Turtle()
    turtleCover2.penup()
    turtleCover2.shape("square")
    turtleCover2.color("purple")
    turtleCover2.goto(-15, -155)
  if boost == 75 and haveBooster[2] == False:
    playerThreeSpeed = randint(6, 10)
    haveBooster[2] = True
    turtleCover3 = Turtle()
    turtleCover3.penup()
    turtleCover3.shape("square")
    turtleCover3.color("yellow")
    turtleCover3.goto(-55, -155)
  if boost == 100 and haveBooster[3] == False:
    playerFourSpeed = randint(6, 10)
    haveBooster[3] = True
    turtleCover4 = Turtle()
    turtleCover4.penup()
    turtleCover4.shape("square")
    turtleCover4.color("blue")
    turtleCover4.goto(-85, -125)


distanceList = [playerOneDistance, playerTwoDistance, playerThreeDistance, playerFourDistance]
goto(0, -200)
if max(distanceList) == playerOneDistance:
    write("Red Wins!", align='center', font=('Arial', 20, 'normal'))
  # Changes the you win text to red
    redColor = "red"
    pencolor(redColor)
if max(distanceList) == playerTwoDistance:
    write("Blue Wins!", align='center', font=('Arial', 20, 'normal'))
    # Changes the you win text to blue
    blueColor = "blue"
    pencolor(blueColor)
if max(distanceList) == playerThreeDistance:
    write("Green Wins!", align='center', font=('Arial', 20, 'normal'))
    # Changes the you win text to green
    greenColor = "green"
    pencolor(greenColor)
if max(distanceList) == playerFourDistance:
    write("Orange Wins!", align='center', font=('Arial', 20, 'normal'))
    # Changes the you win text to orange
    orangeColor = "orange"
    pencolor(orangeColor)
mainloop()
