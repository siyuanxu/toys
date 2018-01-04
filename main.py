#-*-coding:utf-8-*-
from weather_api import weather
import yaml

with open('index.md', 'w') as index:
    config = yaml.load(open('config.yaml'))

    weather_main=weather('南京', config)
    weather_1 = weather_main.to_write
    weather_2 = weather('漯河', config).to_write
    weather_3 = weather('泸州', config).to_write

    index.write('## {0} 天气'.format(weather_main.date))
    index.write(weather_1)
    index.write(weather_2)
    index.write(weather_3)