# coding:utf-8

import jieba

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from figure_painting import *

def get_character_frequency():
    # 打开文件并读取文本内容
    content = open('sgyy.txt','r').read()
    # 使用结巴分词对文本进行分词
    words = jieba.lcut(content)

    # 非人名集合,用于下面统计词频时排除不是人名的单词
    excludes = {u'将军', u'却说', u'二人', u'不可', u'荆州', u'不能', u'如此', u'商议', u'如何',
                u'军士', u'左右', u'天下', u'次日', u'大喜', u'引兵', u'军马', u'东吴', u'于是',
                u'今日', u'不敢', u'魏兵', u'陛下', u'一人', u'人马', u'汉中', u'不知', u'只见',
                u'众将', u'蜀兵', u'上马', u'大叫', u'\r\n', u'此人'}

    # 定义一个字典去存储分词结果和出现的次数
    counts = {}
    for word in words:
        # 长度为1的单词大概率不是人名,因此我们忽略长度为1的词
        if len(word) == 1:
            continue
        elif word == u'孔明曰' or word == u'诸葛亮':
            rword = u'孔明'
        elif word == u'玄德' or word == u'玄德曰' or word == u'主公':
            rword = u'刘备'
        elif word == u'孟德' or word == u'丞相':
            rword = u'曹操'
        elif word == u'关公' or word == u'云长':
            rword = u'关羽'
        elif word == u'都督':
            rword = u'周瑜'
        elif word == u'后主':
            rword = u'刘禅'
        elif word == u'太守':
            rword = u'刘度'
        else:
            rword = word
        counts[rword] = counts.get(rword, 0) + 1

    # 把一些不是人名的词语排除掉
    for word in excludes:
        try:
            del counts[word]
        except:
            pass

    items = list(counts.items())

    # 根据items的第二个值进行从大到小的排序
    items.sort(key=lambda x:x[1], reverse=True)

    name_list_sort = []
    name_list_count = []

    for i in range(15):
        word, count = items[i]
        name_list_sort.append(word)
        name_list_count.append(count)
        # 格式化输出
        print ("{:<8}{:>5}".format(word, count))
        # print (word, count)

    return name_list_sort, name_list_count

def main():
    name_list_sort, name_list_count = get_character_frequency()
    show_name_bar(name_list_sort, name_list_count)
    show_name_pie(name_list_sort, name_list_count)

if __name__ == '__main__':
    main()


