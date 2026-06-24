import turtle
import random
import time
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0, startx=0, starty=0)

firstPlace = True
secondPlace = True
thirdPlace = True
fourthPlace = True

def makeTurtle():
  t = turtle.Turtle()
  t.shape("turtle")
  t.penup()
  return t
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)

t.penup()
t.goto(-100, 100)
t.right(90)
for i in range(5):
  t.pendown()
  t.forward(300)
  t.penup()
  t.sety(100)
  t.setx(t.xcor() + 50)
  
t.goto(-100, -175)
t.lt(90)
t.pendown()
t.forward(200)
t.penup()

t1 = makeTurtle()
t2 = makeTurtle()
t3 = makeTurtle()
t4 = makeTurtle()
t1.color("red")
t2.color("blue")
t3.color("yellow")
t4.color("green")
turtles = [t1, t2, t3, t4]
raceStart = -75
for turt in turtles:
  turt.goto(raceStart, 100)
  raceStart += 50

t.goto(100, 150)
for turt in turtles:
  turt.rt(90)

screen.tracer(0)

for i in range(200):

  for turt in turtles:
      turt.speed(random.randint(1,10))
      if turt.ycor() >= -200:
        turt.forward(random.randint(1,10))
      else:
        if firstPlace:
          turt.penup()
          turt.goto(-300, -250)
          turt.pendown()
          turt.write("I got first place!")
          firstPlace = False
        else:
          if secondPlace:
            turt.penup()
            turt.goto(-200, -250)
            turt.pendown()
            turt.write("I got second place.")
            secondPlace = False
          else:
            if thirdPlace:
              turt.penup()
              turt.goto(200, -250)
              turt.pendown()
              turt.write("I got third place...")
              thirdPlace = False
            else: 
              if fourthPlace:
                turt.penup()
                turt.goto(300, -250)
                turt.pendown()
                turt.write("Get that camera out of my FACE!!")
                fourthPlace = False
  screen.update()
  time.sleep(0.01)

turtle.done()
