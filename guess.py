import random
upper=int(input())
lower=int(input())
random= random.randint(upper,lower)
count=0
marks=100
while (count<=3):
    guess=int(input())
    if (guess == random):
        print("your answer is correct your mark is ",marks)
        break
    elif (count==0):
        count=count+1
        marks=marks-5
        if(guess<random):
            print("number u entered is too small")
        else:
            print("number u entered is too large")
    elif(count==1):
        count=count+1
        marks=marks-10
        if(random%2==0):
            print("the system generated number is even")
        else:
            print("the system generated number is odd")
    elif(count==2):
        count=count+1
        marks=marks-30
        for i in range (3,10):
            if(random%i == 0):
                print("random num is divisible by" ,i)
            else:
                print ("it is not divisible by ",i)
    elif(count==3):
        print("u lost ur opportunity")
        marks=0
        print(marks)
        break
            
