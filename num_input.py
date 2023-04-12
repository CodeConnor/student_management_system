# 定义num_input函数，判断用户输入数据的合理性
def num_input(func):
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
                # 判断数据范围合理性
                if 0 < num < 9:
                    return num
                else:
                    return
            else:
                return

if __name__ == '__main__':
    # print(num_input(1))
    print(num_input(2))

