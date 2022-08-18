from utils.settings import *
from .person import *
from utils import utils

class Family:
	"""
	Class to create the Family
	"""

	def __init__(self):
		self.members = {} # Now storing in dictionary and doing search by key. As name is unique so making key as name to avoid duplicates

	def add_king_queen(self, name, gender):
		"""
		Function to Add King and Queen.Also 
		There is no Mother or Father to them 
		"""

		member = Person(name, gender, None)
		self.members[member.name] = member

		return SUCCESS_MESSAGE["MEMBER_ADDITION_SUCCEEDED"]

	def add_spouse(self, person_name, spouse_name, gender):

		person = utils.get_member(self, person_name)
		
		message = []
		if(person and person.spouse is None):
			spouse = Person(spouse_name, gender, None)
			person.add_spouse_name(spouse) 
			spouse.add_spouse_name(person) 
			self.members[spouse.name] = spouse

			message.append(SUCCESS_MESSAGE["MEMBER_ADDITION_SUCCEEDED"])

		else:
			message.append(ERROR_MESSAGE["PERSON_NOT_FOUND"])

		return message


	def add_child(self, mother, child_name, gender):

		member = utils.get_member(self, mother)
		message = []

		if(member and member.gender == GENDER["FEMALE"]): # Check so that adding with Father it throws CHILD_ADDITION_FAILED
			person = Person(child_name, gender, member)
			member.add_child(person)
			self.members[person.name] = person
			message.append(SUCCESS_MESSAGE["CHILD_ADDITION_SUCCEEDED"])

		elif(member and member.gender == GENDER["MALE"]):
			message.append(ERROR_MESSAGE["CHILD_ADDITION_FAILED"])
			
		else:
			message.append(ERROR_MESSAGE["PERSON_NOT_FOUND"])

		return message




