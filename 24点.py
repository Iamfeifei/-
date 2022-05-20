'''
输入4个数字，利用加减乘除可以得出24的就输出true，否则输出false
递归解决
'''
def helper(arr,item):#先写一个利用递归+枚举解决算24的程序
    if item<1:
        return False
    if  len(arr)==1:#递归终点，当数组arr只剩一个数的时候，判断是否等于item
        return arr[0]==item
    else:#如果arr不是只剩一个数，就调用函数本身（直到只剩一个为止返回真假）
        for i in range(len(arr)):
            m=arr[0:i]+arr[i+1:]
            n=arr[i]
            if helper(m,item+n) or helper(m, item-n) or helper(m, item*n) or helper(m, item/n):
                return True
        return False

while True:
    try:
        if helper(list(map(int,input().split())), 24):
            print('true')
        else:
            print('false')
    except:
        break
