# sum.py
# Computes the sum of the first 4 positive integer

def summy():
    inputNum = int(input('please give me an integer and' +
               ' i will output the first "n" integers' +
               ' of my summy function: '))
    sum = 0

    if inputNum == 0:
        print "zero is not a positive or negative integer,' +
        ' i have nothing to sum! bye!"

    elif inputNum < 0:
        for i in range(0, inputNum, -1):
            print 'adding index', i, 'to sum', sum
            sum = i - sum
            print 'this is my summm :)', sum

    else:
        for i in range(inputNum):
            print 'adding index', i, 'to sum', sum
            sum = i + sum
            print 'this is my summm :)', sum

summy()