while True:
    try:
        string = input()
        count = -1
        for char in string:
            if string.count(char) == 1:
                count = char
                break
        print(count)
    except:
        break