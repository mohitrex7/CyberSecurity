

from utils import parser
from utils import output

def Card(content):
	cc = parser.Parser(content).getcc()
	if len(cc) > 1:
		output.Output().plus('Found Credit Cards: %s'%str(cc).split('[')[1].split(']')[0])
	elif len(cc) == 1:
		output.Output().plus('Found Credit Card: %s'%cc[0])
