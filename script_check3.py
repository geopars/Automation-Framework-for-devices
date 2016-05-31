#-*- coding: UTF-8 -*- 
#!/usr/bin/env python
#Boa:PyApp:main

modules ={u'script_check3': [0, '', u'script_check3.py']}
import os
import sys
import time
#def main():
#    pass

def get_dict():
    print "sys.argv[0]:",sys.argv[0]
    path1 = os.path.abspath(sys.argv[0])
    print "path1:" ,path1
    result_path = os.path.dirname(path1)
    print result_path
    file_result_name = result_path+'\\param_demo\\param_demo.INI'
    f = file(file_result_name,'r')
    dic={}
    linenum=0.0
    while True:
        line = f.readline()                 #��ȡ�ļ�����һ��
        linenum=linenum+1
        #print '''line '%d'is:%s ''' %(linenum,line)
        if len(line)==0:
            break
        elif line=='\n':
            #print 'run to here'
            continue
        elif'#'in line:                     #������#��ʾ����һ��Э��
            index_pro=line.find('#')        
            procotol=line[index_pro+1:-1]   #���Э����
            dic[procotol]={}                #����һ��Э���ֵ���
            continue
        list=line.split('$')                #����$ʱ����ȡ���а�$���һ���б�

        length=len(list) 
        i=0
        while(length>0):
            list[i]=list[i].strip()         #ɾ���ַ��������˵Ŀհ׷�
            i=i+1
            length=length-1
        #print list
        least_argu=0
        if list[i-1] == '':
            amount=0            #����б����һ��Ԫ���ǿհף�˵����������Ϊ0
        else:
            amount=list[1].count(',')+1   #�����������Ϊ����������+1 
            default_argu=list[1].count('=')
            least_argu=amount-default_argu
        dic[procotol][list[0]]=[least_argu,amount]       #���ֵ�����Ӹ��ֵ���
    
    #print dic               
    f.close()
    #print dic
    return [dic,result_path]
def filehead(logpath):
    logpath.write('''\
    **************************
    ***                    ***
    ***                    ***
    ***      ��鱨��      ***
    ***                    ***
    ***                    ***
    **************************\n\n''')
    t=time.strftime("%y-%m-%d-%H:%M:%S",time.localtime())
    logpath.write('����ʱ�䣺'+t+'\n')
    
def check_script(to_be_che,log_dir='log.txt'):
    return_list=get_dict()
    dict_source=return_list[0]
    log_file=return_list[1]+'\\script_check.log'
    f=file(to_be_che)
    log=open(log_file,'w')
    print "create log success!"
    print 'the log path is:',log_file
    linenum=0
    log.write('Begin \t^_^ ^_^ ^_^\n')
    filehead(log)
    log.write('����������'+to_be_che+'\n\n\n\n')
    amount=0
    error_num=0
    flag=0
    while True:
        line = f.readline()
        linenum=linenum+1
        if len(line)==0:
            break
        if line.isspace()==1:
            continue 
        if '****'in line:
            if flag==0:
                flag=1
            else:
                flag=0 
            continue
        if flag==1:     
            continue
        if 'ע��' in line:
            continue
        elif'#'in line:
            index_pro=line.find('#')
            if index_pro<1:
                procotol=line[index_pro+1:-1]
                log.write('//'+str(linenum)+'//'+'OK  \t\t\t\t'+'//\t\t\t#'+procotol+'\n')
                continue
        #log.write('\nline:'+str(linenum)+'\n')
        list=line.split('$') 
        #print 'now list is',list
        #lenlist=len(list)
        list[0]=list[0].strip()
        list[1]=list[1].strip()
        #print 'now list is',list
        if list[1] == '':
            amount=0
        else:
            amount=list[1].count(',')+1
        if dict_source.get(procotol)==None:
            print 'there is no',procotol
            print 'procotol is ',procotol
        if dict_source[procotol].get(list[0])==None:
            log.write('there is no '+list[0]+'$ in #'+procotol+'\n')
            error_num=error_num+1
        elif dict_source[procotol][list[0]][0]>amount or dict_source[procotol][list[0]][1]<amount:
            log.write('//'+str(linenum)+'//'+'NG  \t')
            #log.write(line)
            #log.write('!!! the amount of arguments of \"'+list[0]+'\"is wrong !!!!!\n')
            #log.write('the amount of arguments must be at least: '+str(dict_source[procotol][list[0]][0])+' and at most: '+str(dict_source[procotol][list[0]][1])+'\n')
            log.write(''+str(amount) + '---')
            log.write('('+str(dict_source[procotol][list[0]])+')\t\t//\t\t\t\t')
            log.write(list[0]+'$\t'+list[1]+'\n')
            error_num=error_num+1
        #else:
            #log.write('the amount of'+list[0]+'are at least'+str(dict_source[procotol][list[0]][0])+'and at most'+str(dict_source[procotol][list[0]][1])+'\n')
            #log.write('your amount is'+str(amount)+'\n')
            #log.write('Done exact!\n')
            #log.write('//'+str(linenum)+'//'+'OK  \t\t\t\t'+'//\t\t\t\t')
            #log.write(list[0]+'$\t'+list[1]+'\n')
    
    log.write('\nEnd ^_^ ^_^ ^_^\n\n\n')
    
    log.write('---------------  �����ķָ���  --------------------\n\n')
    log.write('  there is '+str(error_num)+' errors in the document\n')
    log.close()
    f.close()
if __name__ == '__main__':
    #main()
    #temple=raw_input('please input the dictory of temple:')
    to_be_check=raw_input('please input the dictory of the file to be check:')
    dict=get_dict()
    #print temple
    print to_be_check
    check_script(to_be_check)
    
    #print 'main end'
        
 
        