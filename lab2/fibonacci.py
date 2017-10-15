# fibonacci.py
# computes the nth fibonacci number

def fibonacci():
    print('hi, if you give me a positive integer > 2, then i\'ll tell you' +
    ' what fibonacci number is in that place.')

    n = int(input('what number? '))
    current = 1
    previous = 1

    for i in range(2, n + 1):
        previous = current
        current = current + previous

fibonacci()