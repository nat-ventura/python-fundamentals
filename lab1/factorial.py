# factorial.py
# gets n number from user
# calculates product of first n positive integers

def facty():
    inputNum = int(input('please enter a positive integer' +
                ' and i will calculate the product counting' +
                ' up to your integer.\nalso i\'ll be your' +
                ' friend: '))
    product = inputNum

    if inputNum > 0:
        for i in range(2, inputNum + 1):
            print 'product is ', product
            print 'multiplying index', i, '* product', product
            product = i * product
        print ('lol the first time i did this, i totally didn\'t' +
        ' start from index 0 i promise.')

facty()