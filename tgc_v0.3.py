#made by noah
#turtle grafing kalqlator
#bugs: x doenst work (do "--x") need to add screen size fitting to the xy axis
#note:angles are in radians, NOT degrees; 90 Degrees=pi/2. You are able to type pi, it will automatically convert to the radian unit.
#other minor bugs
import math
import turtle as t
import time
mx=0
x=960
y=500
ax="black"
pc="red"
bg="white"
fx=input("Function (in terms of x) ")
while fx[0] and fx[1]=="!":
    cmd=input("Commands: \nc | Cancel \ncss | Custom Screen Size \npc | Change Pen Color \nbg | Change Background Color \nax | Change Axis Color \ndl | View Dev Log ")
    if cmd=="css":
        x=int(input("Screen Resolution on x axis (Default=1920) "))/2
        y=int(input("Screen Resolution on y axis (Default=1080) "))/2
    elif cmd=="pc":
        pc=input("Pen Color (If it is typed wrongly, it might break the program.) ")
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
    if fx.find("sin") or fx.find("cos") or fx.find("tan"):
        xk=math.pi*12
        yk=24
    else:
        xk=2
        yk=2
else:
    xk=int(input("How many pixels should the X-Axis Extend Out per unit? (Default=12)"))
    yk=int(input("How many pixels should the Y-Axis Extend Out per unit? (Default=12)"))
    it=int(input("How many iterations? (Default=200)"))
def f(x):
    y=fx
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
    y=y.replace("x",f"*{x}")
    y=y.replace("pi","math.pi()")
    y=y.replace("sin(","math.sin(")
    y=y.replace("cos(","math.cos(")
    y=y.replace("tan(","math.tan(")
    y=eval(str(y))
    return y
def setup():
    window=t.Screen()
    window.setup(2*x,2*y,startx=None, starty=None)
    window.bgcolor(bg)
    window.title("Graphing Calculator v0.2")
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
t.pencolor(pc)
for i in range (math.ceil(it/2)):
    t.setpos(mx,f(mx/xk)*yk)
    mx+=x/math.ceil(it/2)
mx=0
t.penup()
t.setpos(0,0)
t.pendown()
for i in range (math.ceil(it/2)):
    t.setpos(mx,f(mx/xk)*yk)
    mx+=-1*x/math.ceil(it/2)
t.penup()
t.setpos(-3*x/4,y/2)
t.pendown()
t.pencolor(ax)
t.write(f"y={fx}",font=("Arial", math.floor(x/24), "normal"))
#Graph Auto Shutdown Sequence
time.sleep(5)
t.bye()