import turtle
 
def shape():
 
    window = turtle.Screen()
    window.bgcolor("white")
 
    
 
    asdf = turtle.Turtle()
    asdf.shape("turtle")
    
    asdf.speed(500)
    for j in range(120):
        asdf.color("blue")
        for i in range(4):
            asdf.forward(100)
            asdf.right(90)
        asdf.right(1)
    for j in range(120):
        asdf.color("green")
        for i in range(4):
            asdf.forward(100)
            asdf.right(90)
        asdf.right(1)
    for j in range(120):
        asdf.color("yellow")
        for i in range(4):
            asdf.forward(100)
            asdf.right(90)
        asdf.right(1)
 
    
    window.exitonclick()
shape()