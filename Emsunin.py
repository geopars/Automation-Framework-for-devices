#!/usr/bin/python 
#coding=gbk
import time
import win32gui
import win32ui
import win32api
import win32con
import os
import shutil
import sys
from pywinauto import application
from pywinauto.controls import HwndWrapper
from pywinauto import *

class uninst_progam:
    def __init__(self,path):
        self.progam_path = path
        #print self.progam_path
    def uninst_EMS_client(self):
        try:
            if (os.path.isfile(self.progam_path) == False):
                print 'The file %s didn\'t exist!!!'% (self.progam_path)
                return
            app = application.Application.start(self.progam_path)
            if (os.path.isfile(self.progam_path) == False):
                print 'The file %s didn\'t exist!!!'% (self.progam_path)
                return
            time.sleep(5)
            #print "start EMS_Client unist progam................."
            WINDOW_TITLE = u"EMS-client ж��: ȷ��ж��"
            app=application.Application().connect_(title_re = WINDOW_TITLE )
            Bunton = u'ж��(&U)'
            app[WINDOW_TITLE][Bunton].Click()
            #KEY_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
            #strTime = time.strftime(KEY_TIME_FORMAT)
            #print strTime
            #WINDOW_TITLE = u"EMS-client ж��: ж���ļ�"
            #app[u"EMS-client ж��"].Wait('exists',40)
            WINDOW_TITLE = u"EMS-client ж��"
            cnt = 0
            while cnt<60:
                try:
                    tmp_list = findwindows.find_windows(title=WINDOW_TITLE)
                    #print 'tmp_list:',tmp_list
                    if len(tmp_list)>0:
                        #print 'find the windows title:',WINDOW_TITLE
                        break
                except Exception,e:
                    cnt = cnt + 1
                    time.sleep(1)
                        #print 'not find : ' ,cnt,'  times' 
                    pass    
            #time.sleep(20)
            #strTime = time.strftime(KEY_TIME_FORMAT)
            #print strTime
            
            #app=application.Application().connect_(title_re=WINDOW_TITLE )
            app[WINDOW_TITLE][u'��(&N)'].Click()

            time.sleep(2)
            WINDOW_TITLE = u"EMS-client ж��: ���"
            app[WINDOW_TITLE][u'�ر�(&L)'].Click()
          
            return "uninst EMS-client complete!!!!!!!"
        except Exception,e:
            print 'Exception:',e
            return "EMS_client uninst fail!!!!"
    def uninst_EMS_server(self):
        try:

            if (os.path.isfile(self.progam_path) == False):
                print 'The file %s didn\'t exist!!!'% (self.progam_path)
                return
            app = application.Application.start(self.progam_path)
            time.sleep(5)
            #print "start the EMS_server unist progam................."
            WINDOW_TITLE = u"CY-EMS-server ж��: ȷ��ж��"
            app=application.Application().connect_(title_re = WINDOW_TITLE )
            Bunton = u'ж��(&U)'
            app[WINDOW_TITLE][Bunton].Click()
            time.sleep(2)
            
            WINDOW_TITLE = u'CY-EMS-server ж��: ж���ļ�'
            Button = u'�ر�(&L)'
            Button_Property = HwndWrapper.HwndWrapper(app[WINDOW_TITLE][Button]).GetProperties()
            while(Button_Property['IsEnabled'] == False):
                time.sleep(1)
                Button_Property = HwndWrapper.HwndWrapper(app[WINDOW_TITLE][Button]).GetProperties()
                #print Button_Property['IsEnabled']
                
            WINDOW_TITLE = u'CY-EMS-server ж��: ���'
            app[WINDOW_TITLE][u'�ر�(&L)'].DoubleClick()

            return "uninst EMS-server complete!!!!!!!"
        except Exception,e:
            print 'Exception:',e
            return "EMS_server uninst fail!!!!"
            
#��װ���ܿͻ���

class install_progam:
    def __init__(self,path,lisence_path = u'C:\\Documents and Settings\\dell\\����\\LISENCE(4).KEY'):
        self.progam_path = path
        self.lisence_path = lisence_path
    def install_EMS_client(self):
        try:
            reload(sys)
            sys.setdefaultencoding('utf-8')
            if (os.path.isfile(self.progam_path) == False):
                print 'The file %s didn\'t exist!!!'% (self.progam_path)
                return

            app = application.Application.start(self.progam_path)
            time.sleep(5)
            #print "start EMS_client install progam................."
            WINDOW_TITLE = u"EMS-client ��װ"
        
            app=application.Application().connect_(title_re = WINDOW_TITLE )
            Bunton = u'��һ��(&N) >'
            app[WINDOW_TITLE][Bunton].DoubleClick()
            WINDOW_TITLE = u'EMS-client ��װ: ������Э��'
            #time.sleep(2)
            Bunton = u'�ҽ��ܡ����֤Э�顱�е�����(&A)'
            app[WINDOW_TITLE][Bunton].DoubleClick()
            Bunton = u'��һ��(&N) >'
            app[WINDOW_TITLE][Bunton].Click()
            WINDOW_TITLE = u'EMS-client ��װ: ѡ��װλ��'
            Bunton = u'��һ��(&N) >'
            app[WINDOW_TITLE][Bunton].Click()
            WINDOW_TITLE = u'EMS-client ��װ: ѡ�񡰿�ʼ�˵����ļ���'
            Button = u'��װ(&I)'
            app[WINDOW_TITLE][Button].Click()

    
            #time.sleep(2)
            WINDOW_TITLE = u'EMS-client ��װ: �����ļ�'
            Button = u'��һ��(&N) >'   
            Button_Property = HwndWrapper.HwndWrapper(app[WINDOW_TITLE][Button]).GetProperties()
            while(Button_Property['IsEnabled'] == False):
                time.sleep(1)
                Button_Property = HwndWrapper.HwndWrapper(app[WINDOW_TITLE][Button]).GetProperties()
                
            WINDOW_TITLE = u'EMS-client ��װ: �����'
            app[WINDOW_TITLE][Bunton].Click()
            
            WINDOW_TITLE = u'EMS-client ��װ: �����'
            Bunton = u'�ر�'
            app[WINDOW_TITLE][u'�ر�'].Click()

            return "EMS_client install success"
            shutil.copy(u'D:\\CYEMS\\client\\bin\\start.bat',u'D:\\CYEMS\\client')
            if (os.path.isfile(self.lisence_path) == False):
                return 'the lisence file isn\'t exists!!'
            else:
                shutil.copy(self.lisence_path,u'D:\\CYEMS\\client')
        except Exception,e:
            print 'Exception:',e
            return "EMS_client install unsuccess!!!!"
        
    def install_EMS_server(self):
        try:
            if (os.path.isfile(self.progam_path) == False):
                print 'The file %s didn\'t exist!!!'% (self.progam_path)
                return
            app = application.Application.start(self.progam_path)
            time.sleep(5)
            #print "start EMS_server install progam................."
            WINDOW_TITLE = u"CY-EMS-server ��װ"
            app=application.Application().connect_(title_re = WINDOW_TITLE )
            Bunton = u'��һ��(&N) >'
            app[WINDOW_TITLE][Bunton].Click()
            
            WINDOW_TITLE = u"CY-EMS-server ��װ: ������Э��"
            #time.sleep(2)
            Bunton = u'�ҽ��ܡ����֤Э�顱�е�����(&A)'
            app[WINDOW_TITLE][Bunton].DoubleClick()
            Bunton = u'��һ��(&N) >'
            app[WINDOW_TITLE][Bunton].Click()
            
            WINDOW_TITLE = u"CY-EMS-server ��װ: ѡ��װλ��"   
            Bunton = u'��һ��(&N) >'
            app[WINDOW_TITLE][Bunton].Click()

            WINDOW_TITLE = u"CY-EMS-server ��װ: ѡ�񡰿�ʼ�˵����ļ���"
            Bunton = u'��װ(&I)'
            app[WINDOW_TITLE][Bunton].Click()


            #time.sleep(1)
            WINDOW_TITLE = u"CY-EMS-server ��װ: �����ļ�"
            Button = u'��һ��(&N) >'
            Button_Property = HwndWrapper.HwndWrapper(app[WINDOW_TITLE][Button]).GetProperties()
            while(Button_Property['IsEnabled'] == False):
                time.sleep(1)
                Button_Property = HwndWrapper.HwndWrapper(app[WINDOW_TITLE][Button]).GetProperties()
                
            #time.sleep(1)
            WINDOW_TITLE = u"CY-EMS-server ��װ: �����"
            app[WINDOW_TITLE][Button].Click()
            
            Bunton = u'�ر�'
            WINDOW_TITLE = u"CY-EMS-server ��װ: ��װ���"
            app[WINDOW_TITLE][u'�ر�'].Click()

            return "EMS_server install success"
        except Exception,e:
            print 'Exception:',e
            return "EMS_server install unsuccess!!!!"
            

if __name__ == "__main__":

    EMS = u'D:\\CYEMS\\client\\uninst.exe'
    uninst1 = uninst_progam(EMS)
    result = uninst1.uninst_EMS_client()
    print result
    
    EMS = u'E:\\client\\EMS-client(1).exe'
    we = install_progam(EMS)
    result = we.install_EMS_client()
    print result

    '''
    EMS = u'D:\\CYEMS\\server\\uninst.exe'
    uninst1 = uninst_progam(EMS)
    result = uninst1.uninst_EMS_server()
    print result
    
    EMS = u'C:\\Documents and Settings\\dell\\����\\EMS-server(2).exe'
    we = install_progam(EMS)
    result = we.install_EMS_server()
    print result
    '''

