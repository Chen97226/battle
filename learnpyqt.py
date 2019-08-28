#!/usr/bin/python
# -*- coding: utf-8 -*-

# calendar.py

import sys ,random
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt
import  pyHook , pythoncom
import win32api
import win32con
import threading
import time
global start,spos,vec
def OnMouseEvent(event):
    global start,spos,vec
    if event.MessageName=='mouse left down':
        start=1
        spos=event.Position
        print ( 'Position:',spos)
    if event.MessageName=='mouse left up':
        start=0
    if event.MessageName=='mouse move':
        if start == 1:
            vec[0]=event.Position[0]-spos[0]
            vec[1]=event.Position[1]-spos[1]
            print ( 'Position:',vec,spos)
    print ( 'MessageName:',event.MessageName )
    return True



class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        global vec
        sx=0
        sy=0
        spos=[0,0]
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(0,0,1000,1000)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('icons/web.png'))

        # 下面两个配合实现窗体透明和置顶
        #sizeGrip=QtGui.QSizeGrip(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow )
        #self.setMouseTracking(True);

        self.trans=False

        self.set_transparency(True)
            

    def set_transparency(self, enabled):
        if enabled:
            self.setAutoFillBackground(False)
        else:
            self.setAttribute(Qt.WA_NoSystemBackground, False)
        #下面这种方式好像不行
#        pal=QtGui.QPalette()
#        pal.setColor(QtGui.QPalette.Background, QColor(127, 127,10,120))
#        self.setPalette(pal) 
        self.setAttribute(Qt.WA_TranslucentBackground, enabled)
        self.repaint()


    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()
    def drawPoints(self, qp):
        global vec
        pen=QtGui.QPen(Qt.red,10)
        pen.setCapStyle(Qt.RoundCap)
        qp.setPen(pen)
 
           # qp.drawPoint(x, y)
        print ('paint: ',vec)
        if start==1:
            qp.drawPoint(500+vec[0],500+vec[1])
        else:
            qp.drawPoint(500,500)
        self.update()
    
    


def main():
    hm = pyHook.HookManager()
    #hm.MouseLeftDown = onMouse_leftdown
    #hm.MouseLeftUp = onMouse_leftup
    hm.MouseAll=OnMouseEvent
    hm.HookMouse()
    
    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()




if __name__ == '__main__':
    global start,spos,vec
    start=0
    spos=[0,0]
    vec=[0,0]
    t = threading.Thread(target=main, name='mouse')
    t.start()
    app = QtGui.QApplication(sys.argv)
    ex = Icon()
    ex.show()



    #QWidget::repaint()




    https://stackoverflow.com/questions/27363268/how-can-i-avoid-typeerror-mouseswitch-missing-8-required-positional-arguments
