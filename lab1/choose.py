# choose.py
# gets two integer sfrom the user (n and k)
# and computes n choose k
# aka counts the number of ways you can choose k objects 
# from a set of n distinct objects
# and can be computed as n! / (k! * (n-k)!)

def choosey():
    n = int(input('give me one number please! '))
    k = int(input('give me another number please! '))

    n_fact = 1
    for i in range(2, n + 1):
        n_fact = n_fact * i

    k_fact = 1
    for i in range(2, n + 1):
        k_fact = k_fact * i

    # calculate n-k
    selection = n - k
    nk_fact = 1
    for i in range(2, selection + 1):
        nk_fact = nk_fact * i

    choose = n_fact / (k_fact * nk_fact)

    print(n, 'choose', k, 'is:', choose)

choosey()