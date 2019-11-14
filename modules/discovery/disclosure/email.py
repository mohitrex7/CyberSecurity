

from utils import parser
from utils import output

def Email(content):
	list_email = parser.Parser(content).getmail()
	if len(list_email) > 1:
		output.Output().plus('Found Emails: %s'%str(list_email).split('[')[1].split(']')[0])
	elif len(list_email) == 1:
		output.Output().plus('Found Email: %s'%list_email[0])
