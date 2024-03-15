
#made by noah
#turtle grafing kalqlator
#note:angles are in radians, NOT degrees; 90 Degrees=pi/2. You are able to type pi, it will automatically convert to the radian unit.
#each grid is 50 units
import math
import cmath
import turtle as t
import time
import random as rand
grid=False
mx=0
x=960
y=500
ax="black"
pc=["red","blue","green","yellow"]
bg="white"
pxg=50
lines=1
fx=(input("Function (in terms of x) "))
while fx[0] and fx[1]=="!":
    cmd=input("Commands: \nc  | Cancel \ncss| Custom Screen Size \nsl | Set amt. of Lines # \ngr | Toggle Grid * \npc | Change Pen Color \nbg | Change Background Color \nax | Change Axis Color \ndl | View Dev Log ")
    if cmd=="css":
        x=int(input("Screen Resolution on x axis (Default=1920) "))/2
        y=int(input("Screen Resolution on y axis (Default=1080) "))/2
    elif cmd.find("sl")==0 or cmd=="lines" or cmd=="setlines":
        lines=cmd.split(" ")
        if len(lines)==2:
            lines=int(lines[1])
        else:
            print("#Enter an integer behind this command.")
    elif cmd.find("gr")==0:
        if len(cmd)!=2:
            pxg=cmd.split(" ")
            pxg=pxg[1]
        if grid:
            grid=False
        else:
            grid=True
    elif cmd.find("pc")==0:
        cmd=cmd.split(" ")
        if cmd[1]=="del":
            del(pc[-1])
        elif cmd[1]=="delall":
            pc=[]
        else:
            pc.append(cmd[1])
        print(f"Pen colors: {pc}")
    elif cmd=="bg":
        bg=input("Background Color (If it is typed wrongly, it might break the program.) ")
    elif cmd=="ax":
        ax=input("Axis Color (If it is typed wrongly, it might break the program.) ")
    elif cmd=="dl":
        file= open('graphingcalculator\changelog.txt', 'r')
        print(file.read())
    fx=input("Function in terms of x ")
if fx[0]=="!":
    fx=fx.strip("!")
    it=200
    if fx[0]=="g":
        fx=fx.strip("g")
        grid=True
    if fx.find("sin")==-1 and fx.find("cos")==-1 and fx.find("tan")==-1:
        xk=2
        yk=2
        if fx.find("^")!=-1:
            xk=20
            yk=20
    else:
        xk=math.pi*10
        yk=math.pi*10
else:
    xk=int(input("How many pixels should the X-Axis Extend Out per unit? (Default=2)"))
    yk=int(input("How many pixels should the Y-Axis Extend Out per unit? (Default=2)"))
    it=int(input("How many iterations? (Default=200)"))
pxg=2*y/(yk*10)
if xk==math.pi*10:
    pxg=math.pi
fx=list(fx)
for i in range(lines-1):
    fx.append(input(f"Function #{i+2} (in terms of x) "))
#Function to result converter
def f(q,fn):
    y=fn
    if y[0]=="x":
       y=y.replace("x","1x",1)
    if y[0]=="-" and y[1]=="x":
       y=y.replace("-x","-1x",1)
    for i in range(1):
        while y.find("x")!=-1:
            if y[y.find("x")-1].isdigit():
                y=y.replace("x","y",1)
            else:
                y=y.replace("x","z",1)
        y=y.replace("z","1x")
        y=y.replace("y","x")
    y=y.replace("x^",f"x**")
    y=y.replace("x",f"*{q}")
    y=y.replace("pi","math.pi()")
    y=y.replace("sin(","math.sin(")
    y=y.replace("cos(","math.cos(")
    y=y.replace("tan(","math.tan(")
    y=y.replace("sqrt(","cmath.sqrt(")
    if y.find("cmath.sqrt(")!=-1 and str(eval(y)).find("0j")==-1:
        return 0
    else:
        y=y.replace("cmath.sqrt(","math.sqrt(")
        y=eval(y)
        return y
def setup():
    window=t.Screen()
    window.setup(2*x,2*y,startx=None, starty=None)
    window.bgcolor(bg)
    window.title("Graphing Calculator v1.0")
    t.Pen()
    t.pencolor(ax)
    t.speed(9223372036854775807)
    t.hideturtle()
    t.setpos(0,y)
    t.setpos(0,-y)
    t.setpos(x,-y)
    t.setpos(-x,-y)
    t.setpos(-x,y)
    t.setpos(x,y)
    t.setpos(x,-y)
    t.setpos(x,0)
    t.setpos(-x,0)
    t.setpos(0,0)
def drawgrid():
    t.pencolor("lightgrey")
    t.penup()
    for i in range (math.ceil(x/xk/pxg)):
        t.goto((i+1)*xk*pxg,y)
        t.pendown()
        t.goto((i+1)*xk*pxg,-y)
        t.penup()
    for i in range (math.ceil(x/xk/pxg)):
        t.goto(-1*(i+1)*xk*pxg,y)
        t.pendown()
        t.goto(-1*(i+1)*xk*pxg,-y)
        t.penup()
    for i in range (math.ceil(y/yk/pxg)):
        t.goto(x,-1*(i+1)*yk*pxg)
        t.pendown()
        t.goto(-x,-1*(i+1)*yk*pxg)
        t.penup()
    for i in range (math.ceil(y/yk/pxg)):
        t.goto(x,(i+1)*yk*pxg)
        t.pendown()
        t.goto(-x,(i+1)*yk*pxg)
        t.penup()
def center():
    root = t.getcanvas().winfo_toplevel()
    root.update_idletasks()
    width = root.winfo_width()
    frame_width = root.winfo_rootx() - root.winfo_x()
    window_width = width + 2 * frame_width
    height = root.winfo_height()
    titlebar_height = root.winfo_rooty() - root.winfo_y()
    window_height = height + titlebar_height + frame_width
    x = root.winfo_screenwidth() // 2 - window_width // 2
    y = root.winfo_screenheight() // 2 - window_height // 2
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
setup()
center()
if grid==True:
    drawgrid()

##Graph Drawing System

t.penup()
for i in range (lines):
    if len(pc)>=i+1:
        t.pencolor(pc[i])
    else:
        t.colormode(255)
        t.pencolor(rand.randint(0,255),rand.randint(0,255),rand.randint(0,255))
    mx=-x
    t.setpos(mx,f(mx/xk,fx[i])*yk)
    t.pendown()
    for j in range (it):
        mx+=2*x/it
        t.setpos(mx,f(mx/xk,fx[i])*yk)
    t.penup()

#Text Info Drawing 
t.setpos(-3*x/4,5*y/8)
t.pendown()
t.pencolor(ax)
t.write(f"y={fx}",font=("Arial", math.floor(x/24), "normal"))
if grid:
    t.penup()
    t.setpos(-3*x/4,y/2)
    t.pendown()
    t.write(f"Each grid line represents {round(pxg,4)} units",font=("Arial", math.floor(x/48), "normal"))

#Graph Auto Shutdown Sequence
time.sleep(10)
t.bye()
#200 Lines; gg.