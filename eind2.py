import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(2000)

file = open("tekening2.txt", "r")
while regel := file.readline():
    commando = regel[0]
    argument = regel[1:].strip('\n')
    match commando:
        case 'i':
             t.fillcolor(argument)
        case 'p':
             t.pencolor(argument)
        case 'c':
             (rad, deg) = argument.split(',')
             t.circle(float(rad), float(deg))
        case 'u':
             t.up()
        case 'd':
             t.down()
        case 'g':
             (x, y) = argument.split(',')
             t.goto(float(x), float(y))
        case 'f' :
             t.fd(float(argument))
        case 'b' :
             t.bk(float(argument))
        case 'r' :
             t.rt(float(argument))
        case 'l' :
             t.lt(float(argument))
        #case 'o' :
              # (radius, kleur) = argument.split(',')
              # t.dot(float(radius), kleur) 
        case 'o' :
             t.dot(float(argument))
        case 's':
             t.begin_fill()
        case 'e':
             t.end_fill()
turtle.mainloop()