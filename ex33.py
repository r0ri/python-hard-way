def counter_function(it_max, step_size):
	i = 0
	numbers = []
	
	while i < it_max:
		print "At the top i is %d" % i 
		numbers.append(i)
	
		i += step_size
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i 
	
	print "The numbers: "
	
	for num in numbers:
		print num
		
	print "And now with a for-loop:"
	numbers_for = []
	for i in range(0, it_max, step_size):
		
		print "At the top i is %d" % i
		numbers_for.append(i)
		
		print "Numbers now:", numbers_for
		print "At the bottom i is the same: %d" % i
		
	print "The numbers from the for loop: "
	
	for num in numbers:
		print num
		
counter_function(8, 2)