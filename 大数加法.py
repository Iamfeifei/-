while True:
    try:
        s1 = list(map(int, input()))
        s2 = list(map(int, input()))
        s1.reverse()
        s2.reverse()
        res = ""
        i = 0  # 遍历指针
        addd = 0  # 进位
        summ = 0  # 和
        while i < max(len(s1), len(s2)):  # 开始遍历
            a = 0 if i >= len(s1) else s1[i]  # 获取s1中的一位数字
            b = 0 if i >= len(s2) else s2[i]  # 获取s2中的一位数字
            #if语句确保位数不等时，a或b取0
            summ = (addd + a + b) % 10  # 计算和
            addd = (addd + a + b) // 10  # 计算进位
            res = str(summ) + res  # 组织到输出字符串中
            i += 1
        if addd > 0:  # 处理最后一位
            res = "1" + res
        print(res)  # 输出
    except:
        break


