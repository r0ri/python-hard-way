x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# 2 times string in a string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# 1 time string in string -> 3 total
print "I said: %r." % x
# 1 time s in s -> 4 total
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# 5 times
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e