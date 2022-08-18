import sys
sys.dont_write_bytecode = True

from src.family_tree import *
from file_processor.file_processing import *
from utils.settings import *

filename = sys.argv[1]

def main():
	family = Family()
	file_processing = FileProcessor()
	file_processing.process_file(family, '../FamilyTree/familytree.txt', True)
	file_processing.process_file(family, filename, False)

if __name__ == '__main__':
	main()
