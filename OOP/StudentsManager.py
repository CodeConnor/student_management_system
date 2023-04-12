# 定义管理系统对象
class StudentsManager(object):
    # 属性

    # 方法
    # 定义run方法，启动项目
    @staticmethod
    def run():
        print('-' * 40)
        print('            学生管理系统v2.0')
        print('【1】添加学生信息')
        print('【2】删除学生信息')
        print('【3】修改学生信息')
        print('【4】查询学生信息')
        print('【5】显示所有学生信息')
        print('【6】保存数据到文件')
        print('【7】加载数据到系统')
        print('【8】退出系统')
        print('-' * 40)