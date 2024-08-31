import turtle
import colorsys

# Set up the screen and turtle
tu = turtle.Turtle()
screen = tu.getscreen()
screen.bgcolor("black")
tu.pensize(2)
tu.left(90)
tu.backward(100)
tu.speed(0)  # Set speed to maximum
tu.shape("turtle")

# Function to draw the tree with dynamic colors
def tree(i, level):
    if i < 10:
        return
    else:
        # Calculate color based on level using colorsys
        hue = (level / 10) % 1.0  # Loop hue between 0 and 1
        color = colorsys.hsv_to_rgb(hue, 0.8, 0.8)  # Softer colors
        tu.color(color)
        
        tu.forward(i)
        tu.left(30)
        tree(3 * i / 4, level + 1)
        tu.right(60)
        tree(3 * i / 4, level + 1)
        tu.left(30)
        tu.backward(i)

# Start drawing the tree with the initial length and level
tree(100, 0)
turtle.done()
