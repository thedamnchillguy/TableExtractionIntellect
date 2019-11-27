# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:41:47 2019

@author: Kiran
"""

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
import random
import string
import os
def border(m=0):
    left=down=m*inch
    right=(8.27-m)*inch
    up=(11.69-m)*inch
    c.setLineWidth(random.uniform(0.5,1))
    c.line(left,down,right,down)
    c.line(right,down,right,up)
    c.line(right,up,left,up)
    c.line(left,up,left,down)
    return
    
def table(s=0):
    global cursor,font,margin
    rowsp=random.uniform(1,1.3)                    #use random float number between (0.5 and 1.5)
    colsp=random.uniform(0.4,0.5)
    row=random.randrange(3,6)
    col=random.randrange(3,6)
    tablehor=[]
    tablevert=[]
    for i in range(0,row+1):
        tablehor.append(i*rowsp*inch)
    for j in range(0,col+1):
        tablevert.append(cursor+j*colsp*inch)
    print(tablehor,tablevert)
    c.saveState()
    r=random.random()
    g=random.random()
    b=random.random()
    c.setStrokeColorRGB(r,g,b)
    c.grid(tablehor,tablevert)
    c.restoreState()
    font=int(rowsp*12)
    coordinates=[]
    coordinatespix=[]
    for i in range(row):
        for j in range(col):
            if(i<row and j<col):
                coordinates.append([(int(tablehor[i]),int(tablevert[j])),(int(tablehor[i+1]),int(tablevert[j])),(int(tablehor[i]),int(tablevert[j+1])),(int(tablehor[i+1]),int(tablevert[j+1]))])
                coordinatespix.append([(int((tablehor[i]+margin*inch)*inv),int((tablevert[j]+margin*inch)*inv)),(int((tablehor[i+1]+margin*inch)*inv),int((tablevert[j]+margin*inch)*inv)),(int((tablehor[i]+margin*inch)*inv),int((tablevert[j+1]+margin*inch)*inv)),(int((tablehor[i+1]+margin*inch)*inv),int((tablevert[j+1]+margin*inch)*inv))])
    tabletext(coordinates,tablehor,tablevert)
    cursor=tablevert[-1]+random.randrange(15,30)
    c.drawCentredString(210,cursor,"Heading")
    cursor+=30
    if s==0:
        return(coordinatespix)
    else:
        return(coordinatespix[s])
    return
        
    
def tabletext(coordinates,tablehor,tablevert):
    r=random.random()
    g=random.random()
    b=random.random()
    for i in coordinates:
        
            header=c.beginText(i[0][0]+3,i[0][1]+3)
            if i[0][1]==(int(tablevert[-2])):
                c.saveState()
                
                header.setFont(Fonts[random.randrange(len(Fonts)-1)],font)
                header.textLine("Header")
                c.drawText(header)
                c.restoreState()
                continue
            c.setFillColorRGB(r,g,b)
            header.setFont(Fonts[random.randrange(len(Fonts)-1)],font)
            header.textLine("Content")
            c.drawText(header)
    return
            
def text():
    global cursor,font
    x=random.randrange(7)
    for i in range(x):
        c.saveState()
        r=random.random()
        g=random.random()
        b=random.random()
        c.setFillColorRGB(r,g,b)
        c.setFont(Fonts[random.randrange(len(Fonts)-1)],random.randrange(10,13))
        c.drawString(0,cursor,"SomeRandomString, I know it's boring")
        
        c.restoreState()
        cursor+=font  
    return(x)
        
def drawline():
    global cursor,font
    c.saveState()
    c.setLineWidth(random.uniform(0.5,1))
    r=random.random()
    g=random.random()
    b=random.random()
    c.setStrokeColorRGB(r,g,b)
    c.line(0,cursor,450,cursor)
    cursor+=10
    return(cursor)
    

def drawimg():
    global cursor
    c.drawImage(r"C:\Users\kiran\.spyder-py3\Table Recognition\Images\image"+str(random.randrange(1,5))+".jpg",0,cursor,100,200)
    cursor+=200+5
    return
    
   
cursor=0
pixel=0.24
inv=1/pixel
Fonts=['Arial','BarlowMd','Calibri','Vera','VeraBd','VeraIt','VeraBd']
sentences=["Let's see.","Hey","I am a good boy","OOOOOOOOO"]
for i in Fonts:
    pdfmetrics.registerFont(TTFont(i,i+'.ttf'))
    
registerFontFamily('Vera',normal='Vera',bold='VeraBd',italic='VeraIt')
numberdoc=int(input("How many documents do you want?"))
n=1
exceed=noexceed=tableno=noofsentences=imageno=lineno=0
tabledoc=numberdoc

while(n<=numberdoc):    
    
    c=canvas.Canvas(r"C:\Users\kiran\.spyder-py3\Table Recognition\pdf\Test"+str(n)+".pdf")
    cursor=t=0
    pixel=0.24
    border(random.uniform(0.25,0.5))
    margin=random.uniform(0.6,1)
    c.translate(inch*margin,inch*margin)
    choose=[1,2,3,4]
    for i in range(5):
        
        if(cursor>=680):
            c.setFont(Fonts[random.randrange(len(Fonts)-1)],20)
            c.drawCentredString(220,cursor,"TITLE")
            exceed+=1
            break
        
        p=random.choice(choose)        
        
        if p==1:
            noofsentences+=text()
            
        if p==2:
            drawline()
            lineno+=1
        if p==3:
            drawimg()
            imageno+=1
        if p==4:
            t+=1
            f=open(r"C:\Users\kiran\.spyder-py3\Table Recognition\pdf\Test"+str(n)+".txt","a+")
            f.write(f"\nCoordinates:\nTable {t}")
            for item in table():
                f.write(f"\n{item}")
            
            f.close()            
            tableno+=1
    if(cursor<=680):
        c.setFont(Fonts[random.randrange(len(Fonts)-1)],20)
        c.drawCentredString(220,680,"TITLE")
        noexceed+=1
            
    
            
    c.showPage()
    c.save()
    if t==0:
        os.remove(r"C:\Users\kiran\.spyder-py3\Table Recognition\pdf\Test"+str(n)+".pdf")
        tabledoc-=1
    n+=1
    
print(f'''
      The end.
      Number of documents - cursor exceeded - {exceed}
      Number of documents within the margins - {noexceed}
      Number of tables - {tableno}
      Number of images - {imageno}
      Number of sentences - {noofsentences}
      Number of lines - {lineno}
      Number of documents with tables - {tabledoc}
      ''')


        

