# 导入学生对象
from Student import Student
# 定义管理系统对象
class StudentsManager(object):
    # 属性
    def __init__(self):
        # 定义空列表存储学生信息的对象
        self.__students = []

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
    def num_input(self, func):
        # 当输入为1时，判断输入的年龄数据是否合理
        if func == 1:
            while True:
                user_input = input('请输入学生年龄：')
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

        # 当输入为2时，判断输入的功能编号是否合理
        elif func == 2:
            while True:
                user_input = input('请按提示输入您要执行的功能编号：')
                # 判断用户是否输入为空
                if not user_input:
                    return
                # 判断输入是否是纯数字
                elif user_input.isdigit():
                    num = int(user_input)
                    return num
                else:
                    return

    # 封装add_student方法，用于添加学生信息
    def add_student(self):
        # 提示用户输入
        name = input('请输入学生姓名：')
        # 过滤输入的年龄
        age = self.num_input(1)
        gender = input('请输入学生性别：')
        # 将信息生成学生对象，并将对象存入列表中
        self.__students.append(Student(name, age, gender))
        print(f'学生{name}, 信息添加成功！')

    # 封装del_student方法，用于删除学生信息
    def del_student(self):
        name = input('请输入需要删除的学生姓名：')
        # 遍历学生列表
        for i in self.__students:
            if i.get_student() == name:
                self.__students.remove(i)
                print(f'学生{name}, 信息删除成功！')
                break
        else:
            print('未查询到该学生信息！')

    # 封装alter_student方法，修改学生信息
    def alter_student(self):
        name = input('请输入需要删除的学生姓名：')
        pass

    # 封装show_students方法，遍历展示所有学生信息
    def show_students(self):
        if not self.__students:
            print('暂无学生信息！')
        else:
            for i in self.__students:
                print(i)

    # 定义run方法，启动项目
    def run(self):
        while True:
            # 打印菜单
            StudentsManager.menu()
            # 提示用户输入，并判断输入数字的合理性
            user_num = self.num_input(2)
            # 根据输入执行相应功能
            if user_num == 1:
                self.add_student()
            elif user_num == 2:
                self.del_student()
            elif user_num == 3:
                self.alter_student()
            elif user_num == 4:
                pass
            elif user_num == 5:
                self.show_students()
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
