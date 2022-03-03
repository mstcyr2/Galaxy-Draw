from graphics import *
import math

win=GraphWin("Create your own Galaxy", 800, 600)
win.setCoords(0,0,80,60)
win.setBackground("black")

def startWin():
    # Starting window
    title=Text(Point(40,40), "Create Your Own Galaxy!")
    title.setTextColor("white")
    title.setSize(36)
    title.setStyle("bold")
    title.draw(win)
    button=Rectangle(Point(30,15),Point(50,25))
    button.setFill("azure")
    button.draw(win)
    bCenter=button.getCenter()
    buttonLabel=Text(bCenter,"Start")
    buttonLabel.setTextColor("dark cyan")
    buttonLabel.setSize(24)
    buttonLabel.draw(win)
    win.getMouse()
    title.undraw()
    button.undraw()
    buttonLabel.undraw()

def colScreen():
    # Second screen (choose color)

    instr=Text(Point(40,40),"Choose a Background Color")
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
    rbLabel=Text(rndmButton.getCenter(),"Random")
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
    print(points)
    index=0
    found=False
    while found==False:
        pt=points[index]
        if ((colPoint.getX()-pt.getX())**2 +(colPoint.getY()-pt.getY())**2)**0.5<=2.5:
            bgColor=colorList[index]
            found=True
        else:
            index=index+1
    win.setBackground(bgColor)

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
    startWin()
    colScreen()
    drawWin()
    
main()          


