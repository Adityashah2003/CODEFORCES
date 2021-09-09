n = int(input())
while n != 0 :
    word = input()
    if len(word)>10 :
        a = len(word) - 2
        print(word[0] + str(a) + word[-1])
    else:
        print(word)
    n = n-1



