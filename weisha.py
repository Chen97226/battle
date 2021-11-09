# -*- coding: utf-8 -*-

"""
This example shows a tooltip on 
a window and a button
"""

import sys
from PyQt4 import QtGui
from PyQt4.QtCore import Qt
import threading
import  pyHook , pythoncom
from pykeyboard import *
from pymouse import *
import pyautogui
import time
# import math
import win32api
import win32con
def OnMouseEvent(event):
    global start,spos,vec
    if event.MessageName=='mouse left down':

        start=1
        vec=[0,0]
        spos=event.Position
        if debug:
            print  'Position:',spos
    if event.MessageName=='mouse left up':
        start=0
    if event.MessageName=='mouse move':
        if start == 1:
            vec[0]=event.Position[0]-spos[0]
            vec[1]=event.Position[1]-spos[1]
            #print  'Position:',vec,spos
    if debug:
        print  'MessageName:',event.MessageName
    return True
def main3():
     global down
     k=PyKeyboard()
     while True:
         if down:
             win32api.keybd_event(0x51, 0, 0, 0)
             win32api.keybd_event(0x51, 0, win32con.KEYEVENTF_KEYUP, 0)
         time.sleep(0.045)
def onKeyboardEvent(event):
    '''print "MessageName:", event.MessageName     
    print "Message:", event.Message     
    print "Time:", event.Time     
    print "Window:", event.Window     
    print "WindowName:", event.WindowName     
    print "Ascii:", event.Ascii, chr(event.Ascii)     
    print "Key:", event.Key     
    print "KeyID:", event.KeyID     
    print "ScanCode:", event.ScanCode     
    print "Extended:", event.Extended     
    print "Injected:", event.Injected     
    print "Alt", event.Alt     
    print "Transition", event.Transition     
    print "---"'''
    d=0.06
    t=0.06
    t2=0.02
    global on
    if event.Key=='Oem_3' and event.MessageName=='key up':
        if on==True:
            on=False
        else:
            on=True
    if on==False:
        return True
    #print event.Key
    global down
    if event.Key=='Lshift' and event.MessageName=='key up':
        down=False
    if event.MessageName=='key down':
        if event.Key=='Lshift' and event.MessageName=='key down'and down==False:
            down=True
            return True
        if event.Key == 'S':
            k=PyKeyboard()
            vec2=vec
            newv=[0,0]
            newv[0]=vec2[1]
            newv[1]=vec2[0]*(-1)
            addvec=[(newv[0]+vec[0])*0.5,(newv[1]+vec[1])*0.5]
            #newv[1]=math.sin(math.atan(vec2[1]/vec2[0])+math.pi/4)*(vec2[0]*vec2[0]+vec2[1]*vec2[1])**0.5
            pyautogui.moveRel(addvec[0]-vec2[0],addvec[1]-vec2[1],duration=d, tween=pyautogui.linear)
            #k.tap_key('f')
            time.sleep(t2)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t2)
            pyautogui.moveRel(addvec[0]*(-1),addvec[1]*(-1),duration=d, tween=pyautogui.linear)
            #k.tap_key('f')
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(2*t2)
            pyautogui.moveRel(vec2[0]-addvec[0],vec2[1]-addvec[1],duration=d, tween=pyautogui.linear)
            #k.tap_key('k')
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            '''win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)'''
            return True
        if event.Key == 'D':
            k=PyKeyboard()
            vec2=vec
            newv=[0,0]
            newv[0]=vec2[1]*(-1)
            newv[1]=vec2[0]
            addvec=[(newv[0]+vec[0])*0.5,(newv[1]+vec[1])*0.5]
            #newv[1]=math.sin(math.atan(vec2[1]/vec2[0])+math.pi/4)*(vec2[0]*vec2[0]+vec2[1]*vec2[1])**0.5
            pyautogui.moveRel(addvec[0]-vec2[0],addvec[1]-vec2[1],duration=d, tween=pyautogui.linear)
            #k.tap_key('f')
            time.sleep(t2)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t2)
            pyautogui.moveRel(addvec[0]*(-1),addvec[1]*(-1),duration=d, tween=pyautogui.linear)
            #k.tap_key('f')
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(2*t2)
            pyautogui.moveRel(vec2[0]-addvec[0],vec2[1]-addvec[1],duration=d, tween=pyautogui.linear)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            return True
        if event.Key == 'W':
            k=PyKeyboard()
            vec2=vec
            newvA=[0,0]
            newvB=[0,0]
            newvA[0]=vec2[1]*(-1)
            newvA[1]=vec2[0]
            newvB[0]=vec2[1]
            newvB[1]=vec2[0]*(-1)
            pyautogui.moveRel(newvA[0]-vec2[0],newvA[1]-vec2[1],duration=d, tween=pyautogui.linear)
            #k.tap_key('f')
            time.sleep(t2)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t2)
            pyautogui.moveRel(newvB[0]-newvA[0],newvB[1]-newvA[1],duration=d, tween=pyautogui.linear)
            #k.tap_key('f')
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(2*t2)
            pyautogui.moveRel(vec2[0]-newvB[0],vec2[1]-newvB[1],duration=d, tween=pyautogui.linear)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            return True
        if event.Key == 'A':
            k=PyKeyboard()
            vec2=vec
            newvA=[0,0]
            newvB=[0,0]
            newvA[0]=vec2[1]*(-1)+0.1*vec2[0]
            newvA[1]=vec2[0]+0.1*vec2[1]
            newvB[0]=vec2[1]+0.1*vec2[0]
            newvB[1]=vec2[0]*(-1)+0.1*vec2[1]
            pyautogui.moveRel(newvA[0]-vec2[0],newvA[1]-vec2[1],duration=d, tween=pyautogui.linear)
            #k.tap_key('f')
            time.sleep(t2)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t2)
            pyautogui.moveRel(newvB[0]-newvA[0],newvB[1]-newvA[1],duration=d, tween=pyautogui.linear)
            #k.tap_key('f')
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(2*t2)
            pyautogui.moveRel(vec2[0]-newvB[0],vec2[1]-newvB[1],duration=d, tween=pyautogui.linear)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(t)
            win32api.keybd_event(0x46, 0, 0, 0)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            return True
        ''' if event.Key == 'Lshift':
        if event.MessageName=='key up':
            k=PyKeyboard()
            k.tap_key('l')'''
        return True
    return True
class Example(QtGui.QWidget):
    #####################################设定倍率
    rate=3.73
    def __init__(self):
        super(Example, self).__init__()
        global vec,start
        vec=[0,0]
        start=3
        self.initUI()

    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        #####################################窗口大小
        self.setGeometry(0,0,1500,0.8*1500)
        self.setWindowTitle('Tooltips')
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)#|Qt.SubWindow )
        #####################################设定是否透明
        self.set_transparency(True)
        self.show()
        self.center()
    def set_transparency(self, enabled):
        if enabled:
            self.setAutoFillBackground(False)
        else:
            self.setAttribute(Qt.WA_NoSystemBackground, False)
        self.setAttribute(Qt.WA_TranslucentBackground, enabled)
        self.repaint()
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()
    def drawPoints(self, qp):
        #####################################设定圆圈大小
        pen=QtGui.QPen(Qt.red,26)
        pen.setCapStyle(Qt.RoundCap)
        qp.setPen(pen)
        #if debug:
        #    print 'update'
        if start==1:
            qp.drawPoint(self.geometry().width()/2+vec[0]*Example.rate,self.geometry().height()/2+vec[1]*Example.rate)
        if start==0:
            qp.drawPoint(self.geometry().width()/2,self.geometry().height()/2)
        ####################################设定刷新率
        time.sleep(0.008)    
        self.update()
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
def main2():
    global debug
    debug=False
    global start
    start=0
    global on
    on=True
    global down
    down=False
    hm = pyHook.HookManager()
    hm.MouseAll=OnMouseEvent
    hm.HookMouse()

    #监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    hm.KeyUp = onKeyboardEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()
    pythoncom.PumpMessages()



if __name__ == '__main__':

    t = threading.Thread(target=main2, name='mouse')
    t.start()
    m3 = threading.Thread(target=main3, name='ls')
    m3.start()
    main()
