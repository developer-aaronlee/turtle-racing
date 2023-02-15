import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)

# timmy = turtle.Turtle(shape="turtle")

# def forwards():
#     timmy.forward(10)
#
# def backwards():
#     timmy.backward(10)
#
# def counter_clockwise():
#     timmy.right(25)
#     timmy.backward(10)
#
# def clockwise():
#     timmy.left(25)
#     timmy.backward(10)
#
# def clear():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#
# screen.listen()
# screen.onkey(fun=forwards, key="w")
# screen.onkey(fun=backwards, key="s")
# screen.onkey(fun=counter_clockwise, key="a")
# screen.onkey(fun=clockwise, key="d")
# screen.onkey(fun=clear, key="c")

user_bet = screen.textinput(title="Make a Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = ["t1", "t2", "t3", "t4", "t5", "t6"]

a = -230
b = -125

for x in range(6):
    turtles[x] = turtle.Turtle(shape="turtle")
    turtles[x].color(colors[x])
    turtles[x].penup()
    turtles[x].goto(a, b)
    b += 50

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for x in turtles:
        if x.xcor() > 230:
            winning_color = x.pencolor()
            is_race_on = False
            if user_bet == winning_color:
                print(f"You win! The {winning_color} turtle is the winning winner!")
            else:
                print(f"You lose. The {winning_color} turtle is the winning winner!")
        speed = random.randint(0, 10)
        x.forward(speed)


screen.exitonclick()
