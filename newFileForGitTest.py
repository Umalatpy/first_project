def myFunction(anyList):
    try:

        anyList = list(anyList)
        anyList.insert(-1, ' and ')
        anyList[-1] = anyList[-2] + anyList[-1]
        del anyList[-2]
        print(anyList[:])
    except IndexError:
        print('Mi skuzi, please type something')
        return myFunction(input())


print('Type anything please or press enter:')
# myFunction(input())
spam = ['apples', 'bananas', 'tofu', 'cats']
myFunction(spam)
allFlips = ['All my flips are here']
import random
for flips in range(0, 10000):
    allFlips = list(allFlips)
    if random.randint(0, 1) == 0:
        allFlips.append('T')
    else:
        allFlips.append('H')
print(allFlips)
print(len(allFlips))

# for index in allFlips[:]:
print('Chance of streak: %s%%' % (allFlips / 100000))
