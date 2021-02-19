# -*- coding: utf-8 -*-
'''
    Author: 叶哥哥
    Copyright: 叶哥哥
'''

import requests
import json
import time
from colorama import init,Fore,Back,Style
from os import system

#init(autoreset=True,convert=True,wrap=True)
init(autoreset=True)

def fromxsot():
    url='https://api.xsot.cn/sentence/' #请求（不带参数）

    print(""
    "|  类型  |  输入 | \n"
    "|--------|-------| \n"
    "|  动画  |   a   | \n"
    "|  漫画  |   b   | \n"
    "|  游戏  |   c   | \n"
    "|  文学  |   d   | \n"
    "|  原创  |   e   | \n"
    "|来自网络|   f   | \n"
    "|  其他  |   g   | \n"
    "|  影视  |   h   | \n"
    "|  诗词  |   i   | \n"
    "| 网易云 |   j   | \n"
    "|  哲学  |   k   | \n"
    "|  随机  |  其他 | \n"
    "|--------|-------| \n"
    "") #输出所有类型

    stype=input('选择类型：') #让用户输入类型
    sencode='json' 

    req=url+'?cat='+stype+'&encode='+sencode #发送请求链接（带参数）
    print("请求地址："+req+"\n\n\n") 

    try:
        get=requests.get(url=req,timeout=30) #requests库发送get请求
    except TimeoutError:
        print('网络连接超时，请检查网络连接或者更换源！\n\n')
    except:
        print('请求失败 - 未知错误')
    #print(get.text+"\n\n\n") #打印返回的值

    result=json.loads(get.text) #把返回的json格式转换python字典

    '''时间戳的转换'''
    add_time_unchange=time.localtime(int(result['created_at']))
    add_time=time.strftime('%Y-%m-%d %H:%M:%S',add_time_unchange)

    '''打印结果'''
    print('一言唯一标识：'+result['uuid'])
    print('\n'+result['sentence']+'\n')
    print('句子类型：'+result['type'])
    print('出处：'+result['from'])
    print('作者：'+result['from_who'])
    print('添加时间：'+add_time)
# fromxsot()

def frommain():
    """
    从一言的主站获取。
    官方接口。
    """
    url='https://v1.hitokoto.cn/'
    print(""
    "|  类型  |  输入 | \n"
    "|--------|-------| \n"
    "|  动画  |   a   | \n"
    "|  漫画  |   b   | \n"
    "|  游戏  |   c   | \n"
    "|  文学  |   d   | \n"
    "|  原创  |   e   | \n"
    "|来自网络|   f   | \n"
    "|  其他  |   g   | \n"
    "|  影视  |   h   | \n"
    "|  诗词  |   i   | \n"
    "| 网易云 |   j   | \n"
    "|  哲学  |   k   | \n"
    #"| 抖机灵 |   l   | \n" get请求过去总是返回错误提示没有句子，估计这个挂了
    "|  随机  |  留空 | \n"
    "|--------|-------| \n"
    "") #输出所有类型

    stype=input("输入类型：")
    sencode='json'
    scharset='utf-8'
    # 2021-02-17发现错误，输入空格会报错，添加判断再发送request
    typelist=['a','b','c','d','e','f','g','h','i','j','k','l']
    print(Fore.GREEN+'')
    if stype not in typelist:
        system('')
        print(Fore.BLUE+'输入有误，将默认为随机')
        stype=''

    # 接口文档使用实例中，随机一种是不带c=类型的，所以输入要判断一下
    if stype=='':
        req=url+'?encode='+sencode+'&charset'+scharset
    else:
        req=url+'?c='+stype+'&encode='+sencode+'&charset='+scharset
    
    print('请求地址：'+req)

    try:
        get=requests.get(url=req,timeout=20)
    except TimeoutError:
        print("请求失败，请检查网络连接！")
    except:
        print('请求失败 - 未知错误！')
    #print(get.text)
    #print(get.status_code)
    #if get.status_code!='200':
    #    print('\n\n获取失败，请重试！\n\n')
    #    exit()
    #else:
    #    pass

    result=json.loads(get.text)
    #if result['status']==400:
    #    print('获取失败，请重试！')
    #    exit()     #配合挂了的那个食用

    '''时间戳的转换'''
    add_time_unchange=time.localtime(int(result['created_at']))
    add_time=time.strftime('%Y-%m-%d %H:%M:%S',add_time_unchange)

    print('一言标识：'+str(result['id']))# 不知道为什么报错can only concatenate str (not "int") to str所以就在前面加类型转换
    print("一言唯一标识："+result['uuid'])     
    print('\n正文：'+result['hitokoto']+'\n')
    print('句子类型：'+result['type'])
    print('出处：'+result['from'])
    if result['from_who']==None:
        from_who='未知作者'
    else:
        from_who=result['from_who']
    print('作者：'+from_who)
    print('添加者：'+result['creator'])
    print('添加者id：'+str(result['creator_uid']))
    print('审核员id：'+str(result['reviewer']))
    print('提交方式：'+result['commit_from'])
    print('添加时间：'+add_time)
    print('句子长度：'+str(result['length']))
#frommain()

while True:
    which=input('\n\n选择xsot.cn还是hitokoto.cn的源？输入1或2，或者exit退出：')
    if which=='1':
        fromxsot()
    elif which=='2':
        frommain()
    elif which=='exit':
        break
        exit()
    else:
        print('输入错误，请重试！')
