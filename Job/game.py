import turtle
import random

# Nastavení obrazovky
screen = turtle.Screen()
screen.title("Jednoduchá hra s Turtle")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)  # Vypnutí automatického vykreslování pro lepší výkon

# Hráčova želva
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.goto(0, -250)

# Cíl
goal = turtle.Turtle()
goal.shape("circle")
goal.color("green")
goal.penup()

def generate_goal_position():
    # Omezení generování pozice tak, aby nebyl cíl příliš blízko okrajům
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    if abs(x) > 250:
        x = 250 * (x // abs(x))  # Posun blíže ke středu, pokud je příliš blízko okrajům
    if abs(y) > 150:
        y = 150 * (y // abs(y))
    return x, y

goal.goto(generate_goal_position())

# Skóre
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)

# Vzdálenost pro zásah
hit_distance = 20

# Aktualizace skóre
def update_score():
    score_display.clear()
    score_display.write(f"Skóre: {score}", align="center", font=("Arial", 16, "normal"))

update_score()

# Pohyb hráče
def move_left():
    x = player.xcor()
    if x > -390:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 390:
        player.setx(x + 20)

def move_up():
    y = player.ycor()
    if y < 290:
        player.sety(y + 20)

def move_down():
    y = player.ycor()
    if y > -290:
        player.sety(y - 20)

# Ovládání
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

# Hlavní herní smyčka
def game_loop():
    global score

    # Kontrola kolize s cílem
    if player.distance(goal) < hit_distance:
        score += 1
        update_score()
        goal.goto(generate_goal_position())

    # Aktualizace obrazovky
    screen.update()

    # Naplánování další iterace smyčky
    screen.ontimer(game_loop, 50)

# Zahájení hry
game_loop()

# Ukončení
screen.mainloop()
