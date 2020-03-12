#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.16
author: wangxiaojie
'''

import os,sys
import configparser
import logging

__all__ = [
    "getValueFromConf",
    "getValueWithDefault",
    "ConfParser",
    "confLogger"
    ]

confLogger = logging.Logger("ConfParser")

def getValueFromConf(confFileName, option, key):
    if not confFileName:
        confLogger.error("confFileName is None")
        return False, "confFileName is None", None 
    if not option:
        confLogger.error("option is None")
        return False, "option is None", None 
    if not key:
        confLogger.error("key is None")
        return False, "key is None", None 
    if not os.path.isfile(confFileName):
        confLogger.error("%s is not a file" % confFileName)
        return False, "%s is not a file" % confFileName, None
    try:   
        config = configparser.ConfigParser()
        config.read(confFileName)
        result = config.get(option, key)
        return True, "success", result
    except Exception as e:
        confLogger.error("get value from %s error, error is %s" % (confFileName, e))
        return False, "get value from %s error, error is %s" % (confFileName, e), None

def getValueWithDefault(confFileName, option, key, default):
    result, log, value = getValueFromConf(confFileName, option, key)
    if not result:
        return default
    return value

class ConfParser(object):
    def __init__(self, confFile):
        if not os.path.isfile(confFile):
            confLogger.error("%s is not a file" % confFile)
            return
        try:
            self.config = configparser.ConfigParser()
            self.config.read(confFile)
        except Exception as e:
            confLogger.error("init ConfParser error, error is %s" % e)

    def getValue(self, option, key):
        try:
            result = self.config.get(option, key)
            return result
        except Exception as e:
            confLogger.error("getValue error, error is %s" % e)
            return None
    
    def getValueWithDefault(self, option, key, default):
        result = self.getValue(option, key)
        if not result:
            return default
        else:
            return result

    def getIntWithDefault(self, option, key, default):
        tempStr = self.getValueWithDefault(option, key, default)
        try:
            result = int(float(tempStr))
            return result
        except Exception as e:
            confLogger.error("int(float(%s)) error, error msg is %s" % (tempStr, e))
            return None

if __name__ == "__main__":
    confFile = os.path.abspath(os.path.join(__file__, "../../etc/init.conf"))
    initConfParser = ConfParser(confFile)
    RecvTimeout = initConfParser.getValueWithDefault("socket", "RecvTimeout", 10)
    print(RecvTimeout)
    RecvTimeout = getValueWithDefault(confFile, "socket", "RecvTimeout1", 15)
    print(RecvTimeout)
