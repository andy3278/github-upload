from random import randint

lowest = 0
highest = int(input("The range you want to guess: "))
answer = randint(lowest, highest)

#重複猜數字，直到猜對為止
while True:
    guess = input('number bewteen :' + str(lowest) + '-' + str(highest) + ':\n>>')
    
    
    try:
        guess = int(guess)  #把字串轉換成整數
    except ValueError:  #轉換失敗便要求重新輸入數字
        print('plsease input number\n')
        continue
    
    #檢查輸入的數字是否介於規定範圍內
    if guess <= lowest or guess >= highest:
        print('plsease input bewteen :' + str(lowest) + '-' + str(highest) + ' \n')
        continue
    
    #判斷有沒有猜中密碼
    if guess == answer:
        print('you are correct！')
        break   #猜對才跳脫迴圈
    elif guess < answer:
        lowest = guess
    else:
        highest = guess