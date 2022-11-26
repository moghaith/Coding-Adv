import turtle
import time


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Cookie Click")
wn.screensize(700,1000)

wn.register_shape("Coding-Adv/cookie clicker/cookie1.gif")
wn.register_shape("Coding-Adv/cookie clicker/cookie2.gif")
cookie = turtle.Turtle()
cookie.shape("Coding-Adv/cookie clicker/cookie1.gif")
cookie.speed(0)

clicks = 0
start_time = 0
endtime = 0

pen = turtle.Turtle()
pen.hideturtle()

pen.color("white")
pen.penup()
pen.goto(0,350)
pen.write(f"Clicks: {clicks}", align="center", font=("Roboto", 32, "normal"))
pen.goto(0,300)
pen.write(f"Time starts upon your first click", align="center", font=("Roboto", 26 , "normal"))
pen.goto(0, 250)
pen.write(f"Click on F Once you finish to Show your speed", align="center", font=("Roboto", 18 , "normal"))
if (clicks == 1):
    start_time = time.time()
def exitgm():
    global clicks
    pen.clear()
    cookie.hideturtle()
    global start_time
    global endtime 
    endtime = time.time()
    totaltime = (endtime - start_time)

    pen.write(f"You Clicked: {clicks} in {round(totaltime,2)} Seconds \n Your rate is {round((clicks/totaltime),3)} clicks/sec",align="center", font=("Roboto", 16, "normal"))
    
def clicked(x, y):
    global clicks
    global start_time
    clicks += 1
    if clicks == 1:
        start_time = time.time()
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Roboto", 32, "normal"))
    cookie.shape("Coding-Adv/cookie clicker/cookie2.gif")
    cookie.shape("Coding-Adv/cookie clicker/cookie1.gif")



cookie.onclick(clicked)
wn.onkeypress(exitgm, 'f')
wn.listen()

wn.mainloop()