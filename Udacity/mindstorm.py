import turtle

def draw_square(some_turtle):

    some_turtle.shape("turtle")
    some_turtle.color("green")

    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

   

def draw_rhombus(some_turtle):
    some_turtle.shape("turtle")
    some_turtle.color("green")

    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.left(45)
        some_turtle.forward(100)
        some_turtle.left(135)

def draw_line(some_turtle):

    for i in range(1,2):
        some_turtle.right(90)
        some_turtle.forward(300)



def draw_art():
    window= turtle.Screen()
    window.bgcolor("red")

    brad= turtle.Turtle()
    brad.speed(2)

    print("Enter 1 to draw circle using square 2 to draw flower 3 to draw circle")

    ch = int(input("Enter your choice"))

    if ch==2:

        for i in range(1,37):
            draw_rhombus(brad)
            brad.right(10)
        
    
        for i in range(37,38):
           draw_line(brad)

           
    
    elif ch==1:
        for i in range(1,37):
            draw_square(brad)
            brad.right(10)
        
    
    else:
        #to draw circle
        ang=turtle.Turtle()
        ang.shape("arrow")
        ang.speed(2)
        ang.circle(150)
        
        

    

    window.exitonclick()


draw_art()
