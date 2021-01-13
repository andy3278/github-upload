
import turtle 
import random 
screen = turtle.Screen()
turtle_1 = turtle.Turtle()
turtle_2 = turtle.Turtle()
turtle_1.speed(30)
for w in range(1000) :
    prob = random.random()
    #if (prob>0.5):
    turtle_1.forward(prob*30)
    #else:
    #   turtle_1.backward(prob*30)
    turtle_1.pensize(1)
    if (prob>0.5):
        turtle_1.right(prob*90)
    else:
        turtle_1.left(prob*90)
