# 定义学生对象
class Student(object):
    # 属性
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    # 方法和接口
    def __str__(self):
        stu_info = f'姓名：{self.__name} 年龄：{self.__age} 性别：{self.__gender}'
        return stu_info

    def get_student(self):
        return self.__name

# 测试该模块
if __name__ == '__main__':
    stu = Student('Tom', 20, 'male')
    print(stu)
