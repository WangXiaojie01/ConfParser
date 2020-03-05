#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.17
author: wangxiaojie
'''

import os, sys

codePath = os.path.abspath(os.path.join(__file__, "..", "Code"))
if os.path.exists(codePath):
    sys.path.append(codePath)
from ConfParser import *

if __name__ == "__main__":
    #配置文件的路径
    confFile = os.path.abspath(os.path.join(__file__, "../../etc/init.conf"))
    #初始化ConfParser
    iniConfParser = ConfParser(confFile)
    #获取配置，第一个参数为选项，第二个参数为要获取的参数名，第三个参数为获取不到参数后返回的默认值
    RecvTimeout = iniConfParser.getValueWithDefault("socket", "RecvTimeout", 10)
    print(RecvTimeout)

    #直接调用接口获取参数
    RecvTimeout = getValueWithDefault(confFile, "socket", "RecvTimeout1", 15)
    print(RecvTimeout)