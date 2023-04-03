# 定义列表存储学生信息
students = []


# 定义menu函数，实现对系统功能界面的输出
def menu():
    print('-' * 40)
    print('            学生管理系统v1.0')
    print('【1】添加学生信息')
    print('【2】删除学生信息')
    print('【3】修改学生信息')
    print('【4】查询学生信息')
    print('【5】显示所有学生信息')
    print('【6】保存数据到系统')
    print('【7】加载数据到系统')
    print('【8】退出系统')
    print('-' * 40)


# 定义is_digit函数，判断用户是否输入数字
def is_digit(user_str):
    try:
        num = int(user_str)
        return num
    except:
        return


# 系统的调用
while True:
    menu()
    user_str = input('请按照提示输入数字：')
    # 判断输入内容是否是纯数字
    user_num = is_digit(user_str)

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

    # 当用户输入错内容时，返回功能提示菜单
    else:
        print('输入错误，请按提示输入正确内容！')
