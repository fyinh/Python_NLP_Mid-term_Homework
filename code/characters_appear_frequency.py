# coding: utf-8

import codecs
import jieba.posseg as pseg
import jieba

import sys
reload(sys)
sys.setdefaultencoding('utf8')

names = {} # 保存人物, key为人物名称,value为该人物在全文中出现的次数
relationships = {} # 保存人物关系的有向边，键为有向边的起点，值为一个字典 edge ，edge 的键为有向边的终点，值是有向边的权值
line_names = [] # 缓存变量,保存对每一段分词得到当前段中出现的人物名称

jieba.load_userdict("names.txt") # 加载人物表
with codecs.open("sgyy.txt","r", "utf8") as f:
    for line in f.readlines():
        pos = pseg.cut(line) # 分词,返回词性
        line_names.append([]) # 为本段增加一个人物列表
        for w in pos:
            if w.flag != 'nr' or len(w.word) < 2:
                continue # 当分词长度小于2或该词词性不为nr(人名)时认为该词不为人名
            line_names[-1].append(w.word) # 为当前段的环境增加一个人物
            if names.get(w.word) is None: # 如果某人物(w.word)不在人物字典中
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1

# 输出人物出现次数统计结果
for name, counts in names.items():
    print (name, counts)

# 对于 lineNames 中每一行，我们为该行中出现的所有人物两两相连。如果两个人物之间尚未有边建立，则将新建的边权值设为 1，
# 否则将已存在的边的权值加 1。这种方法将产生很多的冗余边，这些冗余边将在最后处理。
for line in line_names:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2] + 1

# 由于分词的不准确会出现很多不是人名的“人名”，从而导致出现很多冗余边，
# 为此可设置阈值为100，即当边出现100次以上则认为不是冗余

with codecs.open("People_node.txt", "w", "utf8") as f:
    f.write("ID Label Weight\r\n")
    for name, times in names.items():
        if times > 100:
            f.write(name + " " + name + " " + str(times) + "\r\n")



with codecs.open("People_edge.txt", "w", "utf8") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 100:
                f.write(name + " " + v + " " + str(w) + "\r\n")

# 利用names.txt来筛选People_edge.txt中非人名的词
f = codecs.open('People_edge.txt', 'r', encoding='utf8')
f2 = codecs.open('names.txt', 'r', encoding='utf8').read()
lines = f.readlines()

A = []
for line in lines:
    A.append([])
    m = line.strip('\n').split(' ')
    for x in m:
        A[-1].append(x)
B = []
for items in A:
    if items[0] not in f2 or items[1] not in f2:
        continue
    else:
        B.append(items)

f.close()
w = codecs.open('result.txt', 'w', encoding='utf8')
for i in B:
    w.write(" ".join(i) )

# # 筛选度>100的较重要的人物关系
# f = codecs.open('result.txt','r',encoding='utf8')
# lines = f.readlines()
#
# A = []
# for line in lines:
#     A.append([])
#     m = line.strip('\n').split(' ')
#     for x in m:
#         A[-1].append(x)
# B = []
# for items in A:
#     try:
#         if int(items[-1]) > 100:
#             B.append(items)
#     except:
#         pass
#
# f.close()
# w = codecs.open('result1.txt', 'w', encoding='utf8')
# for i in B:
#     w.write(" ".join(i))