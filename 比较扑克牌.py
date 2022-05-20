'''
输入4 4 4 4-joker JOKER（两副手牌，比较大小）
手牌有单张，对子，三张，炸弹，顺子，王炸几种，
只有炸弹和王炸可以和任意牌比较
不能比较的时候输出ERROR
'''

while True:
    try:
        s1, s2 = input().split('-')
        a, b = s1.split(), s2.split()
        n1, n2 = len(a), len(b)
        d = {'3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':15, 'joker':16, 'JOKER':17}
        if s1 == 'joker JOKER' or s2 == 'joker JOKER': # 对王最大
            print('joker JOKER')
            break
        if n1 == n2:
            if d[a[0]] > d[b[0]]: # 相同类型的比较牌面大小
                print(s1)
            else:
                print(s2)
        else: # 炸弹和其他类型相比：输出炸弹
            if n1 == 4:
                print(s1)
            elif n2 == 4:
                print(s2)
            else: # 除了炸弹和对王，长度不同不存在比较关系
                print('ERROR')
    except:
        break