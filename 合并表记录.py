'''输入：
4
0 1
0 2
1 2
3 4

输出：
0 3
1 2
3 4
'''

entry = int(input())#总共有的表记录数
tinydict = {}
while True:
    try:
        temp = []#用来临时存储输入数据
        temp = list(map(int,input().split(' ')))
        if temp[0] not in tinydict:#如果字典里没有这条记录，创建一个新的记录
            tinydict[temp[0]] = temp[1]
        else:#如果有这条记录，将值更新
            tinydict[temp[0]] += temp[1]
    except:
        break
for k, v in sorted(tinydict.items()):#格式化并输出
    print(f'{k} {v}')