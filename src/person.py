from utils.settings import *
from utils import utils

class Person:
	"""
	This class will be used to create the family tree
	"""
	def __init__(self, name, gender, mother):
		"""
		Person have these attributes associated with it
		"""
		self.name = name
		self.gender = gender
		self.mother = mother
		self.children = []
		self.spouse = None
	
	def add_spouse_name(self, spouse):
		self.spouse = spouse

	def add_child(self, child):
		self.children.append(child)

	@property
	def siblings(self):
		siblings_array = []

		if(self.mother):
			for person in self.mother.children:
				if(person.name != self.name):
					siblings_array.append(person)
		
		return siblings_array