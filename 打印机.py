def check(nums):
    count = 0
    for i in range(len(nums)):
        item = nums[i]
        if nums.count(item)==1:
            count+=1
        else:
            nums[i] = 1 + item
    if count == len(nums):
        return nums
    else:
        return check(nums)

while True:
    try:
        prios = list(map(int,input().split(',')))
        temp = sorted(prios,reverse= True)
        order = []
        indexs = []
        for i in range(len(prios)):
            indexs.append(i)
        for item in prios:
            i = temp.index(item)
            if i in order:
                ith = order.count(i)
                a = int(i+ith)
                order.append(a)
            else:
                order.append(i)
            #temp.remove(item)
        order = check(order)
        print(','.join(map(str,order)))
    except:
        break