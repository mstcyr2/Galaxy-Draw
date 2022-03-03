# Create your own Galaxy
# cyog.py
# Makayla St. Cyr
# mkstcyr

from graphics import *
import math
from random import randrange

win=GraphWin("Create your own Galaxy", 800, 600) # (GW)
win.setCoords(0,0,80,60)
win.setBackground("black")

outSave=open("Saves.txt", "w")
infile=open("Saves.txt","r")

# class to display saved drawings
class Drawing: #(CLOD)
    def __init__(self, color, file):
        self.color=color
        self.file=file

    def display(self):
        drwng=open(self.file, "r") # (IFL)
        winCopy=GraphWin("Drawing", 650, 450) #(GW)
        winCopy.setCoords(0,15,65,60)
        winCopy.setBackground(self.color)
        drwngObj=drwng.readlines() #(IFL)
        for i in drwngObj:
            draw=i.split("\t")
            eval(draw[0])(eval(draw[1]),winCopy)

# window that allows the user to search saved drawings
def viewSaves():
    title=Text(Point(40,50), "Saved Drawings") #(OTXT)
    title.setTextColor("white")
    title.setSize(30)
    title.draw(win)
    bButton=Rectangle(Point(35,3), Point(45,12))
    bButton.setFill("azure")
    bButton.draw(win)
    bbCenter=bButton.getCenter()
    bbLabel=Text(bbCenter, "Back") #(OTXT)
    bbLabel.setTextColor("dark cyan")
    bbLabel.draw(win)
    nameBox=Entry(Point(40,40), 20) #(IEB)
    nameBox.setText("Saved Galaxy Name")
    nameBox.setFace("helvetica")
    nameBox.setSize(28)
    nameBox.draw(win)
    nxt=Text(Point(40, 20), "Click anywhere to view!")
    nxt.setTextColor("white")
    nxt.setSize(30)
    nxt.draw(win)
    done=False
    while done==False:
        click=win.getMouse() #(IMS)
        cX=click.getX()
        cY=click.getY()
        if cX>=35 and cX<=45 and cY>=3 and cY<=12:
            clicked="back"
        else:
            clicked="any"
        
        if clicked == "any":
            name=nameBox.getText() #(IEB)
            infile=open(name+"color.txt", "r")
            color=infile.readline()
            bgColor=color.replace("\n", "")
            acc=Drawing(bgColor, name+".txt") #(CLOD)
            acc.display() 
        
        elif clicked=="back":
            done=True
            title.undraw()
            bButton.undraw()
            bbLabel.undraw()
            nameBox.undraw()
            nxt.undraw()
         
        
# starting window
def startWin():
    title=Text(Point(40,40), "Create Your Own Galaxy!") #(OTXT)
    title.setTextColor("white")
    title.setSize(36)
    title.setStyle("bold")
    title.draw(win)
    sbutton=Rectangle(Point(17,15),Point(37,25))
    sbutton.setFill("azure")
    sbutton.draw(win)
    sbCenter=sbutton.getCenter()
    sbuttonLabel=Text(sbCenter,"Start") #(OTXT)
    sbuttonLabel.setTextColor("dark cyan")
    sbuttonLabel.setSize(24)
    sbuttonLabel.draw(win)
    vbutton=Rectangle(Point(43,15), Point(63,25))
    vbutton.setFill("azure")
    vbCenter=vbutton.getCenter()
    vbuttonLabel=Text(vbCenter,"View") #(OTXT)
    vbuttonLabel.setTextColor("dark cyan")
    vbuttonLabel.setSize(24)
    vbutton.draw(win)
    vbuttonLabel.draw(win)
    click=win.getMouse()
    cX=click.getX()
    cY=click.getY()
    if cX>=17 and cX<=37 and cY>=15 and cY<=25:
        title.undraw()
        sbutton.undraw()
        sbuttonLabel.undraw()
        vbutton.undraw()
        vbuttonLabel.undraw()
        screen="draw"
    elif cX>=43 and cX<=63 and cY>=15 and cY<=25:
        title.undraw()
        sbutton.undraw()
        sbuttonLabel.undraw()
        vbutton.undraw()
        vbuttonLabel.undraw()
        screen="view"
    return screen
        
        
# window so user can name their galaxy to save it
def getName():
    bg=Rectangle(Point(0,0),Point(80,60))
    bg.setFill("black")
    bg.draw(win)
    nameBox=Entry(Point(40,40), 20) #(IEB)
    nameBox.setText("Name Your Galaxy")
    nameBox.setFace("helvetica")
    nameBox.setSize(28)
    nameBox.draw(win)
    nxt=Text(Point(40, 20), "Click anywhere to continue!") #(OTXT)
    nxt.setTextColor("white")
    nxt.setSize(30)
    nxt.draw(win)
    nameKey= win.getMouse() #(IMS)
    if nameKey!=None:
        name=nameBox.getText() #(IEB)
        nameBox.undraw()
        nxt.undraw()
        return name
    
# after saved window so user can choose to restart game or close window
def svrst():
    done= Text(Point(40,40), "Saved!") #(OTXT)
    done.setTextColor("white")
    done.setSize(36)
    rsButton=Rectangle(Point(10,5), Point(30,15))
    rsButton.setFill("white")
    rsButton.setOutline('dark cyan')
    rsCenter=rsButton.getCenter()
    rsLabel=Text(rsCenter, "Restart") #(OTXT)
    rsLabel.setTextColor("dark cyan")
    rsLabel.setSize(20)
    clsButton=Rectangle(Point(50,5), Point(70,15))
    clsButton.setFill("white")
    clsButton.setOutline('dark cyan')
    clsCenter=clsButton.getCenter()
    clsLabel=Text(clsCenter, "Close") #(OTXT)
    clsLabel.setTextColor("dark cyan")
    clsLabel.setSize(20)
    done.draw(win)
    rsButton.draw(win)
    rsLabel.draw(win)
    clsButton.draw(win)
    clsLabel.draw(win)

    click=win.getMouse() #(IMS)
    x=click.getX()
    y=click.getY()
    if x>=10 and x<=30 and y>=5 and y<=15:
        done.undraw()
        rsButton.undraw()
        rsLabel.undraw()
        clsButton.undraw()
        clsLabel.undraw()
        choice="restart"
    elif x>=50 and x<=70 and y>=5 and y<=15:
        choice="close"
    return choice


# screen to choose bg color for drawing
def colScreen():
    instr=Text(Point(40,40),"Choose a Background Color") #(OTXT)
    instr.setTextColor("white")
    instr.setSize(36)
    instr.setStyle("bold")
    instr.draw(win)
    #(LOOD)
    colorList=["powder blue","dark grey","black","dark green", "midnight blue", "indigo", "dark magenta","dark red","deep pink","hot pink","light pink","white",]
    x=12.5
    y=30
    colBox=[]
    for i in colorList: #(LOOD)
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
    rbLabel=Text(rndmButton.getCenter(),"Random") #(OTXT)
    rbLabel.setTextColor("dark cyan")
    rbLabel.draw(win)
    colPoint=win.getMouse() #(IMS)
    points=[]
    for i in colBox: #(LOOD)
        cenCol=i.getCenter()
        points.append(cenCol)
    index=0
    found=False
    while found==False:
        pt=points[index] #(LOOD)
        x1=colPoint.getX()
        y1=colPoint.getY()
        x2=pt.getX()
        y2=pt.getY()
        if math.sqrt(((x1-x2)**2)+(y1-y2)**2)<=2.50:
            bgColor=colorList[index]
            found=True
        elif x1>=30 and x1<=50 and y1>=15 and y1<=20:
            randIndex=randrange(0,12) #(RND)
            bgColor=colorList[randIndex] #(LOOD)
            found=True
        else:
            index=index+1
        if found==True:
            break
    for i in colBox: #(LOOD)
        i.undraw()
    rbLabel.undraw()
    rndmButton.undraw()
    instr.undraw()
    win.setBackground(bgColor)
    return bgColor

# functions for drawings including parameters to draw in a specific window and a user given point
# moon format
def moon(point,window):
    body=Circle(point, 3.5)
    body.setFill("gainsboro")
    body.setOutline("gray")
    bx=point.getX()
    by=point.getY()
    crater1=Circle(Point(bx-1.9, by+1.5), 1)
    crater1.setFill("gray")
    crater1.setOutline("white")
    crater2=Circle(Point(bx+.5, by-1.5), 1.4)
    crater2.setFill("gray")
    crater2.setOutline("white")
    body.draw(window)
    crater1.draw(window)
    crater2.draw(window)

# planet format
def redPlanet(point,window):
    body=Circle(point, 5)
    body.setFill("firebrick")
    body.setOutline("firebrick")
    bx=point.getX()
    by=point.getY()
    ring=Oval(Point(bx-7, by), Point(bx+7, by))
    ring.setOutline("white")
    body.draw(window)
    ring.draw(window)

# another planet format
def greenPlanet(point,window):
    body=Circle(point, 6)
    body.setFill("cornflower blue")
    body.setOutline("cornflower blue")
    bx=point.getX()
    by=point.getY()
    land=[]
    for i in range(9):
        xpt=randrange(-40,40) #(RND)
        ypt=randrange(-40,40) #(RND)
        pt=Point(bx+xpt/10, by+ypt/10)
        land.append(pt)
    grnLand=Polygon(land) #(LOOD)
    grnLand.setFill("dark green")
    grnLand.setOutline("dark green")
    body.draw(window)
    grnLand.draw(window)

#star format
def star(point,window):
    bx=point.getX()
    by=point.getY()
    starpoints=[Point(bx, by+3), Point(bx+.5, by+.5), Point(bx+3,by), Point(bx+.5, by-.5), Point(bx, by-3),Point(bx-.5, by-.5), Point(bx-3,by), Point(bx-.5, by+.5)]
    body=Polygon(starpoints) #(LOOD)
    body.setFill("yellow")
    body.setOutline("white")
    body.draw(window)
        
# set up for the drawing window
def drawWin():        
    finBar=Rectangle(Point(0,0),Point(80,15))
    finBar.setFill("azure")
    finBar.setOutline("black")
    finButton=Rectangle(Point(20,2),Point(45,13))
    finButton.setFill("dark cyan")
    finButton.setOutline("black")
    fCenter=finButton.getCenter()
    fbLabel=Text(fCenter, "Finished!") #(OTXT)
    fbLabel.setTextColor("black")
    fbLabel.setSize(30)
    rmButton=Circle(Point(55,7.5),5.5)
    rmButton.setFill("dark cyan")
    rmButton.setOutline("black")
    rmCenter=rmButton.getCenter()
    rmbLabel=Text(rmCenter, "random") #(OTXT)
    rmbLabel.setTextColor("black")
    menu=Rectangle(Point(65,0),Point(80,60))
    menu.setFill("azure")
    menu.setOutline("black")
    finBar.draw(win)
    menu.draw(win)
    finButton.draw(win)
    fbLabel.draw(win)
    rmButton.draw(win)
    rmbLabel.draw(win)
    return rmCenter

# function to draw the menu of the drawing window
def menu():
    picHolder=[]
    for i in range(4):
        holder=Circle(Point(72.5,51-i*14), 7)
        holder.setFill("white")
        holder.setOutline("black")
        picHolder.append(holder)
        holder.draw(win)
    whtCenters=[]
    for i in picHolder: #(LOOD)
        holCenter=i.getCenter()
        whtCenters.append(holCenter)
    #(LOOD)
    mn=whtCenters[0]
    rp=whtCenters[1]
    gp=whtCenters[2]
    sr=whtCenters[3]
    moon(mn,win) #(FNC)
    redPlanet(rp,win) #(FNC)
    greenPlanet(gp,win) #(FNC)
    star(sr,win) #(FNC)
    return mn, rp, gp, sr

# function to randomly place drawing objects
def randDraw():
    place=[] #(LOOD)
    plX=randrange(4,56) #(RND)
    plY=randrange(19,61) #(RND) 
    place.append(Point(plX,plY))
    p2X=randrange(5,60) #(RND)
    p2Y=randrange(20,55) #(RND) 
    place.append(Point(p2X,p2Y))
    p3X=randrange(6,59) #(RND)
    p3Y=randrange(21,54) #(RND) 
    place.append(Point(p3X,p3Y))
    p4X=randrange(3,62) #(RND)
    p4Y=randrange(18,57) #(RND) 
    place.append(Point(p4X,p4Y))
    moon(place[0],win) #(FNC)
    redPlanet(place[1],win) #(FNC)
    greenPlanet(place[2],win) #(FNC)
    star(place[3],win) #(FNC)
    return place

#set up for the screen which asks user to save drawing
def saveScreen():
    botBar=Rectangle(Point(0,0),Point(80,15))
    botBar.setFill("black")
    sideBar=Rectangle(Point(65,0),Point(80,60))
    sideBar.setFill("black")
    svButton=Rectangle(Point(10,2), Point(30,13))
    svButton.setFill("white")
    svButton.setOutline('dark cyan')
    svCenter=svButton.getCenter()
    svLabel=Text(svCenter, "Save") #(OTXT)
    svLabel.setTextColor("dark cyan")
    svLabel.setSize(20)
    rsButton=Rectangle(Point(30,2), Point(50,13))
    rsButton.setFill("white")
    rsButton.setOutline('dark cyan')
    rsCenter=rsButton.getCenter()
    rsLabel=Text(rsCenter, "Restart") #(OTXT)
    rsLabel.setTextColor("dark cyan")
    rsLabel.setSize(20)
    botBar.draw(win)
    sideBar.draw(win)
    svButton.draw(win)
    svLabel.draw(win)
    rsButton.draw(win)
    rsLabel.draw(win)

# function to return where the user wants the drawing    
def placePoint():
    place=win.getMouse() #(IMS)
    px=place.getX()
    py=place.getY()
    return place, px, py

# function that allows user to draw within one area
def userDraw():
    rmCenter=drawWin() #(FNC)
    mn, rp, gp, sr=menu()
    done=False
    drawingList=[] #(LOOD)
    placeList=[] #(LOOD)
    while done==False:
        drawing=win.getMouse() #(IMS)
        x1=drawing.getX()
        y1=drawing.getY()
        mnX=mn.getX()
        mnY=mn.getY()
        rpX=rp.getX()
        rpY=rp.getY()
        gpX=gp.getX()
        gpY=gp.getY()
        srX=sr.getX()
        srY=sr.getY()
        rmX=rmCenter.getX()
        rmY=rmCenter.getY()
        place, px, py=placePoint()
        if math.sqrt(((x1-mnX)**2)+(y1-mnY)**2)<=7:
            if px<=61.5 and px>=3.5 and py>=18.5 and py<=56.5:
                placeList.append(place)
                moon(place,win) #(FNC)
                drawingList.append("moon")
        elif math.sqrt(((x1-rpX)**2)+(y1-rpY)**2)<=7:
            if px<=60 and px>=5 and py>=20 and py<=55:
                placeList.append(place)
                redPlanet(place,win) #(FNC)
                drawingList.append("redPlanet")
        elif math.sqrt(((x1-gpX)**2)+(y1-gpY)**2)<=7:
            if px<=59 and px>=6 and py>=21 and py<=54:
                placeList.append(place)
                greenPlanet(place,win) #(FNC)
                drawingList.append("greenPlanet")
        elif math.sqrt(((x1-srX)**2)+(y1-srY)**2)<=7:
            if px>=3 and px<=62 and py>=18 and py<=57:
                placeList.append(place)
                star(place,win) #(FNC)
                drawingList.append("star")
        elif math.sqrt(((x1-rmX)**2)+(y1-rmY)**2)<=5.5:
            rndmPlace=randDraw() #(FNC)
            placeList.extend(rndmPlace)
            drawingList.extend(["moon","redPlanet","greenPlanet","star"])
        elif x1>=30 and x1<=45 and y1>=2 and y1<=13:
            done=True
            saveScreen() #(FNC)
    return drawingList, placeList

# function where user choses to either save or restart game after theyre finished           
def finished():
    drawingList, placeList=userDraw() #(FNC)
    scClick=win.getMouse() #(IMS)
    scX=scClick.getX()
    scY=scClick.getY()
    if scX>=10 and scX<=30 and scY>=2 and scY<=13:
        name=getName() #(FNC)
        outfile=open(name+".txt", "w") #(OFL)
        for i in range(len(drawingList)):
            print(drawingList[i],"\t",placeList[i], file=outfile) #(LOOD)
        outfile.close()
        return name
    elif scX>=30 and scX<=50 and scY>=2 and scY<=13:
        name= None
        bg=Rectangle(Point(0,0), Point(80,60))
        bg.setFill("black")
        bg.draw(win)
        return name
    
# main    
def main():
    if startWin()== "draw": # (FNC)
        color=colScreen() # (FNC)
    elif startWin() == "view":
        viewSaves() #(FNC)
        startWin() #(FNC)
        color=colScreen() #(FNC)
    outfile=finished() # (FNC)
    if outfile!=None:
        choice=svrst() #(FNC)
        colorFile=open(outfile+"color.txt", "w") #(OFL)
        print(color, file=colorFile)
        print(outfile, file=outSave)
        if choice=="restart":
            main()
        elif choice=="close":
            win.close()
    else:
        main()
    
    
    
main()          


