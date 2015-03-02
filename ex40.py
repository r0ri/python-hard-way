# define dictionary
mystuff_dict = {'apple': "I AM APPLES!"}

# import module
import mystuff

print mystuff_dict['apple'] # get apple from dict and print it
mystuff.apple() # get apple from the module
print mystuff.tangerine # same thing, it's just a variable and print it 

# define class MyStuff
class MyStuff(object):
	
	def __init__(self):
		self.tangerine = "And now a thousand years between"
		
	def apple(self):
		print "I AM A CLASSY APPLES!"
		
# instantiate object
thing = MyStuff()
thing.apple()
print thing.tangerine

# another exercise
print '-' * 10

class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
					"I Don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()