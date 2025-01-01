# 掘金自动签到并抽奖脚本
掘金自动签到并抽奖脚本

## 1.获取掘金自动签到并抽奖脚本.py代码

## 2.安装库
```
pip install requests
```

## 3.获取参数

### 3.1 获取参数cookie，aid，uuid，spider
打开签到界面(https://juejin.cn/user/center/signin?from=main_page)，摁F12，点击网络，摁ctrl+f键，在左侧的搜索框输入：get_cur_point回车，刷新界面 ，点击任意接口
![image](https://github.com/user-attachments/assets/fc3db9e9-9126-41b8-8a6d-7379a6d748b8)


在请求 URL 找到aid，uuid，spider，msToken，a_bogus
![image](https://github.com/user-attachments/assets/7836d9dd-0587-4167-b9c2-17198a0b61f1)
```
aid = ""
uuid = ""
spider = ""
a_bogus = ''
```
```
msToken  获取后需要url解码，才可以使用
  解密网址1:https://www.toolhelper.cn/EncodeDecode/Url
  解密网址2:https://www.bejson.com/enc/urlencode/index.html#google%20vignette
```
![image](https://github.com/user-attachments/assets/8dc61afb-e381-4635-9b08-d45d793e007e)
```
msToken = ''
```
获取cookie和User-Agent
![image](https://github.com/user-attachments/assets/9defea05-992b-4b84-91e6-378d301bf4d1)
```
cookie =""
'User-Agent': ''
```
