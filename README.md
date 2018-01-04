# Toys

一些简单、有趣的 Python 小程序，结果以静态网页展现。

## 免费 API

国内的一些数据公司在实名认证前提下会提供相当一部分的免费 api 接口。

**聚合数据 juhe.com**

万年历 https://www.juhe.cn/docs/api/id/177

黄金数据 https://www.juhe.cn/docs/api/id/29

净值数据 https://www.juhe.cn/docs/api/id/25

IP地址 https://www.juhe.cn/docs/api/id/1

股票数据 https://www.juhe.cn/docs/api/id/21

汇率数据 https://www.juhe.cn/docs/api/id/23

重仓股基金 https://www.juhe.cn/docs/api/id/27

笑话大全 https://www.juhe.cn/docs/api/id/95

新闻 https://www.juhe.cn/docs/api/id/138

指数信息 https://www.juhe.cn/docs/api/id/167

**易源数据 showapi.com**

天气预报 https://www.showapi.com/api/lookPoint/9

## Toy 1

本地天气，在这里我用到了易源数据的天气 api，由于是静态网页无法交互，所以我使用的是固定地址的天气信息查询，请求方式是 get，返回数据为 json。源码为[weather-api.py](weather-api.py) 。

结果以字符串格式返回，需要使用 json.loads() 函数整理为字典，就可以使用键值调用了。为了便于使用，将查询天气过程封装为对象。思路如下：

~~~python
class weather
	init area
  	def get weather
    def sort json dict
    def output
    def to_file
~~~

整体后选择性输出的结果示例如下：

~~~
中国 江苏 南京 南京
今日 2018年01月04日
1度 到 -1度
实时空气质量 -- AQI:21 优质 PM2.5:11
实时天气 -- 雪 0摄氏度 东北风2级
南京市气象台2018年01月04日07时27分发布暴雪橙色预警信号。预计未来12小时内我市大部分地区仍有暴雪，中北部部分地区积雪深度将达15厘米以上，请注意防范。
~~~

一般 api 调用都会用到类似于个人 key 的参数



