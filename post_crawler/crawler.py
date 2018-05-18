import requests
import time
import xml.etree.ElementTree as ET
from multiprocessing.dummy import Pool as ThreadPoo
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def __init__(self, provinces):
        self.provinces = provinces

    def start_element(self, name, attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.provinces.append((name, number))

    def end_element(self, name):
        pass

    def char_data(self, text):
        pass


def get_provinces(url):
    # 抓取页面
    content = requests.get(url).content.decode('gb2312')
    # find查找感兴趣的内容
    start = content.find('<map name=\"map_86\" id=\"map_86\">')
    end = content.find('</map>')
    # 使用切片获取需要的内容
    content = content[start:end + len('</map>')].strip()
    print(content)
    # provinces来装取切片的结果
    provinces = []
    # 处理xml代码
    handler = DefaultSaxHandler(provinces)  # 处理器
    parser = ParserCreate()  # 解析器
    parser.StartElementHandler = handler.start_element  # 起始标记
    parser.EndElementHandler = handler.end_element  # 结束标记
    parser.CharacterDataHandler = handler.char_data  # xml文本
    parser.Parse(content)  # 分析获取的文本
    return provinces


provinces = get_provinces('http://www.ip138.com/post')
print(provinces)


