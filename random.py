import random
x = random.randint(1,10)  #random is the module, 'randint' is a function in that module. randint takes two arguments
print(x)
y = random.random()
print(y)
print(random.randrange(0,30,5))  #same as randint, but the third argument specifies the 'step'. E.g. here it can only be 0,5,10,15,20,25
myList = [1,2,3,4,5]
random.shuffle(myList)
print(myList)

myList2 = [6,7,8,9,10]
print(random.choices(myList2))  #choices() allows you to choose 1 or more elements from a list randomly with a different probability
print(random.choices(myList2,weights=[80,40,20,10,5],k=5))  #'weights' specifies probability of each element being picked, 'k' is the list size
