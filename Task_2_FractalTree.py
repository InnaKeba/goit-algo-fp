import turtle
import math

def pythagoras_tree_lines(t, branch_length, level, max_level):
    if level == 0:
        return

    # гра з кольорами на різних рівнях
    base_color_r, base_color_g, base_color_b = 128, 0, 128
    color_intensity_factor = 1 - (max_level - level) / (max_level * 1.2)
    current_r = int(base_color_r * color_intensity_factor + 255 * (1 - color_intensity_factor))
    current_g = int(base_color_g * color_intensity_factor + 255 * (1 - color_intensity_factor))
    current_b = int(base_color_b * color_intensity_factor + 255 * (1 - color_intensity_factor))
    t.pencolor((min(255, current_r), min(255, current_g), min(255, current_b)))

    t.pensize(max(1, level * 0.6))

    t.forward(branch_length)
    pos = t.position()
    head = t.heading()

    new_branch_length = branch_length * 0.75

    # Ліва гілка
    t.left(35)
    pythagoras_tree_lines(t, new_branch_length, level - 1, max_level)
    t.penup()
    t.goto(pos)
    t.setheading(head)
    t.pendown()

    # Права гілка
    t.right(35)
    pythagoras_tree_lines(t, new_branch_length, level - 1, max_level)

    t.penup()
    t.goto(pos)
    t.setheading(head)
    t.pendown()
    t.backward(branch_length)

def setup_tree_lines(max_level):
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Фрактал 'Дерево Піфагора' (Лінії) - Python Turtle")
    screen.colormode(255)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed('fastest')
    t.penup()
    t.goto(0, -300)
    t.setheading(90)
    t.pendown()
    t.pencolor(128, 0, 128)

    screen.tracer(0, 0)
    pythagoras_tree_lines(t, 100, max_level, max_level)
    screen.tracer(1, 1)
    screen.mainloop()

while True:
    try:
        level_input = input("Введіть рівень рекурсії (рекомендовано 8–10): ")
        recursion_level = int(level_input)
        if recursion_level < 1:
            print("Рівень рекурсії має бути додатним числом.")
            continue
        break
    except ValueError:
        print("Невірний ввід. Введіть ціле число.")

setup_tree_lines(recursion_level)