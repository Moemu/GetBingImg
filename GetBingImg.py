import requests as r
import datetime
import os
import sys
from dateutil import parser
from xml.dom import minidom

#当前时间获取
time = datetime.datetime.now()
realtime = time.strftime("%Y-%m-%d")

print('欢迎使用Bing每日美图获取器')
print('今天是:',realtime)
print('作者：WhitemuTeam')
print('----------菜单栏----------')
print('1.获取今日美图')
print('2.获取指定美图')
print('3.获取美图信息')
print('----------菜单栏----------')
print('做出你的选择吧~')
choose=int(input('输入序号：'))

if choose==1:
    print('获取中...')
    img = r.get('https://bing.mcloc.cn/api')
    name = 'Bing('+realtime+').jpg'
    open(name, 'wb').write(img.content)
    input('获取成功，按任意键退出')
if choose==2:
    year = time.strftime('%Y')
    word = '输入年，默认为'+year+'(4位): '
    getyear = input(word)
    if  getyear=='':
        getyear=year
    mouth = time.strftime('%m')
    word = '输入月，默认为'+mouth+'(2位): '
    getmouth = input(word)
    if getmouth=='':
        getmouth=int(mouth)
    else:
        getmouth=int(getmouth)
    day = time.strftime('%d')
    word = '输入日，默认为'+day+'(2位): '
    getday = input(word)
    if getday=='':
        getday=day
    print('您所要下载的是',getyear,'-',getmouth,'-',getday,'的Bing美图')
    print('获取中...')
    if getmouth==1:
        getmouth='Jan'
    elif getmouth==2:
        getmouth='Fbr'
    elif getmouth==3:
        getmouth='Mar'
    elif getmouth==4:
        getmouth='Apr'
    elif getmouth==5:
        getmouth='May'
    elif getmouth==6:
        getmouth='Jun'
    elif getmouth==7:
        getmouth='Jul'
    elif getmouth==8:
        getmouth='Aug'
    elif getmouth==9:
        getmouth='Sep'
    elif getmouth==10:
        getmouth='Oct'
    elif getmouth==11:
        getmouth='Nov'
    elif getmouth==12:
        getmouth='Dec'
    url = 'https://upyuns.mcloc.cn/bing/'+getday+'-'+getmouth+'-'+getyear+'/'+getday+'-'+getmouth+'-'+getyear+'.jpg'
    img = r.get(url)
    name = 'Bing('+getday+'-'+getmouth+'-'+getyear+').jpg'
    open(name,'wb').write(img.content)
    input('获取成功，按任意键退出')

if choose==3:
    print('仅支持同一月内')
    # 不同天的时间差
    d2 = realtime 
    d1_1 = input('输入要查询的时间(dd,若不填则默认是当天)：')
    if d1_1:
        day = time.strftime('%d')
    d1_2= realtime = time.strftime("%Y")
    d1 = d1_2+'-'+d1_1
    Days = str((parser.parse(d2) - parser.parse(d1)).days)
    url = 'https://www.bing.com/HPImageArchive.aspx?format=xml&cc=jp&idx='+Days+'&n=1'
    xls=r.get(url)
    name = 'temp.xml'
    open(name, 'wb').write(xls.content)
    dom=minidom.parse("temp.xml")
    root=dom.documentElement
    msg = root.getElementsByTagName('copyright')
    information1 = msg[0].firstChild.data
    msg = root.getElementsByTagName('copyrightlink')
    information2 = msg[0].firstChild.data
    print('拍摄地(作者)：',information1)
    print('相关链接：',information2)
    os.remove('temp.xml')
    input('按任意键退出')