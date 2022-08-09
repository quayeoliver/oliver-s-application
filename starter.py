import turtle
import random
track = turtle.getscreen()
turtle.bgcolor("black")
racer_1 = turtle.Turtle()
racer_2 = turtle.Turtle()
climax_point = turtle.Turtle()


def track_setup():
    climax_point.penup()
    climax_point.shape("square")
    climax_point.pensize(5)
    climax_point.goto(-250, 170)
    climax_point.fd(500)
    climax_point.rt(90)
    climax_point.pendown()
    climax_point.color("white")
    climax_point.fd(250)

    racer_1.penup()
    racer_1.shape("turtle")
    racer_1.pensize(10)
    racer_1.fillcolor("green")
    racer_1.goto(-270, 80)
    racer_1.pendown()

    racer_2.penup()
    racer_2.shape("turtle")
    racer_2.pensize(10)
    racer_2.fillcolor("blue")
    racer_2.goto(-270, 10)
    racer_2.pendown()


def sprint():
    acceleration = [1, 2, 3, 4, 5, 6]
    moves = 1
    finish_1 = 0
    finish_2 = 0

    input("press enter to start race: ")
    while moves <= 20:
        print(f"moves:{moves}")
        input("racer_1 move.press enter to run: ")
        first_outcome = random.choice(acceleration)
        distance_1 = first_outcome * 20
        print(f"your outcome is {first_outcome}.racer_1 moves {distance_1} steps")
        racer_1.penup()
        racer_1.fd(distance_1)
        finish_1 += distance_1

        input("racer_2 move.press enter to run: ")
        second_outcome = random.choice(acceleration)
        distance_2 = second_outcome * 20
        print(f"your outcome is {second_outcome}.racer_2 moves{distance_2} steps ")
        racer_2.penup()
        racer_2.fd(distance_2)
        finish_2 += distance_2
        moves +=1

        if finish_1 >= 500:
            print("racer_1 wins")
            break
        elif finish_2 >= 500:
            print("racer_2 wins")
            break
        elif moves > 20:
            print("you've run out of moves!!")
            break




track_setup()
sprint()
track.exitonclick()


