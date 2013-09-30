from random import randint


quips = ["""You are knocked out. When you come to, you are a silvery misty version of yourself looking down at your own limp body. You are a ghost.""",
			"""Too bad you're not a cat. GAME OVER.""",
			"""You are dead. Sucks to be you.""",
			"""You are sent to Smeltings. Sorry."""]
					
class Player(object):

	def __init__(self):
		self.name = ''
		self.house = ''
		self.patronus = ''
		self.flying = False
		self.light = False
					
class Scene(object):

	def __init__(self):
		self.invent = {}
		
	def add_invent(self, stuff):
		self.invent.update({stuff.name: stuff})
		
	def remove_invent(self, stuff):
		del self.invent[stuff.name]
			
	def move(self, thing, destination):
		if thing in self.invent.keys():
			if thing not in destination.invent.keys():
				item = self.invent[thing]
				destination.add_invent(item)
				self.remove_invent(item)
			else:
				print "You're already carrying it!"
		else:
			print "I don't see that here."

class Inventory(Scene):

	def look(self):
		for name, thing in self.invent.items():
			print thing.name
						
class Death(object):
	
	def look(self):
		print quips[randint(0,len(quips)-1)]		
		exit(1)
		
		
inventory = Inventory()
death = Death()
you = Player()
		
