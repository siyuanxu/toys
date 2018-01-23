# -*-coding:utf-8-*-
from api import *
import yaml
import codecs
import smtplib
from email.mime.text import MIMEText

with codecs.open('index.md', 'w', 'utf-8') as index:
    # load keys and config
    config = yaml.load(open('config.yaml', encoding="utf8"))
    # weather toy
    weather_main = weather('南京', config)
    weather_1 = weather_main.to_write
    weather_2 = weather('漯河', config).to_write
    weather_3 = weather('泸州', config).to_write

    index.write('## {0} 天气'.format(weather_main.date))
    index.write(weather_1)
    index.write(weather_2)
    index.write(weather_3)  # use coding utf8
    # index.write(str(time.time())) # for crontab test

    # fund toy
    fund_res = fund(config).to_write
    index.write(fund_res)

