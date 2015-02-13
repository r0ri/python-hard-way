def banana_ape(banana_count, monkey_count, crocodile_count):
	print "There are %d bananans." % banana_count
	print "And %d monkeys." % monkey_count
	print "That's %d bananas per monkey." % (banana_count/monkey_count)
	print "Unfortunatelly, they are being chased by %d crocodiles." % crocodile_count
	print "Oh snap.\n"
	
b = raw_input("# Bananas: ")
m = raw_input("# Monkeys: ")
c = raw_input("# Crocodiles: ")

banana_ape(int(b), int(m), int(c))