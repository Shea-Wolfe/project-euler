import math

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

def problem6():
    '''The sum of the squares of the first ten natural numbers is,
    12 + 22 + ... + 102 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first
    one hundred natural numbers and the square of the sum.'''
    num_list = [x for x in range(1, 101)]
    print(abs(sum([x**2 for x in num_list]) - sum(num_list)**2))

def problem7():
    '''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.
    What is the 10 001st prime number?'''
    primes_list = [2,3,5,7,11,13]
    current_number = 15
    while len(primes_list) < 10001:
        if new_prime(current_number, primes_list):
            primes_list.append(current_number)
        if str(current_number)[-1] == '3':
            current_number += 4
        else:
            current_number += 2
    print(primes_list[-1])

def problem8():
    '''The four adjacent digits in the 1000-digit number that have the
    greatest product are 9 × 9 × 8 × 9 = 5832.

    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450

    Find the thirteen adjacent digits in the 1000-digit number that
    have the greatest product. What is the value of this product?'''
    start = 0
    end = 13
    number = '''7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'''
    max_product = 0
    while end < 1001:
        product = 1
        current_list = [int(x) for x in number[start:end]]
        for x in current_list:
            product = product * x
        if product > max_product:
            max_product = product
        start += 1
        end += 1
    print(max_product)

def problem9():
    '''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a2 + b2 = c2
    For example, 32 + 42 = 9 + 16 = 25 = 52.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.'''
    for a in range(0,300):
        for b in range(0,400):
            if a + b + math.sqrt(a**2 + b**2) == 1000:
                print("The numbers are {},{},{}".format(a, b, 1000-a-b))
                print("The product is {}".format(a*b*(1000-a-b)))

def problem10():
    '''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.'''
    #A little slow but it gets there!
    primes_list = [2,3,5,7,11,13]
    current_number = 15
    while primes_list[-1] < 2000000:
        if new_prime(current_number, primes_list):
            primes_list.append(current_number)
        if str(current_number)[-1] == '3':
            current_number += 4
        else:
            current_number += 2
    print(sum(primes_list[:-1]))
