# pattern_n.py
# creates the pattern N

def first_last():
    print('*', end='')
    for i in range(n):
        print(' ', end='')
    print('*')

def print_middle(num):
    print('*', end='')

    spaces_before = num - 1
    for i in range(spaces_before):
        print(' ', end='')

    print('*', end='')

    spaces_after = n - num
    for i in range(spaces_after):
        print(' ', end='')

    print('*')