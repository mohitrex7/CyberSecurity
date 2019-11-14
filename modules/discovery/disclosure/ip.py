

from utils import parser
from utils import output

def IP(content):
	list_ip = parser.Parser(content).getip()
	if len(list_ip) > 1:
		output.Output().plus('Found Private IP: %s'%str(list_ip).split('[')[1].split(']')[0])
	elif len(list_ip) == 1:
		output.Output().plus('Found Private IP: %s'%list_ip[0])
