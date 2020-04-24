#字体按图片颜色.py
import os
from os import path
import jieba as jb
import wordcloud as wc
from PIL import Image
import numpy as np             #1  imread常报错，用numpy和pil替换掉了。
mask=np.array(Image.open('picture.jpg'))
# 获取单前文件路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# 获取文本text
f=open(path.join(d,'text.txt'))
t = f.read()
image_colors = wc.ImageColorGenerator(mask)    #2 按图片颜色显示字体显色
#写出不要出现的词组
exclude={'我们','你们','他们','它们','因为','因而','所以','如果','那么',\
          '如此','只是','但是','就是','这是','那是','而是','而且','虽然',\
          '这些','有些','然后','已经','于是','一种','一个','一样','时候',\
    '没有','什么','这样','这种','这里','不会','一些','这个','仍然','不是',\
    '自己','知道','可以','看到','那儿','问题','一会儿','一点','现在','两个',\
         '三个','说道','可是','地方','怎么','这儿','突然','可能','甚至','还是',\
         '那些','还有','只有',\
          }
f.close()
ls = jb.lcut(t)
txt = ' '.join(ls)
w = wc.WordCloud(
    font_path = 'msyh.ttf',
    max_words=2000,
    min_font_size=1,
    max_font_size=60,
    mask=mask,width = 1000,
    height = 1000,
    background_color = 'white',stopwords=exclude,
    color_func=image_colors)#3 图片颜色加到参数里
w.generate(txt)
w.to_file('save.png')
