"""
完全数等于除了它本身的约数的和
例如28的约数为1，2，4，7，14，28
1+2+4+7+14=28

1.用完全数性质筛选备选数
（1）所有的完全数都是三角形数。例如：6=1+2+3；28=1+2+3+...+6+7；
496=1+2+3+...+30+31；8128=1+2+3…+126+127。
（2）完全数都是以6或28结尾。（科学家仍未发现由其他数字结尾的完全数。）
2.验证是否为完全数
"""
while True:
    try:
        n = int(input())
    except:
        break
    else:
        list1 = []  # 备选数
        list2 = []  # 完全数
        a = 0  # 性质(1)累加
        for i in range(1, n):
            a += i
            if a > n:  # 超出范围跳出循环
                break
            else:
                if a % 10 == 6:
                    list1.append(a)
                elif a % 100 == 28:
                    list1.append(a)

        for x in list1:
            list3 = []
            for y in range(1, int(x / 2 + 1)):  # 求因子
                if x % y == 0:
                    list3.append(y)
            if sum(list3) == x:  # 验证完全数
                list2.append(x)

        print(len(list2))

