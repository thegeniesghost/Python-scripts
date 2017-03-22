from sys import argv
script = argv
print "The", script, "is running."
user_data = raw_input("Would you like to keep this script running?\nY/N?\n>>> ")
if user_data == 'Y':
    de = 'continue'

elif user_data == 'N':
    de = 'quit'

try:
    if 'de' in locals():
        print "You have chosen to", de