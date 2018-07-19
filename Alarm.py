# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:17:48 2018

@author: Sander Oosterveld
"""
from Widget import TextWidget, Position
from MainScreen import MainScreen
from MusicMixer import MusicMixer

class AlarmWidget(TextWidget):
    
    def __init__(self, master, alarm, *args, **kwargs):
        TextWidget.__init__(self, master, Position(0.9,0.5),"", *args, **kwargs)
        self.root = master
        self.alarm = alarm
        self.allAlarms = [self.alarm]
            
    def setNewAlarm(self, alarm):
        self.allAlarms.append(alarm)
        
    def notifyNewAlarm(self):
        self.changeText("Alarm set at" + self.getCurrentAlarm())
        self.make()
        self.root.after(3000, self.place_forget)
        
    def AlarmProtocol(self):
        def colourChanger(flag, counter, maxCounter):
            if counter < maxCounter:
                if flag == True:
                    self.root.changeBackground('white')
                    newCounter = counter + 1
                    self.root.after(500, colourChanger, False, newCounter, maxCounter)
                else:
                    self.root.changeBackground('black')
                    newCounter = counter + 1
                    self.root.after(500, colourChanger, True, newCounter, maxCounter)
            else:
                self.root.changeBackground('white')
        colourChanger(True, 0, 10)
        newMusicMixer = MusicMixer('disturbed.ogg')
        newMusicMixer.start()
        self.root.after(5000, newMusicMixer.pause())
        

class Alarm():
    
    def __init__(self, time, song, active):
        '''
        ALarm object needing three very specific entries
        String time  (e.g. 0700, 2354)
        String song (e.g disturbed.ogg)
        Boolean active (e.g. False or True)
        '''
        
        self.time = time
        self.sound = sound
        self.active = active
            
        
    def setAlarmSong(self, alarmSong):
        self.sound = alarmSong
    
    def setActive(self):
        self.active = True
    
    def setDeactive(self):
        self.active = False
        
    def changeTime(self, newTime):
        self.time = newTime
        
    def getActivity(self):
        return self.active
    
    def getTime(self):
        return self.time
    
    def getSound(self):
        return self.sound
    
    
        