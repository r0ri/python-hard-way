from sys import argv

script, first, second, third = argv

text = raw_input("What day is today? ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print first + ' ' + text
print int(second) + 3