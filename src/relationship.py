from utils.settings import *
from .family_tree import *
from .person import *
from utils import utils

class  Relationship():
	"""docstring for  Relationship"""
	def __init__(self):
		pass

	def get_children(self, family, person, gender):
		"""
		Return Son/Daughter based on mother
		"""
		child_array = []

		for child in person.children:
			if(child.gender == gender):
				child_array.append(child.name)
		
		return utils.is_empty_arr(child_array)

	def get_siblings(self, family, person):
		sibling_array = []
		
		for member in person.siblings:
			sibling_array.append(member.name)


		return utils.is_empty_arr(sibling_array)


	def get_paternal_relations(self, family, person, gender):
		"""
		Return Paternal Aunt/Uncle based on gender passed
		"""
		paternal_relations_arr = []
		
		if(person.mother):
			father = person.mother.spouse			
			for member in father.siblings:
				if(member.gender == gender):
					paternal_relations_arr.append(member.name)

		return utils.is_empty_arr(paternal_relations_arr)	

	def get_maternal_relations(self, family, person, gender):
		"""
		Return Maternal Aunt/Uncle based on gender passed
		"""
		maternal_relations_arr = []

		if(person.mother):
			for member in person.mother.siblings:
				if(member.gender == gender):
					maternal_relations_arr.append(member.name)
		return utils.is_empty_arr(maternal_relations_arr)


	def get_in_laws_relations(self, family, person, gender):
		"""
		Return the Sister/Brother In Laws
		"""
		in_laws_relations_arr = []

		spouse = person.spouse

		if((spouse) and (spouse.mother is not None)):
			for member in spouse.mother.children:
				if(member.gender == gender and member.name != spouse.name):
					in_laws_relations_arr.append(member.name)
			
		for sibling in person.siblings:
				if(sibling.spouse is not None and sibling.spouse.gender == gender):
					in_laws_relations_arr.append(sibling.spouse.name)

		return utils.is_empty_arr(in_laws_relations_arr)


