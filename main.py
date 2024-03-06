from turtle import *
import random
# Fullscreen the canvas
# Variables, List, Functions.
player = ["red", "blue", "green", "orange"]
haveBooster = [False, False, False, False]
goto(-100, -140) 
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
# Move turtles
for turn in range(100):
  playerOne.forward(random.randint(1, 5))
  PlayerTwo.forward(random.randint(1, 5))
  PlayerThree.forward(random.randint(1, 5))
  PlayerFour.forward(random.randint(1, 5))
  # Boost Turtle Speeds
mainloop()
