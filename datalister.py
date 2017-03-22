import random, sys
from urllib import urlopen
from sys import exit

def menu():
    title = "-This a password cracking tool\n-Version (v1.0.0)\n-Created by @Gh0st3rZ_N4ti0N\n"
    print title
    url = raw_input('Enter the url you want to fuck with.\n\\\\ ')
    print "Selected: %s" % url
    
def check():
    datafile = file('example.txt')
    found = False
    for line in datafile:
        if word in line:
            found = True
            break

def appender(url):
    amount = 1
    entered_url = url
    word_url = "%s" % entered_url
    wordlist = open('wordlist.txt', 'a')
    for word in urlopen(word_url):
        print "(%r) Added: %s" % (amount, word)
        amount = amount + 1
        wordlist.write(word)

    print "Successfully written all words to file!"
    print "Closing down file & saving..."
    wordlist.close()
    print "*Close successful"
    print "*Save successful"
    exit(0)
menu()
def file_printer():
op = raw_input('Would you like to print out the file?\n>>> ')
if op == 'yes':
    wordlist = open('wordlist.txt', 'r')
    for word in wordlist:
        print word
    
elif op != 'yes':
    print 'Ok goodbye...'
    from sys import exit
    exit(0)
wordlist.close()