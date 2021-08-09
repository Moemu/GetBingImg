# Bing每日一图获取程序

## 介绍

一款基于Python的获取当天或指定一天的Bing美图，支持查询同一月内Bing美图信息的小程序

## 使用

请确保您的电脑上已配置好Python运行环境

请确保您的电脑上已安装`requests`库（若无则在cmd运行下列代码）：

```powershell
pip install requests
```

配置完成后双击`GetBingImg.py`即可使用（不推荐使用控制台运行此Py程序）

在菜单选择1，即可获取当天美图

在菜单选择2，根据提示依次输入要获取的美图的时间（yyyy-mm-dd）（例：2021-01-01 则依次输入2021，01，01）
（若不填，则默认为当天）即可获取指定时间的美图

在菜单选择3，根据提示依次输入要查询的美图的时间（dd）（仅当月，例如现在是8月，就只能查询8月中的美图时间）（若不填，则默认为当天）即可获取指定时间的美图信息

美图一般保存在程序根目录中（直接运行.py文件时），名字格式为Bing(yyyy-mm-dd).jpg

## 调用

本程序主要调用以下链接：
https://www.bing.com/HPImageArchive.aspx

https://upyuns.mcloc.cn/bing

https://bing.mcloc.cn/api

## 后话

本程序遵守Apache License 2.0，未经允许不可转载

WhitemuTeam