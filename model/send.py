import glob
import pandas
from data import Data 

def test():
	d = Data()
	d.convertTableToDf()
	print d.df[:1]

class Sender():
	
	def __init__(self):
		# key: album, val: list of albums already compared
		# or: hash of sets of albums compared for faster lookup?
		self.archive = dict()
