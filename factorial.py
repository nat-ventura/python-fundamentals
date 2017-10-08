# factorial.py
# gets n number from user
# calculates product of first n positive integers

def facty():
    inputNum = int(input('please enter a positive integer' +
                ' and i will calculate the product counting' +
                ' up to your integer.\nalso i\'ll be your' +
                ' friend.'))
    product = 0

    if inputNum < 0:
        for i in range(inputNum):
            print 'product is ', product
            print 'multiplying index', i, '* product', product
            product = i * product

facty()