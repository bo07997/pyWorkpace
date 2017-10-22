def setclosure(passline):
    def cmp(val):#passline属性依附在cmp里 闭包
        if val > passline:
            print("Pass")
        else:
            print("failed")
    return cmp
# f_100 = setclosure(90)
# f_150 = setclosure(60)
# print(f_100(59))


################################################################# 闭包传函数
def setclosue_two(func):
    def judge(*arg):
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val,int):
                return 0
        return func(*arg)
    return judge
def judge_two(*args):
    return sum(args)/len(args)

# test = setclosue_two(judge_two)
#
# print(test(1, 2, 3, 4, 5))

######################################装饰器实现闭包

def setclosue_three(func):
    def judge(*arg):
        if len(arg) == 0:
            return 0
        for val in arg:
            print("验证", val)
            if not isinstance(val, int):
                return 0
        return func(*arg)
    print("111")
    return judge

@setclosue_three  #相当于改了引用
def judge_three(*args):
    return sum(args)/len(args)

print(judge_three(0, 1, 2, "3"))