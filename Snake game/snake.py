import turtle
import random 
import time
intial_score = 0
highscore = 0
delay_time = 0.1

window = turtle.Screen()
window.title("Snake game python")
window.bgcolor("White") 
window.setup(width=600, height=400)

snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

food = turtle.Turtle()
food.shape("circle")
food.color("pink")
food.speed(0)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('blue')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Your_score: 0 Highest_Score : 0", align="center", font=("Arial", 24, "normal"))
turtle.mainloop()
