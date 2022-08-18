import sys
import os

from utils.settings import *
from src.family_tree import *
from utils import utils

class FileProcessor:
	# def __init__(self, filename):

	def process_file(self, family, filename, isFile):
		message_arr = []

		with open(filename, 'r') as file:
			data = file.read().split('\n') # As getting \n at end of each line so to avoid that
		for line in data:
			
			if(isFile):
				self.process_command(line, family) # File Only to create the familytree .
			else:
				for messages in self.process_command(line, family):
					print(messages,end=" ")
				print() # to make the new message appear on next line
		return

	def process_command(self, line, family):

		command_line = line.split(" ")
		command = command_line[0]
		message = None

		if(command == ACTIONS["ADD_CHILD"]):
			mother, child_name, gender = command_line[1:]
			message = family.add_child(mother, child_name, gender)

		elif(command == ACTIONS["ADD_SPOUSE"]):
			name, spouse_name, gender = command_line[1:]
			message = family.add_spouse(name, spouse_name, gender)

		elif(command == ACTIONS["ADD_FAMILY_HEAD"]):
			name, gender = command_line[1:]
			message = family.add_king_queen(name, gender)

		elif(command == ACTIONS["GET_RELATIONSHIP"]):
			name = command_line[1]
			relation = command_line[2]
			message = utils.get_relationship(family, name, relation) # passing utils here

		else:
			message = [ERROR_MESSAGE["INVALID_COMMAND"]]

		return message