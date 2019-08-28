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

class Example(QtGui.QWidget):
    #####################################设定倍率
    rate=3
    def __init__(self):
        super(Example, self).__init__()
        global vec,start
        vec=[0,0]
        start=3
        self.initUI()

    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        #####################################窗口大小
        self.setGeometry(0,0,800,0.8*800)
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
        pen=QtGui.QPen(Qt.red,10)
        pen.setCapStyle(Qt.RoundCap)
        qp.setPen(pen)
        if debug:
            print 'update'
        if start==1:
            qp.drawPoint(self.geometry().width()/2+vec[0]*Example.rate,self.geometry().height()/2+vec[1]*Example.rate)
        if start==0:
            qp.drawPoint(self.geometry().width()/2,self.geometry().height()/2)
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
    hm = pyHook.HookManager()
    hm.MouseAll=OnMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()



if __name__ == '__main__':
    t = threading.Thread(target=main2, name='mouse')
    t.start()
    main()
