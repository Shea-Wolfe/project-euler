import pdb


def problem16():
    """2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2**1000?"""
    starting_number = 2**1000
    summed_number = 0
    for number in str(starting_number):
        summed_number += int(number)
    print(summed_number)

def problem17():
    """if the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    in words, how many letters would be used?"""
    def hundreds_count(number):
        if int(number) == 1:
            return len("onehundred")
        elif int(number) == 2:
            return len("twohundred")
        elif int(number) == 3:
            return len("threehundred")
        elif int(number) == 4:
            return len("fourhundred")
        elif int(number) == 5:
            return len("fivehundred")
        elif int(number) == 6:
            return len("sixhundred")
        elif int(number) == 7:
            return len("sevenhundred")
        elif int(number) == 8:
            return len("eighthundred")
        elif int(number) == 9:
            return len("ninehundred")
    def tens_count(number):
        if int(number) == 2:
            return len("twenty")
        elif int(number) == 3:
            return len("thirty")
        elif int(number) == 4:
            return len("forty")
        elif int(number) == 5:
            return len("fifty")
        elif int(number) == 6:
            return len("sixty")
        elif int(number) == 7:
            return len("seventy")
        elif int(number) == 8:
            return len("eighty")
        elif int(number) == 9:
            return len("ninety")
        else:
            return 0
    def teens_count(number):
        if int(number) == 1:
            return len("eleven")
        elif int(number) == 2:
            return len("twelve")
        elif int(number) == 3:
            return len("thirteen")
        elif int(number) == 4:
            return len("fourteen")
        elif int(number) == 5:
            return len("fifteen")
        elif int(number) == 6:
            return len("sixteen")
        elif int(number) == 7:
            return len("seventeen")
        elif int(number) == 8:
            return len("eighteen")
        elif int(number) == 9:
            return len("nineteen")
        else:
            return len("ten")
    def ones_count(number):
        if int(number) == 1:
            return len("one")
        elif int(number) == 2:
            return len("two")
        elif int(number) == 3:
            return len("three")
        elif int(number) == 4:
            return len("four")
        elif int(number) == 5:
            return len("five")
        elif int(number) == 6:
            return len("six")
        elif int(number) == 7:
            return len("seven")
        elif int(number) == 8:
            return len("eight")
        elif int(number) == 9:
            return len("nine")
        else:
            return 0
    total_sum = len("onethousand") #So we don't need to worry about that one case
    numbers_list = [str(x) for x in range(1,1000)]
    for number in numbers_list:
        if len(number) == 3:
            total_sum += hundreds_count(number[0])
            if number[1] != "0" or number[2] != "0":
                total_sum += len("and")
            if number[1] == "1":
                total_sum += teens_count(number[2])
            else:
                total_sum += tens_count(number[1])
                total_sum += ones_count(number[2])
        elif len(number) == 2:
            if number[0] == "1":
                total_sum += teens_count(number[1])
            else:
                total_sum += tens_count(number[0])
                total_sum += ones_count(number[1])
        else:
            total_sum += ones_count(number)
    pdb.set_trace()
    print(total_sum)

problem17()
