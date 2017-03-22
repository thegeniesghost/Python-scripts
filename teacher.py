# This is a artificial math teacher hope you like it ladies/gents !
# There is an error when the user does not enter anything when prompted to answer a question who can fix this please ?
# I have not studied error messages just yet forgive me Sir/Madam ;)
import random
from sys import exit
def random_addition(rs, re):
    sum1 = random.choice(range(rs, re))
    sum2 = random.choice(range(rs, re))
    answer = sum1 + sum2
    q = input("%d + %d = " % (sum1, sum2))
    if q == answer:
        print "Correct!"
        e = raw_input('Would you like to go again?\n>>> ')
        
        if e == 'yes':
            random_addition(rs, re)

        elif e == 'no':
            print "Returning to main menu..."
            main_menu(rs, rs)
    
    elif q != answer:
        print "Incorrect!\nThe answer is %d\nPlease try again..." % answer
        random_addition(rs, re)

    else:
        print "Invalid input..."
        random_addition(rs, re)
def random_subtraction(rs, re):
    sum1 = random.choice(range(rs, re))
    sum2 = random.choice(range(rs, re))
    answer = sum1 - sum2
    q = input("%d - %d = " % (sum1, sum2))
    if q == answer:
        print "Correct!"
        e = raw_input('Would you like to go again?\n>>> ')
        
        if e == 'yes':
            random_subtraction(rs, re)

        elif e == 'no':
            print "Returning to main menu..."
            main_menu(rs, rs)
    
    elif q != answer:
        print "Incorrect!\nThe answer is %d\nPlease try again..." % answer
        random_subtraction(rs, re)
    
    else:
        print "Invalid input..."
        random_subtraction(rs, re)

def random_multiplication(rs, re):
    sum1 = random.choice(range(rs, re))
    sum2 = random.choice(range(rs, re))
    answer = sum1 * sum2
    q = input("%d * %d = " % (sum1, sum2))
    if q == answer:
        print "Correct!"
        e = raw_input('Would you like to go again?\n>>> ')
        
        if e == 'yes':
            random_multiplication(rs, re)

        elif e == 'no':
            print "Returning to main menu..."
            main_menu(rs, rs)
    
    elif q != answer:
        print "Incorrect!\nThe answer is %d\nPlease try again..." % answer
        random_multiplication(rs, re)

    else:
        print "Invalid input..."
        random_multiplication(rs, re)
def random_division(rs, re):
    sum1 = random.choice(range(rs, re))
    sum2 = random.choice(range(rs, re))
    answer = sum1 / sum2
    q = input("%d / %d = " % (sum1, sum2))
    if q == answer:
        print "Correct!"
        e = raw_input('Would you like to go again?\n>>> ')
        
        if e == 'yes':
            random_division(rs, re)

        elif e == 'no':
            print "Returning to main menu..."
            main_menu(rs, rs)
    
    elif q != answer:
        print "Incorrect!\nThe answer is %d\nPlease try again..." % answer
        random_division(rs, re)

    else:
        print "Invalid input..."
        random_division(rs, re)

print "Before we start i will need to know what difficulty you would like to begin on..."
print "Please select and option,\n-Easy\t(easy)\n-Medium\t(medium)\n-Hard\t(hard)"
dif = raw_input('>>> ')
if dif == 'easy':
    rs = 10
    re = 25

elif dif == 'medium':
    rs = 25
    re = 50

elif dif == 'hard':
    rs = 50
    re = 100

else:
    print "Error has accured please restart cmd/terminal..."
    exit(0)



print "You have selected %s as you're difficulty setting great let's get started!\n\n\n\n\n\n\n\n\n\n" % dif

def main_menu(rs, re):
    s = input('What would you like to do?\n(1)\t-Addition\n(2)\t-Subtraction\n(3)\t-Multiplication\n(4)\t-Division\n>>> ')
    if s == 1:
        random_addition(rs, re)

    elif s == 2:
        random_subtraction(rs, re)

    elif s == 3:
        random_multiplication(rs, re)

    elif s == 4:
        random_division(rs, re)

    else:
        print "Invalid input..."
        main_menu(rs, re)

main_menu(rs, re)