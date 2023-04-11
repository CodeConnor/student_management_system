# 定义age_input函数，判断用户输入数据的合理性
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


print(num_input('33'))

