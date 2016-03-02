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


def problem3():
    '''The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?'''
    primes_list = [2,3,5,7,11,13]
    current_number = 15
    while len(primes_list) < 10000:
        if new_prime(current_number, primes_list):
            primes_list.append(current_number)
        if str(current_number)[-1] == '3':
            current_number += 4
        else:
            current_number += 2
    for prime in primes_list:
        if 600851475143 % prime == 0:
            print(prime)


def new_prime(number, primes_list):
    'Helper function for problem 3.  Finds primes.'
    for prime in primes_list:
        if number % prime == 0:
            return False
        else:
            pass
    return True

def problem4():
    '''A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.'''
    first_num = [x for x in range(1, 1000)]
    second_num = [x for x in range(1, 1000)]
    highest_palindrome = 9
    for x1 in first_num:
        for x2 in second_num:
            number = x1 * x2
            if is_palindrome(str(number)):
                if number > highest_palindrome:
                    highest_palindrome = number
                else:
                    pass
            else:
                pass
    print(highest_palindrome)

def is_palindrome(sentence):
    ''' Uses recursive methods to check for palindromes
        Helper function for problem4'''
    if len(sentence) <=1:
        return True
    else:
        if sentence[0] == sentence[-1]:
            return is_palindrome(sentence[1:-1])
        else:
            return False

def problem5():
    '''2520 is the smallest number that can be divided by each
    of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible
    by all of the numbers from 1 to 20?'''
    starting_number = 2520
    while divisible_check(starting_number) is False:
        starting_number += 20
    print(starting_number)


def divisible_check(number):
    'Helper function for problem 5.  Checks divisiblity for 1-20. if yes returns True'
    for divisor in range(1,21):
        if number % divisor != 0:
            return False
        else:
            pass
    return True

problem5()
