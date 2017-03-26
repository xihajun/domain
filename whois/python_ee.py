# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 15:57:02 2017

@author: superfan
"""
import requests
import re
import string

def getHTMLText(url):
    kv = {'user-agent':'Mozilla/5.0'}
    try:
        r = requests.get(url, headers = kv, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

    
def parsePage(ilt,html):
    try:
        day = re.findall(r'expire:.*\d{4}\-\d{2}\-\d{2}',html);
        dom = re.findall(r'Domain:.*name.*\d{3}.ee',html)
        print dom,dayly
    except:
        print("异常")

def main(): 
    m = open("domain.txt")
    strin = m.read()
    pool=strin.split('\r\n')
    m.close()
    print pool
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                pool.append(str(i)+str(j)+str(k))
    start_url = 'http://whois.chinaz.com/'
    kv = {'user-agent':'Mozilla/5.0'}
    f = open("new1.txt", "a")
    tool = []
    for i in pool:
        try:
            url = start_url +str(i) + '.ee'
            html = getHTMLText(url)
            domain = re.findall(ur'<title>.*?\.ee',html)
            domain = re.sub(ur'<title>',"",domain[0])
            try:  
                create_day = re.findall(ur'\u521b\u5efa\u65f6\u95f4.*?\d{4}\u5e74\d{2}\u6708\d{2}\u65e5',html)
                create_day = re.sub(ur'<.*>',"",create_day[0])
                expire_day = re.findall(ur'\u8fc7\u671f\u65f6\u95f4.*?\d{4}\u5e74\d{2}\u6708\d{2}\u65e5',html)
                expire_day = re.sub(ur'<.*>',"",expire_day[0])
                temp = [domain+create_day+expire_day+'\n']
                a = temp[0]
                #print type(a)
                ##print a
                #print type(a)
                f.write(a.encode('utf-8'))
            except:
                unr = re.findall(ur'\u672a\u88ab\u6ce8\u518c\u6216\u88ab\u9690\u85cf',html)
                if len(unr):
                    ##print domain,unr[0]
                    temp = [domain+unr[0]+'\n']
                    a = temp[0]
                    f.write(a.encode('utf-8'))
                    #temp = ['未注册：'+" "+i+" "+'快去注册吧！！！']
                    #print>>f,temp[0]
                else:
                    ##print domain,"错误"
                    f.write("网络超时或服务器错误\n")
                    tool.append("http://whois.chinaz.com/"+domain)
                    #temp = ['未知错：'+" "+i+" "+'再试试？？']
                    #print>>f,temp[0]
            #parsePage(infoList,html)
        except:
            continue
    for i in tool:
        print("错误校准中。。。")
        html = getHTMLText(i)
        domain = re.findall(ur'<title>.*?\.ee',html)
        domain = re.sub(ur'<title>',"",domain[0])
        try:        
            try:  
                create_day = re.findall(ur'\u521b\u5efa\u65f6\u95f4.*?\d{4}\u5e74\d{2}\u6708\d{2}\u65e5',html)
                create_day = re.sub(ur'<.*>',"",create_day[0])
                expire_day = re.findall(ur'\u8fc7\u671f\u65f6\u95f4.*?\d{4}\u5e74\d{2}\u6708\d{2}\u65e5',html)
                expire_day = re.sub(ur'<.*>',"",expire_day[0])
                temp = [domain+create_day+expire_day+'\n']
                a = temp[0]
                    #print type(a)
                    #print a
                    #print type(a)
                    #f.write(a.encode('utf-8'))
            except:
                unr = re.findall(ur'\u672a\u88ab\u6ce8\u518c\u6216\u88ab\u9690\u85cf',html)
                if len(unr):
                        print domain,unr[0]
                        temp = [domain+unr[0]+'\n']
                        a = temp[0]
                        f.write(a.encode('utf-8'))
                        #temp = ['未注册：'+" "+i+" "+'快去注册吧！！！']
                        #print>>f,temp[0]
                else:
                        print domain,"错误"
                        f.write("网络超时或服务器错误\n")
                        tool.append("http://whois.chinaz.com/"+domain)
                        #temp = ['未知错：'+" "+i+" "+'再试试？？']
                        #print>>f,temp[0]
                #parsePage(infoList,html)
        except:
            continue
    f.close()
    #printList(infoList) 
main()
