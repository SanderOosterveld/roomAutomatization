# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 09:49:35 2018

@author: Sander Oosterveld
"""
from tkinter import Label
class Widget(Label):
    classCounter = 0
    def __init__(self, master, pos, *args, **kwargs):
        '''
        pos should be a Position Object
        '''
        Label.__init__(self, master, *args, **kwargs)
        self.id = Widget.classCounter
        Widget.classCounter += 1
        self.position = pos
        
    def getId(self):
        return self.id
    
    def getPosition(self):
        return self.position
    
    def changePosition(self,newPos):
        self.position = newPos
    
    
    def make(self):
        print("placing widget at:"+ str(self.position.getXPosition()) + str(self.position.getYPosition()))
        self.place(relx = self.position.getXPosition(), rely = self.position.getYPosition(), anchor = 'center')
    
class TextWidget(Widget):
    def __init__(self, master, pos, widgetText, *args, **kwargs ):
        Widget.__init__(self, master, pos, *args, **kwargs)
        self.text = widgetText
        self.config(text = self.text)
        
    def getText(self):
        return self.text
    
    def changeText(self, newText):
        '''
        Changes the text shown by widget
        input: String
        output: void
        '''
        self.config(text = newText)

    def changeFont(self, newFont):
        '''
        Change the font of the widget in tuple with font and size
        input: Tuple(String,int)
        '''
        self.config(font = newFont)
        
    def __str__(self):
        return "Textwidget showing: " + self.text
    
    
class Position():
    def __init__(self,xpos,ypos):
        self.xPosition = xpos
        self.yPosition = ypos
        
    def getPositionRel(self):
        return (self.xPosition, self.yPosition)
    
    def getXPosition(self):
        return self.xPosition
    
    def getYPosition(self):
        return self.yPosition
    
    def movePositionUp(self,increment):
        self.yPosition -= increment
        
    def movePositionRight(self, increment):
        self.xPosition -= increment
    
    def toPixel(self):
        return (self.xPosition*1280, self.yPosition*720)
        
    def __str__(self):
        return "relX: " + str(self.xPosition)+", relY: "+str(self.yPosition)
    
        