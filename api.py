#-*-coding:utf-8-*-
from urllib import request, parse
import pandas as pd
import json
import yaml


class weather(object):
    """docstring for weather"""

    def __init__(self, area, config):
        super(weather, self).__init__()
        self.area = area
        self.config = config
        self.get_weather()
        self.ana_weather()
        self.to_str()

    def get_weather(self):
        showapi_appid = self.config['showapi_appid']
        showapi_sign = self.config['showapi_sign']
        url = "http://route.showapi.com/9-2"
        send_data = parse.urlencode([
            ('showapi_appid', showapi_appid),
            ('showapi_sign', showapi_sign),
            ('area', self.area),
            ('needAlarm', "1")
        ])

        req = request.Request(url)
        try:
            response = request.urlopen(
                req, data=send_data.encode('utf-8'), timeout=10)
        except Exception as e:
            print(e)
        self.result = json.loads(response.read().decode('utf-8'))

    def ana_weather(self):
        main_data = self.result['showapi_res_body']

        time = main_data['time']
        time_y = time[0:4]
        time_m = time[4:6]
        time_d = time[6:8]
        time_human = '今日 {0}年{1}月{2}日'.format(
            time_y, time_m, time_d)
        self.date = time_human

        city_info = main_data['cityInfo']
        country = city_info['c9']
        province = city_info['c7']
        city = city_info['c5']
        dis = city_info['c3']
        city_human = '{0} {1} {2} {3}'.format(
            country, province, city, dis)
        self.city = city_human

        now = main_data['now']

        aqi = now['aqiDetail']
        aqii = aqi['aqi']
        pm2_5 = aqi['pm2_5']
        quality = aqi['quality']
        now_air = '实时空气质量 -- AQI:{0} {1} PM2.5:{2}'.format(
            aqii, quality, pm2_5)
        self.air = now_air

        now_temp = now['temperature']
        now_weather = now['weather']
        now_wind = now['wind_power']
        now_wind_dir = now['wind_direction']
        now_human = '实时天气 -- {0} {1}摄氏度 {2}{3}'.format(
            now_weather, now_temp, now_wind_dir, now_wind)
        now_weather_pic = now['weather_pic']
        self.rt_weather = now_human
        self.rt_weather_pic = now_weather_pic

        if len(main_data['alarmList']) > 0:
            self.alarm = main_data['alarmList'][0]['issueContent']
        else:
            self.alarm = '又是平静的一天'

        f1 = main_data['f1']
        day_temp = f1['day_air_temperature']
        night_temp = f1['night_air_temperature']
        self.allday = '{0}度 到 {1}度'.format(
            day_temp, night_temp)

    def to_str(self):
        ''' should looks like
        江苏南京 # city
        温度 # allday
        实时天气 #
        空气质量 # rt_weather
        预警信息 # alarm
        '''
        self.to_write = '''
### {0}

今日温度 {1}

![rtwpic]({5})

{2}

{3}

预警信息 -- {4}
    '''.format(self.city,
               self.allday,
               self.rt_weather,
               self.air,
               self.alarm,
               self.rt_weather_pic)

    def output(self):
        print(self.date)
        print(self.to_write)


class fund(object):
    """重仓股基金 www.juhe.cn"""

    def __init__(self, config):
        super(fund, self).__init__()
        self.config = config
        self.get_fund()
        self.to_str()

    def get_fund(self):
        key = self.config['juhe_appkey']
        url = "http://web.juhe.cn:8080/fund/zcgjj/"
        send_data = parse.urlencode([
            ('key', key)
        ])
        req = request.Request(url)
        try:
            response = request.urlopen(
                req, data=send_data.encode('utf-8'), timeout=10)
        except Exception as e:
            print(e)
        self.result = json.loads(response.read().decode('utf-8'))['result'][0]

    def to_str(self):
        data = pd.DataFrame(self.result).T
        data.fundnum = data.fundnum.astype(int)
        fundnum_sort = data.sort_values(by='fundnum')
        most_fund = fundnum_sort[-10:]
        name = most_fund.name
        fundnum = most_fund.fundnum
        code = most_fund.code

        self.to_write = '\n## 今日重仓股 \n'
        self.to_write += '\n|股票名称|股票代码|被持有基金数|当前价格|今日变幅|\n|---|---|---|---|---|\n'
        for i in range(len(name)):
            stock = stock_info(str(code[i]))
            str_i = '|' + str(name[i]) + '|' + str(code[i]) + \
                '|' + str(fundnum[i]) + '|' + str(stock.rt_price) +\
                '|' + str(stock.rt_rate) + '|' + '\n'
            self.to_write += str_i


class stock_info(object):
    """
    get sigle stock infomations from sina api
    hq.sinajs.cn"""

    def __init__(self, stock_id):
        super(stock_info, self).__init__()
        if stock_id[0] == '0':
            # 深圳所
            self.stock = 'sz' + stock_id
        elif stock_id[0] == '6':
            # 上海所
            self.stock = 'sh' + stock_id
        self.rt_stock()

    def rt_stock(self):
        sina_url = 'http://hq.sinajs.cn/list=' + self.stock
        data = str(request.urlopen(sina_url).read()).split(',')[1:]
        self.today_open = data[0]
        self.yes_close = data[1]
        self.rt_price = data[2]
        self.rt_rate = round(
            100 * (float(self.rt_price) - float(
                self.yes_close)) / float(self.yes_close), 2)
        self.today_max = data[3]
        self.today_min = data[4]

        self.k_img = 'http://image.sinajs.cn/newchart/daily/n/{}.gif'.format(
            self.stock)


class stock_pool(object):
    """更新关注股票的动态信息"""

    def __init__(self, config):
        super(stock_pool, self).__init__()
        self.pool = config['stocks']
        self.get_pool()

    def get_pool(self):
        return


if __name__ == '__main__':
    config = yaml.load(open('config.yaml', encoding="utf8"))
    print(fund(config).to_write)
