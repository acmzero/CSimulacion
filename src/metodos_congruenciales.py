'''
Created on 16/03/2012

@author: piter
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.form import Ui_Form
import sys

class ventanaFormi1(QWidget,Ui_Form):
  def __init__(self):
    QWidget.__init__(self)
    self.setupUi(self)
    self.x0=0.0
    self.a=0.0
    self.c=0.0
    columnas=['n','Xn','aXn+c','(aXn+c)/m','Xn+1','pseudoaleatorio']
    self.tableWidget.setColumnCount(6)
    self.tableWidget.setHorizontalHeaderLabels(columnas)
    self.pushButton.clicked.connect(self.multiplicativo_decimal)
    self.pushButton_2.clicked.connect(self.mixto_decimal)
  def multiplicativo_decimal(self):
    self.x0=float(self.lineEdit.text())
    self.a=float(self.lineEdit_2.text())
    self.lineEdit_3.setText('0')
    self.c=float(self.lineEdit_3.text())
    self.m=int(self.lineEdit_4.text())
    self.tableWidget.setRowCount(self.m)
    self.renglon=[]
    for i in range(self.m):
      
      self.renglon.append(i)
      self.renglon.append(self.x0)
      c3=self.a*self.x0+self.c
      self.renglon.append(c3)
      c4=c3/self.m
      self.renglon.append(c4)
      c5=float(str((c3%self.m)/self.m)[2])
      self.x0=c5
      self.renglon.append(c5)
      c6=c5/self.m
      self.renglon.append(c6)
      

    contador=0
    for k in self.renglon:
      qw=QTableWidgetItem(str(k))
      self.tableWidget.setItem(0,contador,qw)
      contador+=1
  def mixto_decimal(self):
    self.x0=float(self.lineEdit.text())
    self.a=float(self.lineEdit_2.text())
    
    self.c=float(self.lineEdit_3.text())
    self.m=int(self.lineEdit_4.text())
    self.tableWidget.setRowCount(self.m)
    self.renglon=[]
    for i in range(self.m):
      
      self.renglon.append(i)
      self.renglon.append(self.x0)
      c3=self.a*self.x0+self.c
      self.renglon.append(c3)
      c4=c3/self.m
      self.renglon.append(c4)
      c5=float(str((c3%self.m)/self.m)[2])
      self.x0=c5
      self.renglon.append(c5)
      c6=c5/self.m
      self.renglon.append(c6)
      

    contador=0
    for k in self.renglon:
      qw=QTableWidgetItem(str(k))
      self.tableWidget.setItem(0,contador,qw)
      contador+=1
  def multiplicativo_fraccionario(self):
    self.x0=self.lineEdit.text()
    self.a=self.lineEdit_2.text()
    self.c=0
    self.m=self.lineEdit_4.text()
  def mixto_fraccionario(self):
    self.x0=self.lineEdit.text()
    self.a=self.lineEdit_2.text()
    self.c=self.lineEdit_3.text()
    self.m=self.lineEdit_4.text()
    
    
x=QApplication(sys.argv)
y=ventanaFormi1()
y.show()
x.exec_()
