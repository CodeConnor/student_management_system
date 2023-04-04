import os
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
    print('【6】保存数据到文件')
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


# 定义add_stu函数，实现添加学生信息
def add_stu():
    while True:
        global students
        name = input('请输入学生姓名：')
        # 判断是否输入的是数字
        while True:
            age_str = input('请输入学生年龄：')
            # 嵌套使用函数is_digit来判断
            age = is_digit(age_str)
            if not age:
                print('【输入错误，请按提示输入正确内容！】')
                continue
            else:
                break
        gender = input('请输入学生性别：')
        # 将信息存入字典和列表
        student = {}
        student['name'] = name
        student['age'] = age
        student['gender'] = gender
        students.append(student)
        user_cmd = input('【输入任意键继续】\n【输入q或者Q退出】\n:')
        # 判断退出或继续
        if user_cmd == 'q' or user_cmd == 'Q':
            break


# 定义del_stu函数，实现删除学生信息
def del_stu():
    while True:
        del_name = input('请输入所要删除的学生姓名：')
        # 遍历学生列表
        for i in students:
            # 判断学生姓名是否存在
            if i['name'] == del_name:
                students.remove(i)
                print(f'【{del_name}】信息已成功删除！')
                break
        # 遍历完成后，没查询到（没有break）时进行提示
        else:
            print('【很抱歉，查询不到该学生！】')

        user_cmd = input('【输入任意键继续】\n【输入q或者Q退出】\n:')
        # 判断退出或继续
        if user_cmd == 'q' or user_cmd == 'Q':
            break


# 定义alter_stu函数，实现修改学生信息
def alter_stu():
    while True:
        global students
        alter_name = input('请输入所要修改的学生姓名：')
        for i in students:
            if i['name'] == alter_name:
                # 提示输入修改信息
                name = input('请输入新学生姓名：')
                # 判断是否输入的是数字
                while True:
                    age_str = input('请输入学生年龄：')
                    age = is_digit(age_str)
                    if not age:
                        print('【输入错误，请按提示输入正确内容！】')
                        continue
                    else:
                        break
                gender = input('请输入新学生性别：')
                # 修改students列表内的字典
                i['name'] = name
                i['age'] = age
                i['gender'] = gender
                print(f'【{alter_name}】信息已成功修改！')
                break
        # 遍历完成后，没查询到（没有break）时进行提示
        else:
            print('【很抱歉，查询不到该学生！】')

        user_cmd = input('【输入任意键继续】\n【输入q或者Q退出】\n:')
        # 判断退出或继续
        if user_cmd == 'q' or user_cmd == 'Q':
            break


# 定义select_stu函数，查询单个学生的信息
def select_stu():
    while True:
        select_name = input('请输入所要查询的学生姓名：')
        for i in students:
            if i['name'] == select_name:
                print(f'姓名：{i["name"]}, 年龄：{i["age"]}, 性别：{i["gender"]}')
                break
        else:
            print('【很抱歉，查询不到该学生！】')

        user_cmd = input('【输入任意键继续】\n【输入q或者Q退出】\n:')
        # 判断退出或继续
        if user_cmd == 'q' or user_cmd == 'Q':
            break


# 定义show_all_stu函数，实现展示所有学生信息
def show_all_stu():
    # 判断students是否为空
    if not students:
        print('【暂无学生信息！】')
    # 非空则输出所有信息
    else:
        for i in students:
            print(f'姓名：{i["name"]}, 年龄：{i["age"]}, 性别：{i["gender"]}')


# 定义save_data_to_file函数，实现保存数据到txt文件
def save_data_to_file():
    global students
    f = open('students.txt', 'w', encoding='utf-8')
    # 判断列表是否为空
    if not students:
        print('【暂无数据需要保存！】')
    else:
        f.write(str(students))
        print('【数据保存成功！】')
    f.close()


# 定义load_data_to_sys函数，实现加载文件数据到系统中
def load_data_to_sys():
    global students
    # 判断文件是否存在，防止打开文件报错
    if not os.path.exists('students.txt'):
        print('【文件不存在，请先保存数据至文件！】')
    else:
        f = open('students.txt', 'r', encoding='utf-8')
        content = f.read()
        # 判断文件是否为空
        if not content:
            print('【文件为空，请先保存数据至文件！】')
        else:
            # content为str，需要将其转换为list
            students = eval(content)
            print('【数据加载成功！】')


# 系统的调用
while True:
    menu()
    user_str = input('请按照提示输入数字：')
    # 判断输入内容是否是数字
    user_num = is_digit(user_str)

    if user_num == 1:
        add_stu()
    elif user_num == 2:
        del_stu()
    elif user_num == 3:
        alter_stu()
    elif user_num == 4:
        select_stu()
    elif user_num == 5:
        show_all_stu()
    elif user_num == 6:
        save_data_to_file()
    elif user_num == 7:
        load_data_to_sys()

    # 退出系统
    elif user_num == 8:
        print('【已成功退出系统，欢迎下次使用！】')
        break

    # 当用户输入错内容时，返回功能提示菜单
    else:
        print('【输入错误，请按提示输入正确内容！】')
