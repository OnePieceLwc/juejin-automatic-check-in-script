# 掘金自动签到并抽奖脚本
掘金自动签到并抽奖脚本

## 1.获取掘金自动签到并抽奖脚本.py代码

## 2.安装库
```
pip install requests
```

## 3.获取参数

### 3.1 获取参数cookie，aid，uuid，spider
```
打开掘金签到页面: 访问 https://juejin.cn/user/center/signin?from=main_page。
打开开发者工具: 按下 F12 键打开浏览器的开发者工具（不同浏览器可能略有差异）。
进入网络面板: 在开发者工具中，选择“网络”或“Network”标签页。
搜索特定请求: 按下 Ctrl+F (或 Cmd+F 在 macOS 上)，在搜索框中输入 get_cur_point 并回车，查找包含该字符串的网络请求。
刷新页面并观察: 刷新页面，观察 get_cur_point 请求是否再次出现，以及其他相关的网络请求。
检查请求细节: 点击任意一个感兴趣的网络请求，查看其请求方法、请求头、请求参数和响应数据等详细信息。
```

![image](https://github.com/user-attachments/assets/fc3db9e9-9126-41b8-8a6d-7379a6d748b8)

```
在请求 URL 找到aid，uuid，spider，msToken，a_bogus
```

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
