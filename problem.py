num=int(input("Enter any number:")) 


for i in range(1,10):
    tmp=num 
    while tmp!=0:
        rem=tmp%10
        tmp=tmp//10
        if rem==i:
            print(rem,end=',')
         
