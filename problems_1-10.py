def problem1():
    '''If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.'''
    final_sum = 0
    for number in range(1000):
        if number % 3 == 0:
            final_sum += number
        elif number % 5 == 0:
            final_sum += number
        else:
            pass
    print(final_sum)
problem1()


def problem2():
    '''Each new term in the Fibonacci sequence is generated
    by adding the previous two terms.
    By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values
    do not exceed four million, find the sum of the even-valued terms.'''
    fib_list = [1,2]
    final_sum = 0
    while fib_list[-1] < 4000000:
        fib_list.append(fib_list[-1]+fib_list[-2])
    for number in fib_list:
        if number % 2 == 0:
            final_sum += number
        else:
            pass
    print(final_sum)
problem2()
