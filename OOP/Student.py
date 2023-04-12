# 定义学生对象
class Student(object):
    # 属性
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 方法和接口
    def __str__(self):
        stu_info = f'姓名：{self.name} 年龄：{self.age} 性别：{self.gender}'
        return stu_info


# 测试该模块
if __name__ == '__main__':
    stu = Student('Tom', 20, 'male')

    print(stu('T', 20, 'male'))
