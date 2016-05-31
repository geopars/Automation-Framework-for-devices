#!/usr/bin/python 
#coding=gbk
import time
import win32gui
import win32ui
import win32api
import win32con
import os
from pywinauto import application
import shutil

class uninst_progam:
    def __init__(self,path):
        self.progam_path = path
        #print self.progam_path
    def uninst_EMS_client(self):
        try:
            app = application.Application.start(self.progam_path)
    
            time.sleep(5)
            print "start EMS_Client unist progam................."
            WINDOW_TITLE = u"EMS-client ж��: ȷ��ж��"
            app=application.Application().connect_(title_re = WINDOW_TITLE )
            Bunton = u'ж��(&U)'
            app[WINDOW_TITLE][Bunton].Click()
            test = 1
            while(test == 1):
                try:
                    time.sleep(1)
                    dlg=app.window_(title = u"EMS-client ж��")
                    test = 0
                except:
                    pass
                    
    
            WINDOW_TITLE = u"EMS-client ж��"
            print 'ok!!!'
            time.sleep(3)
            app[WINDOW_TITLE][u'��(&N)'].DoubleClick()
            #app[WINDOW_TITLE].TypeKeys('N')
            time.sleep(2)
            WINDOW_TITLE = u"EMS-client ж��: ȷ��ж��"
            app[WINDOW_TITLE][u'�ر�(&L)'].Click()
          
            print "uninst EMS-client complete!!!!!!!"
        except:
            print "EMS_client uninst fail!!!!"
    def uninst_EMS_server(self):
        try:
            app = application.Application.start(self.progam_path)
      
            time.sleep(5)
            print "start the EMS_server unist progam................."
            WINDOW_TITLE = u"CY-EMS-server ж��: ȷ��ж��"
            app=application.Application().connect_(title_re = WINDOW_TITLE )
            Bunton = u'ж��(&U)'
            app[WINDOW_TITLE][Bunton].Click()
            
            time.sleep(45)
    
            app[WINDOW_TITLE][u'�ر�(&L)'].DoubleClick()

            print "uninst EMS-server complete!!!!!!!"
        except:
            print "EMS_server uninst fail!!!!"
            
#��װ���ܿͻ���

class install_progam:
    def __init__(self,path,lisence_path = u'C:\\Documents and Settings\\test14\\����\\LISENCE(4).KEY'):
        self.progam_path = path
        self.lisence_path = lisence_path
       # print self.progam_path
    def install_EMS_client(self):

        try:
            if (os.path.isfile(self.progam_path) == False):
                print 'The file %s didn\'t exist!!!'% (self.progam_path)
                return

            app = application.Application.start(self.progam_path)
            time.sleep(5)
            print "start EMS_client install progam................."
            WINDOW_TITLE = u"EMS-client ��װ"
        
            app=application.Application().connect_(title_re = WINDOW_TITLE )
            Bunton = u'��һ��(&N) >'
            app[WINDOW_TITLE][Bunton].DoubleClick()
           
            time.sleep(2)
            Bunton = u'�ҽ��ܡ����֤Э�顱�е�����(&A)'
            app[WINDOW_TITLE][Bunton].DoubleClick()
            #app1[WINDOW_TITLE][Bunton].Click()
    
            Bunton = u'��һ��(&N) >'
            app[WINDOW_TITLE][Bunton].DoubleClick()


            Bunton = u'��װ(&I)'
            app[WINDOW_TITLE][Bunton].Click()


            time.sleep(50)
            print '11111111'
            Bunton = u'��һ��(&N) >'
            app[WINDOW_TITLE][Bunton].Click()
            print '22222'
            Bunton = u'�ر�'
            time.sleep(1)
            app[WINDOW_TITLE][u'�ر�'].Click()
            
            print "EMS_client install success"
            if (os.path.isfile(self.lisence_path) == False):
               print 'the lisence file isn\'t exists!!'
            else:
                #os.rename(self.lisence_path,u'D:\\CYEMS\\client\\LISENCE.KEY')
                shutil.copy(self.lisence_path,u'D:\\CYEMS\\client')
        except Exception,e:
            print 'Exception:',e
            print "EMS_client install unsuccess!!!!"
        
    def install_EMS_server(self):
        try:
            app = application.Application.start(self.progam_path)
            time.sleep(5)
            print "start EMS_server install progam................."
            WINDOW_TITLE = u"CY-EMS-server ��װ"
        
            app=application.Application().connect_(title_re = WINDOW_TITLE )
            Bunton = u'��һ��(&N) >'
            app[WINDOW_TITLE][Bunton].DoubleClick()
           
            time.sleep(2)
            Bunton = u'�ҽ��ܡ����֤Э�顱�е�����(&A)'
            app[WINDOW_TITLE][Bunton].DoubleClick()
            #app1[WINDOW_TITLE][Bunton].Click()
    
            Bunton = u'��һ��(&N) >'
            app[WINDOW_TITLE][Bunton].DoubleClick()


            Bunton = u'��װ(&I)'
            app[WINDOW_TITLE][Bunton].Click()


            time.sleep(60)

            Bunton = u'��һ��(&N) >'
            app[WINDOW_TITLE][Bunton].Click()
            
            Bunton = u'�ر�'
            app[WINDOW_TITLE][u'�ر�'].Click()

            print "EMS_server install success"
        except Exception,e:
            print 'Exception:',e
            print "EMS_server install unsuccess!!!!"
            

if __name__ == "__main__":

    EMS = u'D:\\CYEMS\\client\\uninst.exe'
    uninst1 = uninst_progam(EMS)
    uninst1.uninst_EMS_client()
    
    EMS = u'E:\\client\\EMS-client(1).exe'
    LISECE =u'E:\\client\\LISENCE.KEY'
    we = install_progam(EMS,LISECE)
    
    we.install_EMS_client()
   
    #EMS = u'D:\\CYEMS\\server\\uninst.exe'
    #uninst1 = uninst_progam(EMS)
    #uninst1.uninst_EMS_server()
    
    #EMS = u'C:\\Documents and Settings\\test14\\����\\EMS-server(2).exe'
    #we = install_progam(EMS)
    #we.install_EMS_server()

