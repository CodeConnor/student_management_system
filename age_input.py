# 定义age_input函数，判断用户输入数据的合理性
def age_input():
    while True:
        user_input = input('请输入学生年龄：')
        if user_input:
            if user_input.isdigit():
                age = int(user_input)
                if 0 < age < 200:
                    return age
                else:
                    print('输入的年龄范围不合理，请重新输入！')
                    continue
            else:
                print('输入内容错误，请重新输入！')
                continue
        else:
            print('输入内容为空，请重新输入！')


print(age_input())

