print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print "This is a test for some new input methods!"
print "Where are you located?",
location = raw_input('\n> ')

print "Location: %s\nAdded to database for analysis..." % location

print "Please enter you're fav number dude!\n> ",
fav_num = int(raw_input())
print "Your number is now mine MUhahahaha!"
print fav_num + fav_num * 1000
print "System malfunction [ERROR 987740]\nShutting down..."