#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.16
author: wangxiaojie
'''

import os,sys
import ConfigParser

__all__ = [
    "GetValueFromConf",
    "GetValueWithDefault",
    "ConfParser"
    ]

def GetValueFromConf(confFile, option, key):
    if not confFile:
        print("None of confFile")
        return False, "None of confFile", None 
    if not option:
        print("None of option")
        return False, "None of option", None 
    if not key:
        print("None of key")
        return False, "None of key", None 
    if not os.path.isfile(confFile):
        print("%s not found" % confFile)
        return False, "%s not found" % confFile, None
        
    config = ConfigParser.ConfigParser()
    config.read(confFile)
    try:
        result = config.get(option, key)
        return True, "success", result
    except Exception as e:
        print("None of %s.%s" % (option, key))
        return False, "None of %s.%s" % (option, key), None

def GetValueWithDefault(confFile, option, key, default):
    error, log, value = GetValueFromConf(confFile, option, key)
    if not value:
        value = default
    return value

class ConfParser(object):
    def __init__(self, confFile):
        self.config = ConfigParser.ConfigParser()
        self.config.read(confFile)

    def getValue(self, option, key):
        try:
            result = self.config.get(option, key)
            return result
        except Exception as e:
            return None
    
    def getValueWithDefault(self, option, key, default):
        result = self.getValue(option, key)
        if not result:
            return default
        else:
            return result

    def getIntWithDefault(self, option, key, default):
        result = self.getValue(option, key)
        if not result:
            return default
        else:
            return int(result)
    

if __name__ == "__main__":
    confFile = os.path.abspath(os.path.join(__file__, "../../etc/init.conf"))
    initConfParser = ConfParser(confFile)
    RecvTimeout = initConfParser.getValueWithDefault("socket", "RecvTimeout", 10)
    print(RecvTimeout)
    RecvTimeout = GetValueWithDefault(confFile, "socket", "RecvTimeout1", 15)
    print(RecvTimeout)
