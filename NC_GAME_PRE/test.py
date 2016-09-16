from turtle import Screen, Turtle, mainloop,TK  
from time import clock, sleep  
  
class MainFrm(object):  
    def __init__(self,win,pen):  
          
        self.win=win  
        self.win.bgcolor("black")  
        self.pen=pen.clone()  
        self.win.onkey(self.kbo_space, "space")  
        self.win.onkey(self.kbo_a, "a")  
        self.win.onkey(self.kbo_a, "A")  
        self.win.listen()  
        self.spacepos=self.pen.pos()  
        self.spacehead=self.pen.heading()  
        self.pen.fd(120)  
        self.apos=self.pen.pos()  
        self.ahead=self.pen.heading()  
        self.lock=0  
        self.alttemp=10  
    def kbo_space(self):  
        if self.lock==1:  
            return  
        self.lock=1  
        self.pen.up()  
        self.pen.setpos(self.spacepos)  
        self.pen.seth(self.spacehead)  
        self.pen.hideturtle()  
        self.pen.pencolor("blue")  
        self.pen.pensize(3);  
        self.pen.down()  
        self.pen.fd(self.alttemp)  
        self.pen.lt(90)  
        self.alttemp+=3  
        self.spacepos=self.pen.pos()  
        self.spacehead=self.pen.heading()  
        self.lock=0  
           
    def kbo_a(self):  
        if self.lock==1:  
            return  
        self.lock=1  
        self.pen.up()  
        self.pen.setpos(self.apos)  
        self.pen.seth(self.ahead)  
        self.pen.hideturtle()  
        self.pen.pencolor("red")  
        self.pen.pensize(2)  
        self.pen.down()  
        self.pen.dot(30)  
        self.pen.lt(79)  
        self.pen.fd(79)  
        print(self.pen.heading())  
        self.apos=self.pen.pos()  
        self.ahead=self.pen.heading()  
        self.lock=0  
def main():  
   MainFrm(Screen(),Turtle())    
   return "EVENTLOOP"  
  
if __name__ == '__main__':  
    main()  
    TK.mainloop()  # keep window open until user closes it  
