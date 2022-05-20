while True:
    try:
        num1,array1 = int(input()), list(map(int,input().split()))
        num2,array2 = int(input()), list(map(int,input().split()))
        arrayOutput=[]
        for item in array1:
            if item not in array1:
                arrayOutput.append(item)
        for item in array2:
            if item not in array2:
                arrayOutput.append(item)
        arrayOutput.sort()
        for i in range(len(arrayOutput)):
            print(arrayOutput[i],end='')
    except:
        break