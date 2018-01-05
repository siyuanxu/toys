# -*-coding:utf-8-*-
from weather_api import weather
import yaml
import codecs

with codecs.open('index.md', 'w', 'utf-8') as index:
    config = yaml.load(open('config.yaml'))

    weather_main = weather('南京', config)
    weather_1 = weather_main.to_write
    weather_2 = weather('漯河', config).to_write
    weather_3 = weather('泸州', config).to_write

    index.write('## {0} 天气')
    index.write(weather_1)
    index.write(weather_2)
    index.write(weather_3)  # use coding utf8
