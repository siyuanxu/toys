#-*-coding:utf-8-*-
from urllib import request, parse
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

        self.alarm = main_data['alarmList'][0]['issueContent']

        f1 = main_data['f1']
        day_temp = f1['day_air_temperature']
        night_temp = f1['night_air_temperature']
        self.allday = '{0}度 到 {1}度'.format(
            day_temp, night_temp)

    def output(self):
        print(self.city)
        print(self.date)
        print(self.allday)
        print(self.air)
        print(self.rt_weather)
        print(self.alarm)

    # def to_md(self):
    #     to_write = '''

    #     '''
    #     with open('weather.md', 'w') as f:
    #         f.write(str())


if __name__ == '__main__':
    config = yaml.load(open('config.yaml'))
    weather('南京', config).output()
