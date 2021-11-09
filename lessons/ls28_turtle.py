from turtle import Turtle, done

em: Turtle = Turtle()
i: int = 0
while i < 6:
    em.forward(i * 2)
    em.left(90)
    i += 1 # to prevent infinite loop

while i < 4:
    em.forward(100)
    em.left(90)


done()