for i in range(0,1000):
    num = i*i+i+41
    for j in range(2,num):
        if (num % j) == 0:  
            break  
    else:  
        print(num,"is a prime number")  
    i+=1