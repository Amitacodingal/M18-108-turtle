#square

import turtle
t = turtle.Turtle()
s = int(input("Enter the length of the side of the Square: "))  
for i in range(4):
  # drawing first side
  t.forward(50) # Forward turtle by s units
  t.left(90) # Turn turtle by 90 degree


import turtle    #importing library
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() #defined variable
 
num_sides = 6 #variable
side_length = 70
angle = 360.0 / num_sides
#iterate loop for total number of side
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
     
turtle.done()

#triangle

import turtle

turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()
 
# first triangle for star
board.forward(100) # draw base
 
board.left(120)
board.forward(100)
 
board.left(120)
board.forward(100)
 
board.penup()
board.right(150)
board.forward(50)
 
# second triangle for star
board.pendown()
board.right(90)
board.forward(100)
 
board.right(120)
board.forward(100)
 
board.right(120)
board.forward(100)
 
turtle.done()

#spiral
import turtle     #importing library       
my_wn = turtle.Screen()
my_wn.bgcolor("light blue") #screen background color
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 0
while True: #iterate loop
  for i in range(4): 
    my_pen.fd(size + 1)
    my_pen.left(90)
    size = size - 5
  size = size + 1
  
  #spiral2
import turtle #importing library
loadWindow = turtle.Screen()
turtle.speed(2) #speed of turtle
 
for i in range(100): #iterate for loop
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
 
turtle.exitonclick()
