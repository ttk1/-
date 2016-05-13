from Tkinter import *

root = Tk()
c0 = Canvas(root,width=200,height=200)
click = 0
x_old = None
y_old = None

def callback1(event):
    global x_old,y_old
    if click == 1:
        c0.create_line(event.x,event.y,x_old,y_old)
    x_old = event.x
    y_old = event.y
    
def callback2(event):
    global click,x_old,y_old
    click = 1
    x_old = event.x
    y_old = event.y
    
def callback3(event):
    global click
    click = 0
    
def my_save(event):
    c0.postscript(file='tmp.ps')
    c0.delete('all')

c0.bind('<Motion>',callback1)
c0.bind('<Button-1>',callback2)
c0.bind('<ButtonRelease-1>',callback3)
c0.bind('<Button-3>',my_save)

c0.pack()

c0.postscript(file='out.ps')
root.mainloop()

