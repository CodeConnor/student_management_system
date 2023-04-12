# 定义管理系统对象
class StudentsManager(object):
    # 属性

    # 方法
    # 封装一个menu方法，打印系统菜单
    @staticmethod  # 该方法无需访问属性和调用方法，所以是静态方法
    def menu():
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

    # 封装num_input方法，判断用户输入数据的合理性
    @staticmethod
    def num_input(user_input):
        while True:
            # 判断用户是否输入为空
            if user_input:
                # 判断输入是否是纯数字
                if user_input.isdigit():
                    num = int(user_input)
                    # 判断年龄范围合理性
                    if 0 < num < 200:
                        return num
                    else:
                        print('输入的数值范围不合理，请重新输入！')
                        continue
                else:
                    print('输入内容错误，请重新输入！')
                    continue
            else:
                print('输入内容为空，请重新输入！')

    # 定义run方法，启动项目
    def run(self):
        while True:
            # 打印菜单
            StudentsManager.menu()
            # 提示用户需要执行的功能
            user_input = input('请按提示输入您要执行的功能编号：')
            # 判断输入数字的合理性
            user_num = StudentsManager.num_input(user_input)
            # 根据输入执行相应功能
            if user_num == 1:
                pass
            elif user_num == 2:
                pass
            elif user_num == 3:
                pass
            elif user_num == 4:
                pass
            elif user_num == 5:
                pass
            elif user_num == 6:
                pass
            elif user_num == 7:
                pass
            # 退出系统
            elif user_num == 8:
                print('已成功退出系统，欢迎下次使用！')
                break

            # 输入错误时，提示重新输入
            else:
                print('输入内容错误，请按提示重新输入！')
