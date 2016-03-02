def problem_1():
    final_sum = 0
    for number in range(1000):
        if number % 3 == 0:
            final_sum += number
        elif number % 5 == 0:
            final_sum+= number
        else:
            pass
    print(final_sum)
problem_1()
