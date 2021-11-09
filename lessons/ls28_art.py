from turtle import Turtle, done


TRUNK = 100.0
UP = 90.0

t: Turtle = Turtle()


def tree(x: float, y: float) -> None:
    t.penup() #causes not to see lines when turtle moves
    t.goto(x,y)
    t.pendown()
    branch(TRUNK, UP)
    t.getscreen().update() # updates the turtle


def branch(length: float, angle: float) -> None:
    t.setheading(angle) #angle turtle faces
    t.forward(length) #move forward
    if length < 3:
        ... # Base case do nothing:
    else: 
        #Recursive case: Branch again!
        branch(length * 0.6, angle + 25) # conditional statements add branches
        branch(length * 0.65, angle - 20)
    # Bring the turtle back to the starting point
    t.setheading(angle + 180.0) 
    t.forward(length)


if __name__ == "__main__":
    t.speed(0)
    t.getscreen().tracer(0, 0) # makes the turtle trace instantly
    t.getscreen().onclick(tree) # click screen to print trees
    done()