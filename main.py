# -*-coding:utf-8-*-
from api import *
import yaml
import codecs
import smtplib
from email.mime.text import MIMEText


# load keys and config
config = yaml.load(open('config.yaml', encoding="utf8"))

# finace toys
# write into a finace tmp md file
# if the time is during the market time
# then copy the tmp file into index.md
# if not, keep the old tmp and do nothing


market_time = [928, 1202, 1328, 1502]
time_now = int(time.strftime('%H%M', time.localtime(time.time())))

if time_now in range(market_time[0],
                     market_time[1]) or time_now in range(market_time[2],
                                                          market_time[3]):
    with codecs.open('finace_tmp.txt', 'w', 'utf-8') as ft:
        # fund toy
        fund_res = fund(config).to_write
        ft.write(fund_res)

        # vip stock toy
        vip_stock = stock_pool(config)
        ft.write(vip_stock.to_write)

else:
    pass
with codecs.open('finace_tmp.txt', 'r', 'utf-8') as ft:
    ft_content = ''.join(ft.readlines())


with codecs.open('index.md', 'w', 'utf-8') as index:
  
    xmr_info = xmr()
    index.write(xmr_info.str)

    index.write(ft_content)

    # weather toy
    weather_main = weather('南京', config)
    weather_1 = weather_main.to_write
    weather_2 = weather('漯河', config).to_write
    weather_3 = weather('泸州', config).to_write

    index.write('## {0} 天气'.format(weather_main.date))
    index.write(weather_1)
    index.write(weather_2)
    index.write(weather_3)  # use coding utf8

    # time log
    index.write('\n')
    index.write(time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())))
