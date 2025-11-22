import turtle
import time

# START WRITING HERE


# TURTLE GRAPHICS
screen = turtle.Screen()
screen.setup(900, 450)
screen.title("Balloon Car Race (Turtle Version)")
screen.tracer(0)

# Display calculated values ---
info = turtle.Turtle()
info.hideturtle()
info.penup()
info.goto(-420, 180)
info.write(
    f"Car 1: Velocity = {v1:.2f} m/s   Acceleration = {a1:.2f} m/s²\n"
    f"Car 2: Velocity = {v2:.2f} m/s   Acceleration = {a2:.2f} m/s²",
    font=("Arial", 14, "normal")
)

# Create cars
car1 = turtle.Turtle()
car1.shape("square")
car1.color("red")
car1.penup()
car1.goto(-400, 50)

car2 = turtle.Turtle()
car2.shape("square")
car2.color("blue")
car2.penup()
car2.goto(-400, -50)

# Finish line
finish = turtle.Turtle()
finish.hideturtle()
finish.penup()
finish.goto(300, -200)
finish.pendown()
finish.left(90)
finish.forward(400)

# Physics
start_time = time.time()
running = True

while running:
    current_time = time.time() - start_time

    # x = v*t + 0.5*a*t²
    x1 = (v1 * current_time) + 0.5 * a1 * (current_time ** 2)
    x2 = (v2 * current_time) + 0.5 * a2 * (current_time ** 2)

    # Move turtles (scale meters → pixels)
    car1.goto(-400 + x1 * 100, 50)
    car2.goto(-400 + x2 * 100, -50)

    screen.update()

    # stop when a car reaches finish line
    if car1.xcor() >= 300 or car2.xcor() >= 300:
        running = False

# --- Winner Text ---
winner = turtle.Turtle()
winner.hideturtle()
winner.penup()
winner.goto(-70, 0)

if car1.xcor() > car2.xcor():
    winner.write("Red Car Wins!", font=("Arial", 24, "bold"))
elif car2.xcor() > car1.xcor():
    winner.write("Blue Car Wins!", font=("Arial", 24, "bold"))
else:
    winner.write("It's a tie!", font=("Arial", 24, "bold"))

turtle.done()
