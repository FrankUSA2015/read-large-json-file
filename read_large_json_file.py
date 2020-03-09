# -*- coding: utf-8 -*-
#读取几个G的json文件的方法
#这个方法是一行一行的加载出来
import json
path1 =r""
with open(path1, 'r', encoding='utf-8') as f:
    try:
        while True :
            line_data = f.readline()
            if line_data:
               data= json.loads(line_data)#把读取的一行的json数据加载出来
            else:
                break
    except Exception as e:
        print(e)
        f.close()
