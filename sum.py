# sum.py
# Computes the sum of the first 4 positive integer

sum = 0

for i in range(1, 5):
    print 'sum is', sum
    print 'index is', i
    print 'adding', sum, '+', i
    sum = sum + i
print 'the sum of the first', i, 'positive integers is', sum