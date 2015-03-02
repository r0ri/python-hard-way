class Scene(object):

	def enter(self):
		pass
		
class Engine(object):

	def __init__(self, scene_map):
		pass
		
	def play(self):
		pass
		
class Death(Scene):
	
	def enter(self):
		pass
		
class CentralCorridor(Scene):

	def enter(self):
		print "Your Ship has been assaulted by Gothons."
		print "You are in the main corridor where you see one Gothon lurking around."
		print "You realize that you carry you carry nothing more than a fork."
		print "The Gothon spots you and shoots his laser."
		print "What do you do?"
		action = raw_input("> ")
		
		if action == "dodge!":
			print "You elegantly dodge the laser."
			print "Perform an action roll."
			print "... and crash into the dishes that you left lying around."
			print "The strong smell immediately renders you unconscious."
			print "You awake to the feeling of a bunch of Gothons gnawing at your intestines."
			print "We'll, that was a shitty day. You're dead"
			return 'death'
		elif action == "throw fork!":
			print "You heroeously throw your trusty fork at the Gothon."
			print "The fork hits the blaster shot midair and reflects it directly back at the"
			print "Gothon."
			print "The shot immediately kills the vile monster... and even if it hadn't, the"
			print "randomness of what just happened would have done the job as well."
			return 'laser'
		
class LaserWeaponArmory(Scene):

	def enter(self):
		pass
		
class TheBridge(Scene):

	def enter(self):
		pass
		
class EscapePod(Scene):
	
	def enter(self):
		pass
		
class Map(object):

	def __init__(self, start_scene):
		pass
		
	def next_scene(self, scene_name):
		pass
		
	def opening_scene(self):
		pass
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()