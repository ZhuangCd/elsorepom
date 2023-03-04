from turtle import*

speed(20)
pensize(3)


    ##arc

colormode(255)
pencolor((255, 191, 0))

fillcolor("#FDD128")
begin_fill()

circle(90)

end_fill()

up()

    ##száj

colormode(136)
pencolor((136, 8, 8))

goto(-30, 60)
rt(90)
down()
fillcolor("#D21404")
begin_fill()

circle(30, 180)
lt(90)
fd(61)

up()

end_fill()


    ##szemek: bal

pensize(1.2)

colormode(0)
pencolor("black")

goto(-33, 110)
down()

fillcolor("white")
begin_fill()

circle(10)
up()

end_fill()


goto(-33, 110)
down()

fillcolor("blue")
begin_fill()

circle(5)
up()

end_fill()


    ##szemek: jobb


goto(33, 110)
down()

fillcolor("white")
begin_fill()

circle(10)
up()

end_fill()


goto(33, 110)
down()

fillcolor("blue")
begin_fill()

circle(5)
up()

end_fill()



hideturtle()

