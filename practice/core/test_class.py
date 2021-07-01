# -*- coding: UTF-8 -*-
# 基础包：生成签名

class Tools(object):

    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的个数 %s" % cls.count )


    def __init__(self, name):
        self.name = name

        Tools.count += 1


# 创建工具对象
tool1 = Tools("斧头")
tool2 = Tools("xx")

# 调用类方法
Tools.show_tool_count()




