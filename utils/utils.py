from .settings import *
from src.person import *
from src.relationship import Relationship

relation_instance = Relationship()

def is_empty_arr(arr):
	if(len(arr) == 0):
		arr.append(ERROR_MESSAGE["NONE"])
	return arr
		

def get_member(self, name):
	"""
	Return the single person object having this name 
	"""
	member = None
	for members in self.members: # Now searching in python dictionary makes it O(1)		
		if(name in self.members):
			member = self.members[name]

	return member

def get_relationship(family, name, relationship):
	message = []
	person = get_member(family, name)

	if not person:
		message.append(ERROR_MESSAGE["PERSON_NOT_FOUND"])

	if relationship not in RELATIONS:
		message.append(ERROR_MESSAGE["INVALID_RELATIONSHIP"])

	if(len(message) == 0):
		return get_relationship_status(family, person, relationship)

	return message

def get_relationship_status(family, person, relation):
	names_array = []

	name = get_function_mapping(family, person, relation)
	for member in name:
		names_array.append(member)

	return is_empty_arr(names_array)

def get_function_mapping(family, person, relation):

	relation_mapping =  {
		# All Self function are declared in person class
		"Son" : lambda: relation_instance.get_children(family, person, GENDER["MALE"]),
		"Daughter" : lambda: relation_instance.get_children(family, person, GENDER["FEMALE"]),
		"Siblings" : lambda: relation_instance.get_siblings(family, person),
		"Paternal-Uncle" : lambda: relation_instance.get_paternal_relations(family, person, GENDER["MALE"]),
		"Paternal-Aunt" : lambda: relation_instance.get_paternal_relations(family, person, GENDER["FEMALE"]),
		"Maternal-Uncle" : lambda: relation_instance.get_maternal_relations(family, person, GENDER["MALE"]), 
		"Maternal-Aunt" : lambda: relation_instance.get_maternal_relations(family, person, GENDER["FEMALE"]),
		"Sister-In-Law" : lambda: relation_instance.get_in_laws_relations(family, person, GENDER["FEMALE"]), 
		"Brother-In-Law" : lambda: relation_instance.get_in_laws_relations(family, person, GENDER["MALE"])

	}

	return relation_mapping.get(relation, lambda: 'INVALID_REALTION')()
