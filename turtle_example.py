import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    #create a turtle brad - Draws a square
    brad = turtle.Turtle()  #grab the turtle / to start drawing.
    brad.shape("turtle")
    brad.color("orange")
    brad.speed(5)
    
    for i in range(1, 37):   #repeats the drawing of the square moving a few degrees
        draw_square(brad)
        brad.right(10)
        
    #Create the turtle angie - draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    
    lucas = turtle.Turtle()
    lucas.shape("turtle")
    lucas.color("yellow")
    lucas.triangle(100)

    window.exitonclick() 

draw_square()
