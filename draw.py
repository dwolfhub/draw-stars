from turtle import *
from math import pi, sin, cos

def draw_odd_pointed_star(p, r):
    points = [(r * cos(i * 2 * pi / p), r * sin(i * 2 * pi / p)) for i in range(p)]

    penup()
    goto(points[0][0], points[0][1])
    pendown()
    current_point_index = 0
    next_point_increment = p // 2

    for i in range(p):
        current_point_index = current_point_index + next_point_increment
        if current_point_index > p - 1:
            current_point_index = current_point_index - p

        goto(points[current_point_index][0], points[current_point_index][1])

    done()

def draw_even_pointed_star(p, r):
    p = p // 2
    points = [(r * cos(i * 2 * pi / p), r * sin(i * 2 * pi / p)) for i in range(p)]

    penup()
    goto(points[0][0], points[0][1])
    pendown()

    current_point_index = 0
    next_point_increment = 1

    for i in range(p):
        current_point_index = current_point_index + next_point_increment
        if current_point_index > p - 1:
            current_point_index = current_point_index - p

        goto(points[current_point_index][0], points[current_point_index][1])

    points = [(r * cos((i + .5) * 2 * pi / p), r * sin((i + .5) * 2 * pi / p)) for i in range(p)]
    
    penup()
    goto(points[0][0], points[0][1])
    pendown()

    current_point_index = 0
    next_point_increment = 1

    for i in range(p):
        current_point_index = current_point_index + next_point_increment
        if current_point_index > p - 1:
            current_point_index = current_point_index - p

        goto(points[current_point_index][0], points[current_point_index][1])

    done()
        

p = 32
r = 200

if p % 2 == 1:
    draw_odd_pointed_star(p, r)
else:
    draw_even_pointed_star(p, r)
