import tkinter as tk
import turtle
import math
import os

basefilename = 'tlog.txt'
root = tk.Tk()
root.title("Painting Away")
root.geometry("1000x1000")
root.resizable(0, 0)

with open('tlog.txt', 'w') as file:
    file.write('')


lbl = tk.Label(root, text = " ", borderwidth=1, fg='white', relief="solid")
lbl.place(x = 0, y = 0, width = 1800, height = 1000)
lbl.configure(bg='#4A5D23')
canvas = tk.Canvas(root)
canvas.place(x = 50, y = 50, width = 900, height = 900)
canvas.configure(bg='#8D8B55')
screen = turtle.ScrolledCanvas(canvas)
screen.place(x = 0, y = 0, width = 500, height = 900)
lbl1 = tk.Label(root, text = "Options:", borderwidth=1, fg='white', relief="solid")
lbl1.place(x = 550, y = 50, width = 400, height = 100)
lbl1.configure(bg='#7E8C54', font=("Arial", 25) )
lbl2 = tk.Label(root, text = "Drawing:", borderwidth=1, fg='white', relief="solid")
lbl2.place(x = 560, y = 160, width = 380, height = 50)
lbl2.configure(bg='#7E8C54', font=("Arial", 12) )
lbl3 = tk.Label(root, text = "Settings:", borderwidth=1, fg='white', relief="solid")
lbl3.place(x = 560, y = 560, width = 380, height = 50)
lbl3.configure(bg='#7E8C54', font=("Arial", 12) )
lbl4 = tk.Label(root, text = "Import/Export:", borderwidth=1, fg='white', relief="solid")
lbl4.place(x = 560, y = 435, width = 380, height = 50)
lbl4.configure(bg='#7E8C54', font=("Arial", 12) )
lblmv = tk.Label(root, text = "Enter Movement:", borderwidth=1, fg='white', relief="solid")
lblmv.place(x = 575, y = 250, width = 100, height = 20)
lblmv.configure(bg='#7E8C54')
lblsh = tk.Label(root, text = "Enter Sides:", borderwidth=1, fg='white', relief="solid")
lblsh.place(x = 575, y = 275, width = 100, height = 20)
lblsh.configure(bg='#7E8C54')
lblrd = tk.Label(root, text = "Enter Radius:", borderwidth=1, fg='white', relief="solid")
lblrd.place(x = 575, y = 300, width = 100, height = 20)
lblrd.configure(bg='#7E8C54')
lbldg = tk.Label(root, text = "Enter Degrees:", borderwidth=1, fg='white', relief="solid")
lbldg.place(x = 575, y = 325, width = 100, height = 20)
lbldg.configure(bg='#7E8C54')
t = turtle.RawTurtle(screen._canvas)

#drawing
fw_button = tk.Button(root, text = "Forward", command = lambda : forward(), fg='white', bg='#7E8C54')
fw_button.place(x = 575, y = 225, width = 100, height = 20)
bw_button = tk.Button(root, text = "Backward", command = lambda : backward(), fg='white', bg='#7E8C54')
bw_button.place(x = 700, y = 225, width = 100, height = 20)
mv_input = tk.Entry(root, text = "Movement", fg='white', bg='#7E8C54')
mv_input.place(x = 700, y = 250, width = 100, height = 20)
rs_button = tk.Button(root, text = "Reset", command = lambda : reset(), fg='white', bg='#7E8C54')
rs_button.place(x = 825, y = 225, width = 100, height = 20)
sh_button = tk.Button(root, text = "Draw Shape", command = lambda : shape(), fg='white', bg='#7E8C54')
sh_button.place(x = 825, y = 275, width = 100, height = 20)
sh_input = tk.Entry(root, text = "Shape", fg='white', bg='#7E8C54')
sh_input.place(x = 700, y = 275, width = 100, height = 20)
updown_button = tk.Button(root, text = "On/Off", fg='white', command = lambda : updown(), bg='#7E8C54')
updown_button.place(x = 825, y = 250, width = 100, height = 20)
dt_button = tk.Button(root, text = "Dot", command = lambda : dot(), fg='white', bg='#7E8C54')
dt_button.place(x = 825, y = 300, width = 100, height = 20)
dt_input = tk.Entry(root, text = "Radius", fg='white', bg='#7E8C54')
dt_input.place(x = 700, y = 300, width = 100, height = 20)
circle_button = tk.Button(root, text = "Circle", command = lambda : circle(), fg='white', bg='#7E8C54')
circle_button.place(x = 825, y = 325, width = 100, height = 20)
deg_input = tk.Entry(root, text = "Degree", fg='white', bg='#7E8C54')
deg_input.place(x = 700, y = 325, width = 100, height = 20)
lt_button = tk.Button(root, text = "Turn Left", command = lambda : turnl(), fg='white', bg='#7E8C54')
lt_button.place(x = 575, y = 350, width = 100, height = 20)
rt_button = tk.Button(root, text = "Turn Right", command = lambda : turnr(), fg='white', bg='#7E8C54')
rt_button.place(x = 700, y = 350, width = 100, height = 20)
turn_input = tk.Entry(root, text = "turn", fg='white', bg='#7E8C54')
turn_input.place(x = 825, y = 350, width = 100, height = 20)
#settings
bg_button = tk.Button(root, text = "Background", command = lambda : background(), fg='white', bg='#7E8C54')
bg_button.place(x = 575, y = 625, width = 100, height = 20)
bg_input = tk.Entry(root, text = "Background", fg='white', bg='#7E8C54')
bg_input.place(x = 575, y = 650, width = 100, height = 20)
spd_button = tk.Button(root, text = "Drawing Speed", command = lambda : turtlespeed(), fg='white', bg='#7E8C54')
spd_button.place(x = 700, y = 625, width = 100, height = 20)
spd_input = tk.Entry(root, text = "Drawing Speed", fg='white', bg='#7E8C54')
spd_input.place(x = 700, y = 650, width = 100, height = 20)
cl_button = tk.Button(root, text = "Color Turtle", command = lambda : color(), fg='white', bg='#7E8C54')
cl_button.place(x = 825, y = 625, width = 100, height = 20)
cl_input = tk.Entry(root, text = "Turtle Color", fg='white', bg='#7E8C54')
cl_input.place(x = 825, y = 650, width = 100, height = 20)
fl_button = tk.Button(root, text = "Fill Color Turtle", command = lambda : color(), fg='white', bg='#7E8C54')
fl_button.place(x = 825, y = 675, width = 100, height = 20)
fl_input = tk.Entry(root, text = "FTurtle Color", fg='white', bg='#7E8C54')
fl_input.place(x = 825, y = 700, width = 100, height = 20)
x_button = tk.Button(root, text = "Move X", command = lambda : movex(), fg='white', bg='#7E8C54')
x_button.place(x = 575, y = 675, width = 100, height = 20)
x_input = tk.Entry(root, text = "MoveX", fg='white', bg='#7E8C54')
x_input.place(x = 575, y = 700, width = 100, height = 20)
y_button = tk.Button(root, text = "Move Y", command = lambda : movey(), fg='white', bg='#7E8C54')
y_button.place(x = 700, y = 675, width = 100, height = 20)
y_input = tk.Entry(root, text = "MoveY", fg='white', bg='#7E8C54')
y_input.place(x = 700, y = 700, width = 100, height = 20)
#importexport
import_button = tk.Button(root, text = "Import", command = lambda : importdraw(), fg='white', bg='#7E8C54')
import_button.place(x = 575, y = 500, width = 100, height = 20)
export_button = tk.Button(root, text = "Export", command = lambda : drawex(), fg='white', bg='#7E8C54')
export_button.place(x = 700, y = 500, width = 100, height = 20)
file_input = tk.Entry(root, text = "FileName", fg='white', bg='#7E8C54')
file_input.place(x = 700, y = 525, width = 100, height = 20)
lblfile = tk.Label(root, text = "Name File:", borderwidth=1, fg='white', relief="solid")
lblfile.place(x = 575, y = 525, width = 100, height = 20)
lblfile.configure(bg='#7E8C54')


def reset():
    t.goto(0, 0)
    t.setheading(0)
    t.clear()
    with open('tlog.txt', 'w') as file:
     file.write('')
def forward():
    mvvariable = 10
    mvvariable = mv_input.get()
    if mvvariable.isdigit():
       mvvariable = int(mvvariable)
       t.forward(mvvariable)
       with open('tlog.txt', 'a') as file:
           file.write('f'+str(mvvariable)+'\n')
    else:
       t.forward(10)
       mv_input.delete(0, tk.END)
       with open('tlog.txt', 'a') as file:
           file.write('f10 \n')
    pass
def backward():
    mvvariable = 10
    mvvariable = mv_input.get()
    if mvvariable.isdigit():
       mvvariable = int(mvvariable)
       t.backward(mvvariable)
       with open('tlog.txt', 'a') as file:
           file.write('b'+str(mvvariable)+'\n')
    else:
       t.backward(10)
       mv_input.delete(0, tk.END)
       with open('tlog.txt', 'a') as file:
           file.write('b10 \n')
    pass
def background():
    bgvariable = bg_input.get()
    if bgvariable.isdigit():  
     bgvariable = str('#'+bgvariable)
     if bgvariable.startswith('#') and len(bgvariable) == 7:
        t.screen.bgcolor(bgvariable)
        with open('tlog.txt', 'a') as file:
           file.write('q'+str(bgvariable)+'\n')
     else:
        t.screen.bgcolor('white')
        with open('tlog.txt', 'a') as file:
           file.write('qwhite\n')
        bg_input.delete(0, tk.END) 
    else:
        bg_input.delete(0, tk.END) 
def turtlespeed():
    spdvariable = spd_input.get()  
    if len(spdvariable) < 4 and spdvariable.isdigit():
        spdvariable = int(spdvariable)
        t.speed(spdvariable)
        with open('tlog.txt', 'a') as file:
           file.write('a'+str(spdvariable)+'\n')
    else:
        t.speed(5)
        with open('tlog.txt', 'a') as file:
           file.write('a5\n')
        spd_input.delete(0, tk.END)   
def shape():
    sides = sh_input.get()
    if sides.isdigit():
       sides = int(sides)
       if sides >= 3:  
        angle = 360 / sides
        radius = 176.78
        length = 2 * radius * math.sin(math.pi / sides)
        t.begin_fill()
        with open('tlog.txt', 'a') as file:
           file.write('s\n')
        for _ in range(sides):
         t.fd(length)
         with open('tlog.txt', 'a') as file:
           file.write('f'+str(length)+'\n')
         t.right(angle)
         with open('tlog.txt', 'a') as file:
           file.write('r'+str(angle)+'\n')
        t.end_fill()
        with open('tlog.txt', 'a') as file:
           file.write('e\n')
       else:
        sh_input.delete(0,tk.END)   
    else:
        sh_input.delete(0,tk.END)  
def updown():   
    if t.isdown():
       t.penup()
       updown_button.configure(bg='#303030')
       with open('tlog.txt', 'a') as file:
           file.write('u\n')
    else:
       t.pendown()
       updown_button.configure(bg='#7E8C54')
       with open('tlog.txt', 'a') as file:
           file.write('d\n')
def color():
    colorvariable = cl_input.get()  
    if colorvariable.isdigit():  
     colorvariable = str('#'+colorvariable)
     if colorvariable.startswith('#') and len(colorvariable) == 7:
        t.color(colorvariable)
        with open('tlog.txt', 'a') as file:
           file.write('p'+str(colorvariable)+'\n')
     else:
        t.color('black')
        cl_input.delete(0, tk.END) 
        with open('tlog.txt', 'a') as file:
           file.write('pblack\n')
    else:
        cl_input.delete(0, tk.END)
#     
def fcolor():
    fcolorvariable = fl_input.get()  
    if fcolorvariable.isdigit() or fcolorvariable.startswith('-'):  
     fcolorvariable = str('#'+fcolorvariable)
     if fcolorvariable.startswith('#') and len(fcolorvariable) == 7:
        t.fillcolor(fcolorvariable)
        with open('tlog.txt', 'a') as file:
           file.write('i'+str(fcolorvariable)+'\n')
     else:
        t.fillcolor('')
        with open('tlog.txt', 'a') as file:
           file.write('q \n')
        fl_input.delete(0, tk.END) 
    else:
        fl_input.delete(0, tk.END)  
#   
def dot():
    fcolorvariable = fl_input.get() 
    dotradius = dt_input.get()
    if dotradius.isdigit():
       dotradius = int(dotradius)
       fcolorvariable = str('#'+fcolorvariable)
       if fcolorvariable.startswith('#') and len(fcolorvariable) == 7:
        with open('tlog.txt', 'a') as file:
           file.write('o'+str(dotradius)+','+str(fcolorvariable)+'\n')
        t.dot(dotradius, fcolorvariable)
       else:
        with open('tlog.txt', 'a') as file:
           file.write('o'+str(dotradius)+',black\n')
        t.dot(dotradius,'black')
        fl_input.delete(0, tk.END)
    else:
       dt_input.delete(0, tk.END)       
def circle():
    degreevariable = deg_input.get() 
    dotradius = dt_input.get()
    
    if dotradius.isdigit():
        dotradius = int(dotradius)
        if degreevariable.isdigit() or degreevariable.startswith('-'):
            degreevariable = int(degreevariable)
            fcolorvariable = fl_input.get()
            if fcolorvariable.isdigit():
                fcolorvariable = '#' + fcolorvariable
                if fcolorvariable.startswith('#') and len(fcolorvariable) == 7:
                    t.fillcolor(fcolorvariable)
                    with open('tlog.txt', 'a') as file:
                     file.write('i'+str(fcolorvariable)+'\n')
                else:
                    t.fillcolor('')
                    with open('tlog.txt', 'a') as file:
                     file.write('i \n')
                    fl_input.delete(0, tk.END)
            else:
                fl_input.delete(0, tk.END)
            if degreevariable >= 360 or degreevariable <= -360:
                t.begin_fill()
                with open('tlog.txt', 'a') as file:
                 file.write('s\n')
                t.circle(dotradius, degreevariable)
                with open('tlog.txt', 'a') as file:
                 file.write('c'+str(dotradius)+','+str(degreevariable)+'\n')
                t.end_fill()
                with open('tlog.txt', 'a') as file:
                 file.write('e\n')
            else:
                t.circle(dotradius, degreevariable)
                with open('tlog.txt', 'a') as file:
                 file.write('c'+str(dotradius)+','+str(degreevariable)+'\n')
        else:
            deg_input.delete(0, tk.END)
    else:
        dt_input.delete(0, tk.END)
def movex():
    xvariable = x_input.get()
    if xvariable.isdigit()  or xvariable.startswith('-'):
       xvariable = int(xvariable)
       t.penup()
       t.goto(xvariable, t.ycor())
       t.pendown
       with open('tlog.txt', 'a') as file:
           file.write('u\nx'+str(xvariable)+'\nd\n')
       updown_button.configure(bg='#7E8C54')
    else:
       x_input.delete(0, tk.END)  
def movey():
    yvariable = y_input.get()
    if yvariable.isdigit()  or yvariable.startswith('-'):
       yvariable = int(yvariable)
       t.penup()
       t.goto(t.xcor(), yvariable)
       t.pendown()
       with open('tlog.txt', 'a') as file:
           file.write('u\ny'+str(yvariable)+'\nd\n')
       updown_button.configure(bg='#7E8C54')
    else:
       y_input.delete(0, tk.END)
def turnl():
    tlvariable = 10
    tlvariable = turn_input.get()
    if tlvariable.isdigit():
       tlvariable = int(tlvariable)
       t.lt(tlvariable)
       with open('tlog.txt', 'a') as file:
           file.write('l'+str(tlvariable)+'\n')
    else:
       t.lt(10)
       turn_input.delete(0, tk.END)
       with open('tlog.txt', 'a') as file:
           file.write('l10\n')
    pass
def turnr():
    trvariable = 10
    trvariable = turn_input.get()
    if trvariable.isdigit():
       trvariable = int(trvariable)
       t.rt(trvariable)
       with open('tlog.txt', 'a') as file:
           file.write('r'+str(trvariable)+'\n')
    else:
       t.rt(10)
       turn_input.delete(0, tk.END)
       with open('tlog.txt', 'a') as file:
           file.write('r10\n')

def drawex():  
   filevariable = file_input.get()
   filevariable = str(filevariable +'.txt')
   t.goto(0, 0)
   t.setheading(0)
   t.clear()
   os.rename(basefilename,filevariable)
   with open('tlog.txt', 'w') as file:
    file.write('pblack\nq \n')

def importdraw():
  filevariable = file_input.get()
  filevariable = str(filevariable +'.txt')
  file = open(filevariable, "r")
  while regel := file.readline():
    commando = regel[0]
    argument = regel[1:].strip('\n')
    match commando:
        case 'i':
             t.fillcolor(argument)
        case 'p':
             t.pencolor(str(argument))
        case 'c':
             (rad, deg) = argument.split(',')
             t.circle(float(rad), float(deg))
        case 'u':
             t.up()
        case 'd':
             t.down()
        case 'f' :
             t.fd(float(argument))
        case 'b' :
             t.bk(float(argument))
        case 'r' :
             t.rt(float(argument))
        case 'l' :
             t.lt(float(argument))
        case 'o' :
              (radius, kleur) = argument.split(',')
              t.dot(float(radius), kleur) 
        case 's':
             t.begin_fill()
        case 'e':
             t.end_fill()
        case 'q':
             t.screen.bgcolor((argument))
        case 'a':
             t.speed(float(argument))
        case 'x':
             t.goto(int(argument), t.ycor())
        case 'y':
             t.goto(t.xcor(), int(argument))

root.mainloop()