'''最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
'''

def maxFront(list1):
    temp =[]
    temp2 = []
    output = ''
    # 所有的前缀
    for item in list1:
        for i in range(len(item)):
            temp.append(item[0:i+1])
    # 所有的公共前缀
    for item in temp:
        if temp.count(item) > 1 and temp.count(item) == len(list1):
            temp2.append(item)
    #排序，最长的在前面
    temp2.sort(reverse=True)
    #如果有公共前缀才输出
    if temp2 != []:
        output = temp2[0]
    return output

string = maxFront(["application","applicant ","apple"])
print(string)
