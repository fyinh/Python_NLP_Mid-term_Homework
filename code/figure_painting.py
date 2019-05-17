# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def show_name_bar(name_list_sort, name_list_count):
    # x代表条形数量
    x = np.arange(len(name_list_sort))
    # 处理中文乱码
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 用来正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    # 绘制条形图，bars相当于句柄
    bars = plt.bar(x, name_list_count)
    # 给各条形打上标签
    plt.xticks(x, name_list_sort)
    # 设置题目
    plt.title("出场率高的前15位人物的频率直方图")
    # 显示各条形具体数量
    i = 0
    for bar in bars:
        plt.text((bar.get_x() + bar.get_width() / 2), bar.get_height(), '%d' % name_list_count[i], ha='center',
                 va='bottom')
        i += 1
    # 显示图形
    plt.show()

def show_name_pie(name_list_sort, name_list_count):
    # 处理中文乱码
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 用来正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    # 绘制饼状图
    plt.pie(name_list_count, labels=name_list_sort, autopct='%1.2f%%', shadow=True)
    # 设置题目
    plt.title("出场率高的前15位人物的比例饼图")
    # 显示图形
    plt.show()


def show_words_barh(words_list_sort, words_list_count):
    # x代表条形数量
    x = np.arange(len(words_list_sort))
    # 处理中文乱码
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 用来正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    # 绘制条形图，bars相当于句柄
    barhs = plt.barh(x, words_list_count, height=0.7, color='steelblue', alpha=0.8)
    # 给各条形打上标签
    plt.yticks(x, words_list_sort)
    # 设置题目
    plt.title("词频直方图")
    # 显示各条形具体数量
    for x, y in enumerate(words_list_count):
        plt.text(y + 0.2, x - 0.1, '%s' % y)
    # 显示图形
    plt.show()
