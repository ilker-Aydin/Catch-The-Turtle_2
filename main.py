import turtle

import random

from random import randint

from time import time

screen = turtle.Screen()

screen.bgcolor("light blue")
FONT = ("Arial",30,"normal")
screen.title("iko games")
#score turtle
score_turtle= turtle.Turtle()
score=0

game_over=False
setting_number= 15


def setup_score_turtle():


    score_turtle.hideturtle()
    top_height= screen.window_height()

    y=top_height/2 *0.95

    score_turtle.penup()
    score_turtle.setpos(0,y)
    score_turtle.color("dark blue")

    score_turtle.write(arg="Score: 0",move=False,align="center",font=FONT)



my_turtle = turtle.Turtle()



coordinate_list=[]
x_cordinates=[-20,-10,0,10,20]
y_cordinates=[-20,-10,0,10,20]







countown_turtle = turtle.Turtle()
def countown_timer(time):
    global game_over
    countown_turtle.hideturtle()
    top_height = screen.window_height()

    y = top_height / 2 * 0.99

    countown_turtle.penup()
    countown_turtle.setpos(0, y-40)
    countown_turtle.color("dark blue")
    countown_turtle.clear()
    if time > 0:
        countown_turtle.clear()
        countown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda:countown_timer(time-1),1000)
    else:
        game_over = True
        countown_turtle.clear()
        hide_turtle()
        countown_turtle.write(arg="Time: GAME OVER", move=False, align="center", font=FONT)


def show_turtles_randomly():

    if not game_over:

        my_turtle.penup()
        x = random.choice(x_cordinates)
        y= random.choice(y_cordinates)
        my_turtle.shape("turtle")
        my_turtle.setpos(x* setting_number,y*setting_number)
        my_turtle.showturtle()
        screen.ontimer(show_turtles_randomly,1000)

        def handle_click(x,y):


            global score
            score += 1
            score_turtle.clear()
            score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)


        my_turtle.onclick(handle_click, btn=1)

def start_game():
    turtle.tracer(0)
    setup_score_turtle()

    my_turtle.hideturtle()
    countown_timer(10)
    show_turtles_randomly()

    turtle.tracer(1)

start_game()
#time_turtle
# = turtle.Turtle()

turtle.mainloop()