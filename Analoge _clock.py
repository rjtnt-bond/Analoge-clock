from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *

class Clock:
    def __init__(self,root):
        self.root=root
        self.root.title("GUI Analog Clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        title=Label(self.root,text="RB - Clock",font=("times new roman",50,"bold"),bg="#04444a",fg="white").place(x=0,y=50,relwidth=1)
        self.lb1=Label(self.root,bg="white",bd=10,relief=RAISED)
        self.lb1.place(x=450,y=150,height=400,width=400)
        self.working()


    def clock_image(self,hr,min,sec):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(clock)

        # clock Image
        bg = Image.open("clock2.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))

        # Formula To Rotate the AntiClock
        # angle_in_radians = angle_in_degrees * math.pi/180
        # line_length = 100
        # center_x = 250
        # center_y =250
        # end_x = center_x + line_length * math.cos(angle_in_radians)
        # end_y = center_y - line_length * math.sin(angle_in_radians)

        
        # Hour Image line #
        #     x1,y1,x2,y2
        origin=200,200
        draw.line((origin, 200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
        # Min Image line#
        draw.line((origin, 200+80*sin(radians(min)),200-80*cos(radians(min))), fill="green", width=3)
        # Sec Image line#
        draw.line((origin, 200+100*sin(radians(sec)), 200-100*cos(radians(sec))), fill="blue", width=4)

        draw.ellipse((195,195,210,210), fill="black")

        clock.save("clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min=(m/60)*360
        sec=(s/60)*360
        self.clock_image(hr,min,sec)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lb1.config(image=self.img)
        self.lb1.after(200,self.working)



        # print(h, m, s)
        # print(hr,min,sec)







root=Tk()
obj=Clock(root)
root.mainloop()
