def addition(sum_01, sum_02):
    answer = sum_01 + sum_02
    print "%d + %d = %d" % (sum_01, sum_02, answer)
    main_menu()

def subtraction(sum_01, sum_02):
    answer = sum_01 - sum_02
    print "%d - %d = %d" % (sum_01, sum_02, answer)
    main_menu()

def multiplication(sum_01, sum_02):
    answer = sum_01 * sum_02
    print "%d x %d = %d" % (sum_01, sum_02, answer)
    main_menu()

def division(sum_01, sum_02):
    answer = sum_01 / sum_02
    print "%d / %d = %d" % (sum_01, sum_02, answer)
    main_menu()

def main_menu():
    print "Welcome to simple calculator (version 1.0.0)"
    print "What would you like to do ?"
    klop = input("(1)\t-Addition\n(2)\t-Subtraction\n(3)\t-Multiplication\n(4)\t-division\n> ")

    if klop == 1:
        sum_01 = input("Enter sum: ")
        sum_02 = input("Enter sum: ")
        addition(sum_01, sum_02)

    elif klop == 2:
        sum_01 = input("Enter sum: ")
        sum_02 = input("Enter sum: ")
        subtraction(sum_01, sum_02)

    elif klop == 3:
        sum_01 = input("Enter sum: ")
        sum_02 = input("Enter sum: ")
        multiplication(sum_01, sum_02)

    elif klop == 4:
        sum_01 = input("Enter sum: ")
        sum_02 = input("Enter sum: ")
        division(sum_01, sum_02)

    else:
        from sys import exit
        print "Exiting..."
        exit(0)

main_menu()