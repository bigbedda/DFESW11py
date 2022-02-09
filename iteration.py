#import random
#secretNumber = random.randint(1,9)
#print('I\'m thinking of a number between 1 and 9')


#for guessesTaken in range(1,10):
    #print('take a guess.')
    #guess = int(input())
    #if guess < secretNumber:
     #   print('Your guess is too low')
    #elif guess > secretNumber:
    #    print('Your guess is too high')
   # else:
  #      break

#if guessesTaken == secretNumber:
#    print('well guessed')
#else:
#    print('please try again')


x=[1,2,3,4,5,6]

#for x in range(1,7):
#    if(x ==3 or x == 6):
#        continue
#    print(x)


items = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
print( ",".join(items))

