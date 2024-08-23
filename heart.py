import math
from turtle import *
import colorsys

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)
bgcolor("black")

# Draw the heart shape
for i in range(6000):
    # Calculate the position
    x = hearta(i) * 20
    y = heartb(i) * 20
    
    # Set color using HSV to RGB conversion
    hue = i / 6000  # Vary the hue based on the iteration
    saturation = 1.0
    value = 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
    
    color(r, g, b)
    goto(x, y)
    # Draw line segments to create the shape
    pendown()
    goto(0, 0)
    penup()

done()
