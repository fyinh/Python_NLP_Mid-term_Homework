# coding:utf-8

import jieba
from wordcloud import WordCloud

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from figure_painting import *

def get_words_frequency():
    # 打开文件并读取文本内容
    content = open('sgyy.txt','r').read()
    # 使用结巴分词对文本进行分词
    words = jieba.lcut(content)

    # 定义一个字典去存储分词结果和出现的次数
    counts = {}
    for word in words:
        # 我们忽略长度为1的词
        if len(word) == 1:
            continue
        if word == u'\r\n':
            continue
        counts[word] = counts.get(word, 0) + 1


    items = list(counts.items())

    # 根据items的第二个值进行从大到小的排序
    items.sort(key=lambda x:x[1], reverse=True)

    words_list_sort = []
    words_list_count = []

    for i in range(20):
        word, count = items[i]
        words_list_sort.append(word)
        words_list_count.append(count)
        # 格式化输出
        print ("{:<8}{:>5}".format(word, count))
        # print (word, count)

    return words_list_sort, words_list_count, words


def word_cloud(words):

    # 对切分结果重新拼接用于词云制作
    newtxt = " ".join(words)
    # 词云制作
    wordcloud = WordCloud(background_color='black',
                          width=800,
                          height=600,
                          font_path="/home/fuyinwen/Downloads/simhei.ttf",
                          max_words=100,
                          max_font_size=80
                          ).generate(newtxt)
    # 保存词云图
    wordcloud.to_file("word_cloud1.png")

def main():
    words_list_sort, words_list_count, words = get_words_frequency()
    # word_cloud(words)
    show_words_barh(words_list_sort, words_list_count)


if __name__ == '__main__':
    main()
