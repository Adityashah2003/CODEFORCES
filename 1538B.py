test=int(input())
while test!=0:
     test-=1
     friends=int(input())
     candies=list(int,input().split())
     average=sum(candies)//friends
     if sum(candies)%friends!=0:
          print('-1')
          continue
     k=0
     for i in candies:
          if i > average:
               k+=1
     print(k)
     