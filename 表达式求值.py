'''输入：
400+5

输出：
405'''
while True:
    try:
        print(int(eval(input())))#输入一串字符串的计算式，包含+ - * / ， 0-9
    except:
        break