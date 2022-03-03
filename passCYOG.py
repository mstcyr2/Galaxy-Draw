from graphics import *

win=GraphWin("CYOG", 800,600)
win.setCoords(0,0,80,60)
win.setBackground("black")

def getIndex(aList,point):
    

class Color():
    def __init__(self, index):
        self.point=self
        self.index=index
        
    def changeBg(self, aList):
        self.aList=aList
        bgColor= self.aList[self.index]
        win.setBackground(bgColor)
        

def colScreen():
    # Second screen (choose color)
    instr=Text(Point(40,40),"Choose a Background Color") #(OBTXT)
    instr.setTextColor("white")
    instr.setSize(36)
    instr.setStyle("bold")
    instr.draw(win)

    colorList=["powder blue","dark grey","black","dark green", "midnight blue", "indigo", "dark magenta","dark red","deep pink","hot pink","light pink","white",]
    x=12.5
    y=30
    colBox=[]
    for i in colorList:
        color=Circle(Point(x,y),2.5)
        colBox.append(color)
        color.setFill(i)
        color.setOutline("white")
        color.draw(win)
        x=x+5
    rndmButton=Rectangle(Point(30,15),Point(50,20))
    rndmButton.setFill("azure")
    rndmButton.setOutline("dark cyan")
    rndmButton.draw(win)
    rbLabel=Text(rndmButton.getCenter(),"Random") #(OBTXT)
    rbLabel.setTextColor("dark cyan")
    rbLabel.draw(win)
    win.getMouse()
    rbLabel.undraw()
    rndmButton.undraw()
    instr.undraw()
    for i in colBox:
        i.undraw()
    colPoint=win.checkMouse()
    points=[]
    for i in colBox:
        cenCol=i.getCenter()
        points.append(cenCol)
    

def drawWin():
    finBar=Rectangle(Point(0,0),Point(80,15))
    finBar.setFill("azure")
    finBar.setOutline("dark cyan")
    finBar.draw(win)
    menu=Rectangle(Point(65,0),Point(80,60))
    menu.setFill("azure")
    menu.setOutline("dark cyan")
    menu.draw(win)

def main():
    colScreen()
    drawWin()
    
main()
