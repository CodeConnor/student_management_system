# 导入学生对象
from Student import Student
import os


# 定义管理系统对象
class StudentsManager(object):
    # 属性
    def __init__(self):
        # 定义空列表存储学生信息的对象
        self.students = []

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
        self.students.append(Student(name, age, gender))
        print('信息添加成功！')

    # 封装del_student方法，用于删除学生信息
    def del_student(self):
        name = input('请输入需要删除的学生姓名：')
        # 遍历学生列表
        for i in self.students:
            if i.name == name:
                self.students.remove(i)
                print('信息删除成功！')
                break
        else:
            print('未查询到该学生信息！')

    # 封装alter_student方法，修改学生信息
    def alter_student(self):
        old_name = input('请输入需要修改的学生姓名：')
        # 遍历学生列表
        for i in self.students:
            if i.name == old_name:
                # 提示用户输入
                i.name = input('请输入学生姓名：')
                # 过滤输入的年龄
                i.age = self.num_input(1)
                i.gender = input('请输入学生性别：')
                print('信息修改成功！')
                break
        else:
            print('未查询到该学生信息！')

    # 封装find_student方法，用于查找单个学生信息
    def find_student(self):
        if not self.students:
            print('暂无学生信息！')
        else:
            find_name = input('请输入需要查找的学生姓名：')
            for i in self.students:
                if i.name == find_name:
                    print(i)
                    return
            else:
                print('很抱歉，查询不到该学生！')

    # 封装show_students方法，遍历展示所有学生信息
    def show_students(self):
        if not self.students:
            print('暂无学生信息！')
        else:
            for i in self.students:
                print(i)

    # 封装save_data_to_file方法，用于保存数据至students.txt
    def save_data_to_file(self):
        # 创建空列表
        save_data = []
        # 遍历学生对象列表，获取学生信息
        for i in self.students:
            # 将对象i转换成字典，再使用列表存储学生信息
            save_data.append(i.__dict__)

        # 打开文件存储信息
        f = open('students.txt', 'w', encoding='utf-8')
        f.write(str(save_data))
        f.close()
        print('数据保存成功！')
        pass

    # 封装load_data_to_sys方法，用于从文件加载数据到系统
    def load_data_to_sys(self):
        # 检测文件是否存在
        if os.path.exists('students.txt'):
            # 读取文件
            f = open('students.txt', 'r', encoding='utf-8')
            content = f.read()
            load_data = eval(content)
            # 判断文件中是否有数据
            if len(load_data) == 0:
                print('暂无数据需要加载！')
            else:
                # 清空列表原数据，防止数据重复
                self.students = []
                # 遍历数据，将数据实例化为对象并存入列表
                for i in load_data:
                    self.students.append(Student(i['name'], i['age'], i['gender']))
                f.close()
                print('数据加载成功！')
        else:
            print('文件不存在，请先保存数据至文件！')

    # 定义run方法，启动项目
    def run(self):
        # 启动前将数据加载至系统
        self.load_data_to_sys()
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
                self.find_student()
            elif user_num == 5:
                self.show_students()
            elif user_num == 6:
                self.save_data_to_file()
            elif user_num == 7:
                self.load_data_to_sys()
            # 退出系统
            elif user_num == 8:
                print('已成功退出系统，欢迎下次使用！')
                break

            # 输入错误时，提示重新输入
            else:
                print('输入内容错误，请按提示重新输入！')
