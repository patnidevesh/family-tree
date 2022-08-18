import unittest
import sys
from src.person import *
from src.relationship import Relationship
from src.family_tree import *
from utils import settings
from utils import utils

class TestPerson(unittest.TestCase):
	def family(self):
		family_tree = {}
		mother = Person("mother", settings.GENDER["FEMALE"], None)
		mother_spouse = Person("father", settings.GENDER["MALE"], None)
		mother.add_spouse_name(mother_spouse)
		mother_spouse.add_spouse_name(mother)

		male_child = Person("male_child", settings.GENDER["MALE"], mother)
		mother.children.append(male_child)
		male_child_2 = Person("male_child_2", settings.GENDER["MALE"], mother)
		mother.children.append(male_child_2)
		female_child = Person("female_child", settings.GENDER["FEMALE"], mother)
		mother.children.append(female_child)

		male_child_wife = Person("male_child_wife", settings.GENDER["FEMALE"], None)
		male_child.add_spouse_name(male_child_wife)
		male_child_wife.add_spouse_name(male_child)
		female_child_hus = Person("female_child_hus", settings.GENDER["MALE"], None)
		female_child.add_spouse_name(female_child_hus)
		female_child_hus.add_spouse_name(female_child)

		child_1 = Person("child_1", settings.GENDER["MALE"], male_child_wife)
		child_2 = Person("child_2", settings.GENDER["FEMALE"], male_child_wife)
		male_child_wife.children.append(child_1)
		male_child_wife.children.append(child_2)

		child_3 = Person("child_3", settings.GENDER["MALE"], female_child)
		child_4 = Person("child_4", settings.GENDER["MALE"], female_child)
		female_child.children.append(child_3)
		female_child.children.append(child_4)

		family_tree = {
			"mother": mother,
			"male_child": male_child,
			"male_child_2": male_child_2,
			"female_child": female_child,
			"child_1": child_1,
			"child_2": child_2,
			"child_3": child_3,
			"child_4": child_4,
		}
		return family_tree

	def test_mother(self):
		family_tree = self.family()
		self.assertEqual("mother", family_tree["mother"].name)
	
	def test_spouse(self):
		family_tree = self.family()
		self.assertEqual("father", family_tree["mother"].spouse.name)
	
	def test_male_child_spouse(self):
		family_tree = self.family()
		self.assertEqual("male_child_wife", family_tree["male_child"].spouse.name)

	def test_paternal_uncle(self):
		family_tree = self.family()
		relationship = Relationship()
		paternal_uncle = relationship.get_paternal_relations(family_tree,family_tree["child_2"], GENDER["MALE"])
		self.assertEqual(['male_child_2'],paternal_uncle)

	def test_paternal_aunt(self):
		family_tree = self.family()
		relationship = Relationship()

		paternal_aunt = relationship.get_paternal_relations(family_tree,family_tree["child_2"], GENDER["FEMALE"])
		self.assertEqual(['female_child'],paternal_aunt)

	def test_maternal_uncle(self):
		family_tree = self.family()
		relationship = Relationship()

		maternal_uncle = relationship.get_paternal_relations(family_tree,family_tree["child_3"], GENDER["MALE"])
		self.assertEqual(['NONE'],maternal_uncle)

	def test_maternal_aunt(self):
		family_tree = self.family()
		relationship = Relationship()

		maternal_aunt = relationship.get_paternal_relations(family_tree,family_tree["child_3"], GENDER["FEMALE"])
		self.assertEqual(['NONE'],maternal_aunt)

	def test_sister_in_law(self):
		family_tree = self.family()
		relationship = Relationship()

		sister_in_law = relationship.get_in_laws_relations(family_tree,family_tree["female_child"], GENDER["FEMALE"])
		self.assertEqual(['male_child_wife'],sister_in_law)

	def test_brother_in_law(self):
		family_tree = self.family()
		relationship = Relationship()

		brother_in_law = relationship.get_in_laws_relations(family_tree,family_tree["male_child_2"], GENDER["MALE"])
		self.assertEqual(['female_child_hus'],brother_in_law)

	def test_get_children(self):
		family_tree = self.family()
		relationship = Relationship()

		children = relationship.get_children(family_tree,family_tree["mother"], GENDER["FEMALE"])
		self.assertEqual(['male_child','male_child_2','female_child'], children)

	def test_get_siblings(self):
		family_tree = self.family()
		relationship = Relationship()

		siblings = relationship.get_siblings(family_tree,family_tree["male_child"])
		self.assertEqual(['male_child_2','female_child'], siblings)

	def test_get_siblings_mother(self):
		family_tree = self.family()
		relationship = Relationship()

		siblings = relationship.get_siblings(family_tree,family_tree["mother"])
		self.assertEqual(['NONE'], siblings)

if __name__ == '__main__':
	unittest.main()
