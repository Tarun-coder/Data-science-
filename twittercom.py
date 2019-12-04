# Twitter comment character lenth limit Problem:


character=input("Enter the Comment:")

def classifier(character):
    a=len(character)
    print("The lenth of tweet is:",a)
    lis=[]
    lis_1=[]
    tweet_lis=[]
    if a>10:
        for i in range(0,a,10):
            b=character[i:i+10]
            lis.append(b)
        n=len(lis)
        for i in range(1,n+1):
            b=str((i,n))
            lis_1.append(b)
        for i in range(n):

            g=lis[i] + lis_1[i] 
            tweet_lis.append(g)
        print(tweet_lis)       
    else:
        print(character)    


        

classifier(character)  








