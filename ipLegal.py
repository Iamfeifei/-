while True:
    try:
        string = input().split('.')
        result = 'YES'
        if len(string) != 4:
            result = 'NO'
        for item in string:
            if not item.isdigit():
                result = 'NO'
                break
            elif int(item)>255 or int(item) <0:
                result = 'NO'
                break
            elif item.startswith('0') and len(item)>1:
                result = 'NO'
                break
        print(result)
    except:
        break