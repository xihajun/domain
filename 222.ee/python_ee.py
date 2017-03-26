# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import re
  
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
    start_url = 'http://222.ee/?domain='
    kv = {'user-agent':'Mozilla/5.0'}
    for i in range(255,9999):
        try:
            url = start_url + str(i) + '.ee'
            html = getHTMLText(url)
            try:
                day = re.findall(r'expire:.*\d{4}\-\d{2}\-\d{2}',html)
                dom = re.findall(r'name.*\d{3}.ee',html)
                deadline = day[0].split(' ')[5]
                domain = dom[0].split(' ')[7]
                print '被注册：',domain,deadline
            except:
                unr = re.findall(r'Domain not found',html)
                if unr == 'Domain not found':
                    print '未注册：',i,'快去注册吧！！！'
                else:
                    print '未知错：',i,'再试试？？'
            #parsePage(infoList,html)
        except:
            continue
    #printList(infoList) 
main()
