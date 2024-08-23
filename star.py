import turtle
import colorsys
import random

# Setup turtle
turtle.setup(800, 800)
turtle.speed('fastest')
turtle.bgcolor("black")
turtle.title("Amazing Star")

def draw(n, x, angle):
    for i in range(n):
        # Konversi warna dari HSV ke RGB
        hue = i / n  # Mengubah hue berdasarkan iterasi
        saturation = 1.0
        value = 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
        
        # Set color
        turtle.pencolor(r, g, b)
        turtle.fillcolor(r, g, b)
        
        turtle.begin_fill()
        for j in range(5):
            turtle.forward(5 * n - 5 * i)
            turtle.right(x)
            turtle.forward(5 * n - 5 * i)
            turtle.right(72 - x)
        turtle.end_fill()
        turtle.right(angle)

# Parameters
n = 30
x = 144
angle = 18

# Draw the star
draw(n, x, angle)

turtle.done()
