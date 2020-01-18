# ConfParser
对ConfigParser做了封装的一个从配置文件获取配置的工具

###使用范例
```
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
    RecvTimeout = GetValueWithDefault(confFile, "socket", "RecvTimeout1", 15)
    print(RecvTimeout)
```

###接口说明
GetValueFromConf(confFile, option, key)
&nbsp;&nbsp;&nbsp; confFile配置文件
&nbsp;&nbsp;&nbsp; option参数选项
&nbsp;&nbsp;&nbsp; key参数键
如果获取不到，会返回None

GetValueWithDefault(confFile, option, key, default)
&nbsp;&nbsp;&nbsp; confFile配置文件
&nbsp;&nbsp;&nbsp; option参数选项
&nbsp;&nbsp;&nbsp; key参数键
&nbsp;&nbsp;&nbsp; default获取数据失败后返回的默认值

###类说明
* ConfParser只是将以上的接口封装了
* 先定义一个ConfParser对象
  ```
  initConfParser = ConfParser(confFile)
  ```
* 接口说明
  initConfParser.getValue(option, key)
  &nbsp;&nbsp;&nbsp; option参数选项
  &nbsp;&nbsp;&nbsp; key参数键
  如果获取不到，会返回None

  initConfParser.getValueWithDefault(option, key, default)
  &nbsp;&nbsp;&nbsp; option参数选项
  &nbsp;&nbsp;&nbsp; key参数键
  &nbsp;&nbsp;&nbsp; default获取数据失败后返回的默认值
  
  initConfParser.getIntWithDefault(option, key, default)
  &nbsp;&nbsp;&nbsp; option参数选项
  &nbsp;&nbsp;&nbsp; key参数键
  &nbsp;&nbsp;&nbsp; default获取数据失败后返回的默认值，必需传入int，否则默认返回的就不是int值了