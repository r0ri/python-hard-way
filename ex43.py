from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		# be sure to pint out the last scene
		current_scene.enter()
		
class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud... if she were smart.",
		"Such a luser.",
		"I have a small puppy that is better at this than you."]
		
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew.  You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body.  He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."
		
		action = raw_input("> ")
		
		if action == "shoot!":
			print "You miss. You idiot. That's it for you."
			return 'death'
			
		elif action == "dodge!":
			print "Your doding fails."
			return 'death'
			
		elif action == "tell a joke":
			print "very funny, the gothon laughs himself to death"
			return 'laser_weapon_armory'
			
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'
			
class LaserWeaponArmory(Scene):

	def enter(self):
		print "Enter 1 digit code. FAST!"
		# code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		code = "%d" % (randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 1
		
		while guess != code and guesses < 10:
			print "BZZZEDDDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")
			
		if guess == code:
			print "Yay, you guesses right. That was highly improbable."
			return 'the_bridge'
			
		else:
			print "Well, that didn't work out. Too bad. The door is now locked forever."
			return 'death'
			
		
class TheBridge(Scene):

	def enter(self):
		print "You silently enter the bridge and spot MORE GOTHONS!"
		print "They haven't noticed you yet. What do you do with the bomb?"
		action = raw_input("> ")
		
		if action == "throw the bomb":
			print "You miss and hit yourself. Now your dead."
			return 'death'
			
		elif action == "slowly place the bomb":
			print "Nice stealth action there. You place the bomb."
			return 'escape_pod'
			
		else:
			print "DOES NOT COMPUTE!"
			return 'the_bridge'
			
		
class EscapePod(Scene):

	def enter(self):
		print "5 Pods. You know only one of 'em works. But which one?"
		
		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")
		
		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button." % guess
			print "Unfortunatelly it is faulty and explodes immediately"
			return 'death'
			
		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easily slides out into space heading to"
			print "the planet below. As it flies to the planet, you look"
			print "back and see your ship implode then explode like a"
			print "bright star, taking out the Gothon ship at the same"
			print "time. You won!"
			
			return 'finished'
		
class Finished(Scene):

	def enter(self):
		print "You won! Good job."
		return 'finished'
		
class Map(object):

	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finished(),
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()