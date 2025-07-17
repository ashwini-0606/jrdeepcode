'''
--------------------------------------------
Asteroids Dodger - Jr. DEEP, the Human Computer
By: Ashwini W.            <--------------------------------- change to your group name
--------------------------------------------
Welcome aboard the HCSS (Human Computer Space Shuttle)! We are so excited to have you
joining us this week. Today, you'll be steering the HCSS to help guide us to safety.

Your Task: Control the spaceship and dodge the falling asteroids for as long as
possible without crashing. 
--------------------------------------------
FILL THE SECTION BELOW ONCE YOU HAVE FINISHED CODING YOUR GAME.
How To Play:
    - Use the ___________ keys to move your ship left, right, up, and down.
    - Avoid touching any of the asteroids that fall from the top of the screen.
    - If the ship collides with an asteroid, the game ends with a crash.
--------------------------------------------
Resources: 
    A. Get colour codes here: https://htmlcolorcodes.com/
    B. See available fonts here: https://codehs.com/documentation/new/python-turtle#docs-write
'''

import turtle, random, time   # built‑in Python modules

# Do not touch!!!!!!!!!!!!!
def draw_star(pen, size=6):
    pen.setheading(0)        
    pen.pendown()
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)       
    pen.end_fill()
    pen.penup()

def register_rocket_shape_color(screen, name, body_color, fin_color, flame_color):
    rocket = turtle.Shape('compound')

    def add_poly(points, fill, outline="white"):
        t = turtle.Turtle(visible=False)
        t.penup()
        t.begin_poly()
        for x, y in points:
            t.goto(x, y)
        t.end_poly()
        poly = t.get_poly()
        rocket.addcomponent(poly, fill, outline)

    body = [(-6, -20), (-6, 20), (-12, 20), (0, 40), (12, 20), (6, 20), (6, -20)]
    add_poly(body, body_color)

    left_fin = [(-6, -10), (-18, -25), (-6, -25)]
    add_poly(left_fin, fin_color)

    right_fin = [(6, -10), (18, -25), (6, -25)]
    add_poly(right_fin, fin_color)

    flame = [(-4, -25), (4, -25), (2, -35), (-2, -35)]
    add_poly(flame, flame_color)

    screen.register_shape(name, rocket)

def show_mission_failed():
    message = turtle.Turtle()
    message.hideturtle()
    message.penup()
    message.goto(0, 0)
    message.color("red")
    message.write("MISSION FAILED", align="center", font=("Comic Sans MS", 24, "bold"))

# PART 1: CUSTOMIZE YOUR GAME BACKGROUND !!!!!

# STEP 1: SET UP THE GAME WINDOW.
wn = turtle.Screen()
wn.title("HCSS Asteroid Dodger") # Can be changed to any title.        
wn.bgcolor("#131f4c")   # Use this website to change the color: https://htmlcolorcodes.com/
wn.setup(width=600, height=600)
wn.tracer(0)

# STEP 2: DRAW THE STARS.
starpen = turtle.Turtle()
starpen.hideturtle()
starpen.penup()
starpen.color("#d1be0a")    # Change the colour codes.

for i in range(50):           # Change the "50" to increase/decrease the number of stars.
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    starpen.goto(x, y)
    draw_star(starpen, size=8)  # Change size to increase/decrease size of stars.

# PART 2: CUSTOMIZE YOUR PLAYERS !!!!!!

# STEP 3: CUSTOMIZE SHIP 1
register_rocket_shape_color(wn, 'rocket1', '#c0392b', '#e74c3c', '#e67e22')   
register_rocket_shape_color(wn, 'rocket2', '#2980b9', '#3498db', '#f39c12')

ship1 = turtle.Turtle()
ship1.shape('rocket1')                  
ship1.penup()
ship1.goto(150, -250)
ship1.setheading(90)

ship2 = turtle.Turtle()
ship2.shape('rocket2')
ship2.penup()
ship2.goto(-150, -250)
ship2.setheading(90)

wn.update()
