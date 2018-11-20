import turtle
#it's not going to do anything inside a function definition with no call ;)

def draw_bag():
    #turtle starts facing right at 0,0
    turtle.shape('turtle')
    turtle.pen(pencolor='orange', pensize=10)
    turtle.penup()
    turtle.goto(-35,35)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)

if __name__ == '__main__':
    turtle.setworldcoordinates(-70.,-70., 70.,70.)
    draw_bag()
    #don't close until allowed....
    turtle.mainloop()
