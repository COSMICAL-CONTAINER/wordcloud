import os
from os import path
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 获取单前文件路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# 获取文本text
with open(path.join(d,'text.txt')) as f:
    # cut_txt =" ".join(f.read())#空格划分
    cut_txt =f.read()
    print(cut_txt)
    photo =plt.imread('picture.jpg')#形成词云图的图片形状
    wordcloud =WordCloud(
            font_path="simhei.ttf",#设置输出词云的字体
            max_font_size=60,#设置字体的大小，默认200
            background_color='white',
            prefer_horizontal=1,
            #width=2300,height=1900,
            scale=6,#设置图的词密度
            random_state=50,## random.Random用来生成随机颜色
            mask=photo#设置图片形状,
            ).generate(cut_txt)#generate()根据文本生成词云
    plt.imshow(wordcloud,interpolation="nearest")
    plt.axis("off")#关闭x,y轴刻度
    plt.savefig('save.jpg')
    plt.show()
