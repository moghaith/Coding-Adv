import turtle
import time
window = turtle.Screen()
window.bgcolor('black')
window.title("Cookie")
window.screensize(720, 1980)

cookie = turtle.Turtle()
window.register_shape('Coding-Adv/cookie clicker/cookie1.gif')
window.register_shape('Coding-Adv/cookie clicker/cookie2.gif')
cookie.shape("Coding-Adv/cookie clicker/cookie1.gif")
cookie.speed(0)

click_count = 0
start_time = 0 
endtime = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color('white')
pen.penup()
pen.goto(0,310)
pen.write(f"Click on the Cookie", align='center', font=('Roboto', 32, 'normal'))
pen.goto(0,280)
pen.write(f"Time starts upon your first click", align='center', font=('Roboto', 26, 'normal'))
pen.goto(0,230)
pen.write(f"Press on F button when you finish to show your speed", align='center', font=('Roboto', 26, 'normal'))
def clickcounter(x,y):
    global click_count
    global start_time
    click_count += 1
    if click_count == 1 :
        start_time = time.time()
    pen.clear()
    pen.write(f"Clicks Score: {click_count}", align='center',font=('Roboto', 32, 'normal'))
    cookie.shape('Coding-Adv/cookie clicker/cookie2.gif')
    cookie.shape('Coding-Adv/cookie clicker/cookie1.gif')
def finishgame():
    pen.clear()
    cookie.hideturtle()
    global start_time
    global endtime
    endtime = time.time()
    totaltime = endtime - start_time
    rate = click_count/totaltime
    pen.write(f"You clicked: {click_count} clicks in {round(totaltime, 2)} Seconds \n Your rate is {round(rate,2)}", align='center',font=('Roboto', 32, 'normal'))

cookie.onclick(clickcounter)
window.onkeypress(finishgame, 'f')
window.listen()

window.mainloop()