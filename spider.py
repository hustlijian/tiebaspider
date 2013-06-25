#!/usr/bin/env python  
#-*- coding: utf8 -*-  
from urllib import urlopen
import re

myFile = open('file.txt', 'w')

def getonepage(url):
    ''' 从连载贴中取得一章的内容'''
    #print url
    webdata = urlopen(url).read()
    #print webdata
    matches = re.findall('<title>(.+?)</title>', webdata)
    for m in matches:
        print m #章节名字
        myFile.write(m)

    #matches = re.findall('<cc>(.+?)</cc>', webdata)
    matches = re.findall('j_d_post_content">(.+?)</div>', webdata)
    for m in matches:
        #print m #
        str = re.sub(r'<br>','\n',m) #处理换行
        str = re.sub(r'</?\w+[^>]*>','',str) #删除网页标签
        #print str,
        myFile.write(str)
    #print '======================================' #一章结束
    myFile.write('\n===========================================\n')
        
def geturls(url):
    ''' 从《绝世唐门》全部章节连载贴【禁水】中提取每章的url'''
    webdata = urlopen(url).read()
    #print webdata
    #matches = re.findall('<cc>(.+?)</cc>', webdata)
    matches = re.findall('target="_blank">(http:.+?)</a>', webdata)
    for m in matches:
        #print m+"?see_lz=1"
        getonepage(m+"?see_lz=1") #只看楼主
        #break

def main():
    geturls("http://tieba.baidu.com/p/1980204171")
    geturls("http://tieba.baidu.com/p/1980204171?pn=2")

if __name__ == '__main__':
    main()
    myFile.close()