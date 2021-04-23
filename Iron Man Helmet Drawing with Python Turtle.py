'''Iron Man Helmet Drawing with Python Turtle

Explanation:

First Part:
a. In the first part of the Draw Ironman Helmet, we will import the turtle module and set the variable ankur1,ankur2,ankur3, and its value as below code:

avinash1=[[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20)],[(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]]

avinash2=[[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210)],[(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]]

avinash3=[[(-60, -220), (-80, -240), (-110, -220), (-120, -250),(-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250)],[(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250),(110, -220), (80, -240), (60, -220), (0, -220)]]

b. Then we will hide the turtle and set the background color to #ba161e and set the size to 500 / 600.
c. Likewise, we will make the above turtle to move in the above codes. Set the speed to 2.

Second Part:
a. Create a function name logo() with the parameters “a” and “b”. Inside this function, call the penup(), goto(b),pendown() method and set the color to #fab104 and begin the fill.
b. After that inside the function itself, create a for loop with the range of { len(a[0]) }. Inside this loop, set x, y = a [0][i]. Then, goto (x, y).
c. Coming out of the loop, again create another for loop with the range of { len(a[1]) }. Inside this loop, set x, y = a[1][i]. Then, goto x,y and coming out of the loop, end the fill.

Last Part:
a. In this part just call the functions in the following order and hide the turtle.
logo(avinash1,avinash1Goto)
logo(avinash2,avinash2Goto)
logo(avinash3,avinash3Goto)
'''

import turtle

avinash1 = [
    [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),
     (-40, -20), (0, -20)],
    [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),
     (40, 120), (0, 120)]]
avinash2 = [
    [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),
     (-80, -230), (-64, -210), (0, -210)],
    [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),
     (100, -46), (50, -40), (40, -30), (0, -30)]]
avinash3 = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),
             (0, -250)],
            [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240),
             (60, -220),
             (0, -220)]]

turtle.hideturtle()
turtle.bgcolor('#ba161e')  # Dark Red
turtle.setup(500, 600)
turtle.title("I AM IRONMAN")
avinash1Goto = (0, 120)
avinash2Goto = (0, -30)
avinash3Goto = (0, -220)
turtle.speed(2)


def logo(a, b):
    turtle.penup()
    turtle.goto(b)
    turtle.pendown()
    turtle.color('#fab104')  # Light Yellow
    turtle.begin_fill()

    for i in range(len(a[0])):
        x, y = a[0][i]
        turtle.goto(x, y)

    for i in range(len(a[1])):
        x, y = a[1][i]
        turtle.goto(x, y)
    turtle.end_fill()


logo(avinash1, avinash1Goto)
logo(avinash2, avinash2Goto)
logo(avinash3, avinash3Goto)
turtle.hideturtle()
turtle.done()



