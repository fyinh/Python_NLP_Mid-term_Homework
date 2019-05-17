# coding: utf-8

import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from figure_painting import *

def get_char_frequency():
    # 打开文件并读取文本内容
    content = codecs.open('sgyy.txt', 'r', encoding="utf-8").read()

    words = []

    # 忽略标点符号
    excludes = {u'，', u'。', u'！', u'？', u'、', u'（', u'）', u'【', u'】',
                u'<', u'>', u'《', u'》', u'=', u'：', u'+', u'-', u'*',
                u'—', u'“', u'”', u'…', u'"', u'；'}

    # 添加每一个字到列表中
    for line in content:
        for char in line:
            words.append(char)

    # 定义一个字典去存储分词结果和出现的次数
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    # 把一些不是人名的词语排除掉
    for word in excludes:
        try:
            del counts[word]
        except:
            pass

    items = list(counts.items())

    # 根据items的第二个值进行从大到小的排序
    items.sort(key=lambda x: x[1], reverse=True)

    char_list_sort = []
    char_list_count = []

    for i in range(20):
        word, count = items[i]
        char_list_sort.append(word)
        char_list_count.append(count)
        # 格式化输出
        print ("{:<8}{:>5}".format(word, count))
        # print (word, count)

    return char_list_sort, char_list_count

char_list_sort, char_list_count = get_char_frequency()
show_words_barh(char_list_sort, char_list_count)
