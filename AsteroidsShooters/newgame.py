import turtle, random, time

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

def show_text(text, color="red", size=24):
    message.clear()
    message.color(color)
    message.write(text, align="center", font=("Comic Sans MS", size, "bold"))

def update_score_display():
    score_display.clear()
    score_display.write(
        f"P1: {score1} (High {high_score1})    P2: {score2} (High {high_score2})",
        align="center",
        font=("Arial", 16, "bold")
    )

# Setup
wn = turtle.Screen()
wn.title("HCSS Asteroid Dodger")
wn.bgcolor("#131f4c")
wn.setup(width=600, height=600)
wn.tracer(0)

# Stars
starpen = turtle.Turtle()
starpen.hideturtle()
starpen.penup()
starpen.color("#d1be0a")
for _ in range(50):
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    starpen.goto(x, y)
    draw_star(starpen, size=8)

# Text turtles
message = turtle.Turtle()
message.hideturtle()
message.penup()
message.goto(0, 0)

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.color("white")

# Register rockets
register_rocket_shape_color(wn, 'rocket1', '#c0392b', '#e74c3c', '#e67e22')
register_rocket_shape_color(wn, 'rocket2', '#2980b9', '#3498db', '#f39c12')

# Ships
ship1 = turtle.Turtle()
ship1.shape('rocket1')
ship1.penup()
ship1.setheading(90)

ship2 = turtle.Turtle()
ship2.shape('rocket2')
ship2.penup()
ship2.setheading(90)

# Globals
asteroids = []
score1 = 0
score2 = 0
high_score1 = 0
high_score2 = 0
running = False

def check_bounds(ship):
    x, y = ship.xcor(), ship.ycor()
    x = max(-290, min(290, x))
    y = max(-290, min(290, y))
    ship.goto(x, y)

# Movement
def go_left1(): ship1.setx(ship1.xcor() - 20); check_bounds(ship1)
def go_right1(): ship1.setx(ship1.xcor() + 20); check_bounds(ship1)
def go_up1(): ship1.sety(ship1.ycor() + 20); check_bounds(ship1)
def go_down1(): ship1.sety(ship1.ycor() - 20); check_bounds(ship1)
def go_left2(): ship2.setx(ship2.xcor() - 20); check_bounds(ship2)
def go_right2(): ship2.setx(ship2.xcor() + 20); check_bounds(ship2)
def go_up2(): ship2.sety(ship2.ycor() + 20); check_bounds(ship2)
def go_down2(): ship2.sety(ship2.ycor() - 20); check_bounds(ship2)

def bind_keys():
    wn.listen()
    wn.onkeypress(go_left1, "Left")
    wn.onkeypress(go_right1, "Right")
    wn.onkeypress(go_up1, "Up")
    wn.onkeypress(go_down1, "Down")
    wn.onkeypress(go_left2, "a")
    wn.onkeypress(go_right2, "d")
    wn.onkeypress(go_up2, "w")
    wn.onkeypress(go_down2, "s")
    wn.onkeypress(start_game, "s")

def reset_game():
    global score1, score2, asteroids, running
    score1 = 0
    score2 = 0
    update_score_display()
    ship1.goto(150, -250)
    ship2.goto(-150, -250)
    ship1.color("white")
    ship2.color("white")
    for rock in asteroids:
        rock.hideturtle()
    asteroids = []
    for _ in range(6):
        rock = turtle.Turtle()
        rock.shape("circle")
        rock.color("grey")
        rock.penup()
        rock.goto(random.randint(-280, 280), random.randint(100, 290))
        rock.speed = random.randint(2, 4)
        asteroids.append(rock)
    running = True

def start_game():
    global running
    if not running:
        reset_game()
        message.clear()
        bind_keys()
        play_game()

def play_game():
    global score1, score2, high_score1, high_score2, running

    while running:
        wn.update()

        for rock in asteroids:
            rock.sety(rock.ycor() - rock.speed)

            if rock.ycor() < -300:
                rock.goto(random.randint(-280, 280), 300)

                # Give points to whichever ship is farther from the rock
                if ship1.distance(rock) > ship2.distance(rock):
                    score1 += 1
                    if score1 > high_score1:
                        high_score1 = score1
                else:
                    score2 += 1
                    if score2 > high_score2:
                        high_score2 = score2
                update_score_display()

            if ship1.distance(rock) < 20:
                ship1.color("red")
                show_text(f"💥 P1 Crashed! 💥\nP1: {score1} (High {high_score1})\nP2: {score2} (High {high_score2})\nPress S to restart", "red", 16)
                running = False
                bind_keys()
                return

            if ship2.distance(rock) < 20:
                ship2.color("red")
                show_text(f"💥 P2 Crashed! 💥\nP1: {score1} (High {high_score1})\nP2: {score2} (High {high_score2})\nPress S to restart", "red", 16)
                running = False
                bind_keys()
                return

            if ship1.distance(ship2) < 20:
                ship1.color("red")
                ship2.color("red")
                show_text(f"💥 SHIPS COLLIDED 💥\nP1: {score1} (High {high_score1})\nP2: {score2} (High {high_score2})\nPress S to restart", "red", 16)
                running = False
                bind_keys()
                return

        time.sleep(0.02)

# Start screen
show_text("🚀 ASTEROID DODGER 🚀\nUse Arrow Keys + WASD\nPress 'S' to Start!", "yellow", 20)
bind_keys()
wn.mainloop()
